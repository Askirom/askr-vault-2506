#!/bin/bash

# Script to clean up underscore-dash-underscore patterns
# Replaces _-_ with just - for cleaner filenames

VAULT_PATH="/Users/askirom/Documents/Askr.Vault-2506"
LOG_FILE="$VAULT_PATH/dash_cleanup.log"

echo "Starting dash cleanup - $(date)" > "$LOG_FILE"

# Function to safely rename files and log changes
rename_file() {
    local old_path="$1"
    local new_path="$2"
    
    if [ "$old_path" != "$new_path" ] && [ -f "$old_path" ]; then
        mv "$old_path" "$new_path"
        echo "RENAMED: $old_path -> $new_path" >> "$LOG_FILE"
        echo "RENAMED: $(basename "$old_path") -> $(basename "$new_path")"
        return 0
    fi
    return 1
}

# Function to update wikilinks in files
update_wikilinks() {
    local old_name="$1"
    local new_name="$2"
    
    # Remove .md extension for wikilink matching
    old_link="${old_name%.md}"
    new_link="${new_name%.md}"
    
    if [ "$old_link" != "$new_link" ]; then
        # Find and update wikilinks in all markdown files
        find "$VAULT_PATH" -name "*.md" -type f -exec grep -l "\[\[$old_link\]\]" {} \; | while read -r file; do
            sed -i.bak "s/\[\[$old_link\]\]/[[$new_link]]/g" "$file"
            echo "UPDATED LINK: $old_link -> $new_link in $(basename "$file")" >> "$LOG_FILE"
            echo "UPDATED LINK: $old_link -> $new_link in $(basename "$file")"
            # Remove backup file
            rm "$file.bak" 2>/dev/null
        done
    fi
}

echo "Finding files with _-_ patterns..."

# Find all markdown files with _-_ patterns and process them
find "$VAULT_PATH" -name "*.md" -type f | while read -r file; do
    if [[ "$file" == *"_-_"* ]]; then
        # Get directory and filename
        dir=$(dirname "$file")
        filename=$(basename "$file")
        
        # Create new filename with clean dashes
        new_filename=$(echo "$filename" | sed 's/_-_/-/g')
        new_path="$dir/$new_filename"
        
        # Rename file and update links
        if rename_file "$file" "$new_path"; then
            update_wikilinks "$filename" "$new_filename"
        fi
    fi
done

echo "Dash cleanup completed - $(date)" >> "$LOG_FILE"
echo ""
echo "Cleanup complete! Check dash_cleanup.log for details."
echo "Total changes logged:"
grep -c "RENAMED:" "$LOG_FILE" 2>/dev/null || echo "0"