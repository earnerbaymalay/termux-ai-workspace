# Termux:Widget Scripts for AI Access

This directory contains scripts that can be used with Termux:Widget to provide one-tap access to AI functions on your Android device.

## Available Scripts

### qwen-quick
- Prompts you to enter a question for Qwen
- Sends the question to the local Ollama instance
- Displays the response as a toast notification at the top of the screen

### analyze-code
- Gets the current clipboard content
- Sends it to Qwen for code analysis
- Creates a notification with the analysis results

### quick-nmap
- Performs a network scan of your local network (192.168.1.0/24)
- Creates a notification with the scan results

## Setup Instructions

1. Install Termux:Widget from F-Droid
2. On your home screen, long press and select "Widgets"
3. Choose "Termux:Widget" and resize to show all scripts
4. Tap any widget to run the corresponding script

## Prerequisites

- Ollama service running locally (port 11434)
- Required packages: jq, nmap, termux-api
- The ~/ai/scripts/qwen-chat script must be accessible