#!/usr/bin/env bash
# web_search.sh
# Performs a privacy-respecting search using DuckDuckGo via Lynx.

QUERY="$1"

if [ -z "$QUERY" ]; then
    echo "Error: No search query provided."
    exit 1
fi

if ! command -v lynx &>/dev/null; then
    pkg install lynx -y >/dev/null
fi

# Sanitize and encode query
QUERY_ENCODED=$(echo "$QUERY" | sed 's/ /+/g; s/\"/%22/g; s/\&/%26/g')
SEARCH_URL="https://duckduckgo.com/html/?q=$QUERY_ENCODED"

lynx -dump -nonumbers "$SEARCH_URL" | grep -A 20 "Results" | head -n 50
