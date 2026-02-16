# HTTP Shortcuts for Ollama API

This directory contains configuration files for HTTP Shortcuts that connect to the Ollama API.

## Available Shortcuts

### Quick AI Query
- Makes a POST request to the Ollama generate endpoint
- Allows you to input a custom prompt
- Shows the response as a toast notification

### Code Review
- Makes a POST request to the Ollama generate endpoint
- Reviews code from your clipboard
- Shows the response as a notification

### Check Models
- Makes a GET request to the Ollama tags endpoint
- Lists all available models
- Shows the response in a dialog

## Setup Instructions

1. Install "HTTP Shortcuts" app from F-Droid or Google Play
2. Import the ollama-shortcuts.json file using the import feature
3. The shortcuts will be available in the app for execution

## Prerequisites

- Ollama service running locally (port 11434)
- The qwen model installed in Ollama

