#!/bin/bash
# Script to recursively rename files and directories

VAULT_PATH="/Users/askirom/Documents/Askr.Vault-2506/migrated_vault"

# Go into the target directory
cd "$VAULT_PATH" || exit

# Find all directories and files and rename them to replace underscores with hyphens
find . -depth -name "*_" -exec bash -c 'mv "$0" "${0//_/-}"' {} \;

# Find all directories and files and rename them to replace spaces with hyphens
find . -depth -name "* *" -exec bash -c 'mv "$0" "${0// /-}"' {} \;
