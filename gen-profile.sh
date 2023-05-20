#!/bin/sh
if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
  printf "Usage: %s <source_file> <language_code> <target_dir>" "$0"
fi
file=$1
code=$2
target=$3
dir=$(mktemp -d)
scriptdir=$(dirname "$0")

mkdir -p "$dir/profiles/"

cp "$file" "$dir/"
java -jar "$scriptdir/langdetect.jar" --genprofile -d "$dir" "$code"
cp "$dir/profiles/$code" "$target/"
