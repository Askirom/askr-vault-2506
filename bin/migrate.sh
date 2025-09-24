#!/bin/bash

#
# This script migrates a single file into the Askirom PKM v4 system.
# Usage: ./migrate.sh /path/to/your/file.md
#

set -e

# --- 1. VALIDATE INPUT ---

if [ -z "$1" ]; then
  echo "Error: No file path provided." >&2
  echo "Usage: $0 <file_path>" >&2
  exit 1
fi

if [ ! -f "$1" ]; then
  echo "Error: File not found at '$1'" >&2
  exit 1
fi

FILE_PATH="$1"
VAULT_ROOT="$PWD"
FILENAME=$(basename "$FILE_PATH")

# --- 2. HELPER FUNCTIONS ---

# Slugify a string for use in filenames
# Ex: "My File Name!" -> "my-file-name"
slugify() {
  echo "$1" | tr '[:upper:]' '[:lower:]' | sed -e 's/[^a-z0-9._-]//g' -e 's/^[ 	]*//;s/[ 	]*$//' -e 's/[ 	]/-/g' | sed 's/--+/-/g'
}

# Extract a value from YAML frontmatter
# Usage: get_yaml_value "key" "/path/to/file"
get_yaml_value() {
  local key="$1"
  local file="$2"
  # Use awk to parse the frontmatter block (between --- lines)
  awk '
    /^---$/ { in_yaml = !in_yaml; if (!in_yaml) exit; next }
    in_yaml && /^"$key":/ {
      sub(/^"$key":[ 	]*/, "");
      gsub(/^["']|["']$/, "");
      print;
      exit;
    }
  ' "$file"
}

# --- 3. PREPARE FILE ---

# Ensure the file has YAML frontmatter, add a default if it doesn't
if ! head -n 1 "$FILE_PATH" | grep -q "^---"; then
  TEMP_FILE=$(mktemp)
  # Default to a 'knowledge' type, which will be routed to /usr/reference
  cat <<EOF > "$TEMP_FILE"
---
"type": "knowledge"
"status": "seedling"
"tags": []
---

EOF
  cat "$FILE_PATH" >> "$TEMP_FILE"
  mv "$TEMP_FILE" "$FILE_PATH"
fi

# --- 4. READ METADATA & ROUTE ---

CLIENT=$(get_yaml_value "client" "$FILE_PATH")
PROJECT=$(get_yaml_value "project" "$FILE_PATH")
TYPE=$(get_yaml_value "type" "$FILE_PATH")
SLUG=$(slugify "$FILENAME")

# Route to a project folder if client and project are defined
if [ -n "$CLIENT" ] && [ -n "$PROJECT" ]; then
  PROJECT_DIR="$VAULT_ROOT/srv/$CLIENT/$PROJECT"

  # Ensure the standard project directory structure exists
  mkdir -p "$PROJECT_DIR/notes"
  mkdir -p "$PROJECT_DIR/deliverables"
  touch "$PROJECT_DIR/_index.md" "$PROJECT_DIR/meetings.md" "$PROJECT_DIR/decisions.md" "$PROJECT_DIR/backlog.md"

  case "$TYPE" in
    project)
      # The file itself is the project's main page
      mv "$FILE_PATH" "$PROJECT_DIR/_index.md"
      ;;
    meeting-log)
      # Append content to the project's meeting log
      echo -e "\n\n---
" >> "$PROJECT_DIR/meetings.md"
      # Strip frontmatter from source file before appending
      sed '1,/^---$/d' "$FILE_PATH" >> "$PROJECT_DIR/meetings.md"
      rm "$FILE_PATH"
      ;;
    decision)
      # Append content to the project's decision log
      echo -e "\n\n---
" >> "$PROJECT_DIR/decisions.md"
      sed '1,/^---$/d' "$FILE_PATH" >> "$PROJECT_DIR/decisions.md"
      rm "$FILE_PATH"
      ;;
    action|knowledge|standard)
      # File becomes a note within the project
      mv "$FILE_PATH" "$PROJECT_DIR/notes/$SLUG"
      ;;
    *)
      # Default action: move to the project's notes folder
      mv "$FILE_PATH" "$PROJECT_DIR/notes/$SLUG"
      ;;
  esac
  echo "Migrated to project: $PROJECT_DIR"
else
  # Route to a standard folder based on file type
  DEST_DIR=""
  case "$TYPE" in
    daily)       DEST_DIR="$VAULT_ROOT/var/daily" ;; 
    meeting-log) DEST_DIR="$VAULT_ROOT/var/meeting" ;; 
    decision)    DEST_DIR="$VAULT_ROOT/var/decision" ;; 
    action)      DEST_DIR="$VAULT_ROOT/var/action" ;; 
    knowledge)   DEST_DIR="$VAULT_ROOT/usr/reference" ;; 
    standard)    DEST_DIR="$VAULT_ROOT/usr/standards" ;; 
    *)           DEST_DIR="$VAULT_ROOT/tmp" ;; 
  esac

  mkdir -p "$DEST_DIR"
  mv "$FILE_PATH" "$DEST_DIR/$SLUG"
  echo "Migrated to: $DEST_DIR/$SLUG"
fi

exit 0
