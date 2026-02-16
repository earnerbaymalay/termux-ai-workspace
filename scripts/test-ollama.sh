#!/data/data/com.termux/files/usr/bin/bash
# Test script to verify HTTP shortcut functionality
curl -s http://localhost:11434/api/tags | jq -r ".models[].name"
