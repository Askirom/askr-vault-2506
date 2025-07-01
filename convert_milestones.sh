#!/bin/bash

# Script to convert remaining milestone files to regular project notes

VAULT_PATH="/Users/askirom/Documents/Askr.Vault-2506"

# Find remaining milestone files (excluding already converted ones)
find "$VAULT_PATH" -name "Milestone-*.md" -type f | while read -r file; do
    echo "Converting: $file"
    
    # Get directory and filename
    dir=$(dirname "$file")
    filename=$(basename "$file")
    
    # Create new filename without "Milestone-" prefix
    new_filename="${filename#Milestone-}"
    new_file="$dir/$new_filename"
    
    # Convert the file content
    # Remove YAML frontmatter and milestone-specific structure
    sed -e '/^---$/,/^---$/d' \
        -e 's/^# Milestone: /# /' \
        -e 's/^## 🎯 Win Condition$/## Project Overview/' \
        -e 's/^## 💰 Financial Impact$/## Financial Impact/' \
        -e '/^\*\*Completion:\*\*/d' \
        "$file" > "${file}.tmp"
    
    # Replace the file
    mv "${file}.tmp" "$new_file"
    
    # Remove original milestone file
    rm "$file"
    
    echo "Converted to: $new_file"
done

echo "Milestone conversion complete!"