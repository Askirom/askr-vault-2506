import os
import re
import shutil

def get_alias_from_file(file_path):
    """Extracts the first alias from the YAML frontmatter of a Markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            in_frontmatter = False
            for line in f:
                if line.strip() == '---':
                    in_frontmatter = not in_frontmatter
                    continue
                if in_frontmatter and line.strip().startswith('aliases:'):
                    # Handle single-line or multi-line aliases
                    if '[' in line and ']' in line:
                        alias = line.split('[')[1].split(']')[0].replace('"', '').strip()
                        return alias
                    else:
                        # Look for the next line with the alias
                        next_line = next(f).strip()
                        if next_line.startswith('-'):
                            return next_line.replace('-', '').strip()
    except Exception as e:
        print(f"Error reading alias from {file_path}: {e}")
    return None

def to_kebab_case(name):
    """Converts a string to kebab-case."""
    name = re.sub(r'[\s_\\/]+', '-', name)
    name = re.sub(r'[^a-zA-Z0-9-]', '', name)
    return name.lower()

def process_files():
    """
    Finds Markdown files with UUID-like names, renames them to their kebab-cased alias,
    and adds the original filename as a 'uuid' property in the frontmatter.
    """
    rename_map = {}
    for root, dirs, files in os.walk("."):
        # Exclude hidden directories
        dirs[:] = [d for d in dirs if not d.startswith('.')]

        for file in files:
            if file.endswith(".md") and (file[:-3].isdigit() or (file.startswith('20') and '-' in file)):
                file_path = os.path.join(root, file)
                alias = get_alias_from_file(file_path)
                
                if alias:
                    new_name = to_kebab_case(alias) + ".md"
                    new_path = os.path.join(root, new_name)
                    
                    if os.path.exists(new_path) and new_path != file_path:
                        print(f"Warning: File '{new_path}' already exists. Skipping rename for '{file_path}'.")
                        continue
                        
                    rename_map[file_path] = new_path

    print(f"Found {len(rename_map)} files to rename.")

    for old_path, new_path in rename_map.items():
        try:
            if not os.path.exists(old_path):
                continue

            with open(old_path, 'r', encoding='utf-8') as f:
                content = f.read()

            uuid = os.path.basename(old_path)[:-3]
            
            if 'uuid:' not in content:
                id_match = re.search(r'id:\s*([^\n]+)', content)
                if id_match:
                    id_line = id_match.group(0)
                    new_content = content.replace(id_line, f"{id_line}\nuuid: {uuid}")
                else:
                    new_content = f"---\nuuid: {uuid}\n---\n" + content
            else:
                new_content = content

            with open(old_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

            shutil.move(old_path, new_path)
            print(f"Renamed '{old_path}' to '{new_path}'")

        except Exception as e:
            print(f"Error processing file '{old_path}': {e}")

if __name__ == "__main__":
    process_files()
