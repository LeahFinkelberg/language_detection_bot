#!/bin/sh
site_packages="$(python -m pip show langdetect | grep '^Location: ' | cut -d ':' -f 2-)"
exec "$(dirname "$0")"/gen-profile.sh "$1" "$2" "$site_packages/profiles/"
