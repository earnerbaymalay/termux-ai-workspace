# Checkpoint Script

This script provides automatic checkpoint functionality for your development workflow.

## Usage

```bash
~/ai/scripts/checkpoint "Description of the step completed"
```

If no description is provided, it defaults to "Progress update".

## Features

- Automatically navigates to the ~/termux-ai-workspace directory
- Updates the ROADMAP.md file by checking off the completed step
- Adds an entry to the CHANGELOG.md file with timestamp
- Commits and pushes changes to the main branch
- Shows a notification confirming the checkpoint was saved

## Requirements

- A git repository named "termux-ai-workspace" in your home directory
- Proper git configuration and remote access
- Termux-API for notifications

