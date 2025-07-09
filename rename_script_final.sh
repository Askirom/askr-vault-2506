#!/bin/bash
# Script to recursively rename files and directories to kebab-case.

# Define the top-level directories to process
TARGET_DIRS=("/Users/askirom/Documents/Askr.Vault-2506/archive" "/Users/askirom/Documents/Askr.Vault-2506/lib" "/Users/askirom/Documents/Askr.Vault-2506/sys" "/Users/askirom/Documents/Askr.Vault-2506/tmp" "/Users/askirom/Documents/Askr.Vault-2506/var")

for dir in "${TARGET_DIRS[@]}"; do
  # Check if the directory exists
  if [ -d "$dir" ]; then
    # Use find to handle renaming, ignoring errors for files that don't match
    find "$dir" -depth -name "*_" -exec bash -c 'mv -n "$0" "${0//_/-}"' {} \; 2>/dev/null
    find "$dir" -depth -name "* *" -exec bash -c 'mv -n "$0" "${0// /-}"' {} \; 2>/dev/null
  fi
done
