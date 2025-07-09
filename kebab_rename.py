import os
import re

def to_kebab_case(name):
    # Replace spaces and underscores with hyphens
    name = re.sub(r'[ _]+', '-', name)
    # Remove leading/trailing hyphens
    name = name.strip('-')
    return name

root_path = "/Users/askirom/Documents/Askr.Vault-2506/"
target_dirs = ["archive", "lib", "sys", "tmp", "var"]

for top_dir_name in target_dirs:
    top_dir_path = os.path.join(root_path, top_dir_name)
    if not os.path.exists(top_dir_path):
        continue

    # Walk through the directory tree, processing files and then directories
    # topdown=False ensures that files are renamed before their parent directories
    # are renamed, preventing path issues.
    for dirpath, dirnames, filenames in os.walk(top_dir_path, topdown=False):
        # Rename files
        for filename in filenames:
            old_path = os.path.join(dirpath, filename)
            new_filename = to_kebab_case(filename)
            if filename != new_filename:
                try:
                    os.rename(old_path, os.path.join(dirpath, new_filename))
                except OSError as e:
                    print(f"Error renaming file {old_path} to {os.path.join(dirpath, new_filename)}: {e}")

        # Rename directories
        for dirname in dirnames:
            old_path = os.path.join(dirpath, dirname)
            new_dirname = to_kebab_case(dirname)
            if dirname != new_dirname:
                try:
                    os.rename(old_path, os.path.join(dirpath, new_dirname))
                except OSError as e:
                    print(f"Error renaming directory {old_path} to {os.path.join(dirpath, new_dirname)}: {e}")
