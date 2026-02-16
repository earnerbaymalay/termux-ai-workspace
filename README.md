# Termux AI Workspace [![GitHub stars](https://img.shields.io/github/stars/earnerbaymalay/termux-ai-workspace.svg)](https://github.com/earnerbaymalay/termux-ai-workspace/stargazers) [![License](https://img.shields.io/github/license/earnerbaymalay/termux-ai-workspace.svg)](https://github.com/earnerbaymalay/termux-ai-workspace/blob/main/LICENSE) [![Last Commit](https://img.shields.io/github/last-commit/earnerbaymalay/termux-ai-workspace.svg)](https://github.com/earnerbaymalay/termux-ai-workspace/commits/main) [![Issues](https://img.shields.io/github/issues/earnerbaymalay/termux-ai-workspace.svg)](https://github.com/earnerbaymalay/termux-ai-workspace/issues)

A comprehensive local-first AI development environment on Android using Termux + Ollama and various AI tools.
# Termux AI Workspace

A comprehensive local-first AI development environment on Android using Termux + Ollama and various AI tools.

## Project Description

This repository contains a complete setup for an AI development environment on Android devices using Termux. It includes scripts, configurations, and templates to set up a powerful local AI workspace that can run completely offline.

## Features

✓ **Termux Environment**: Complete Termux setup with TUR (Termux Unstable Repository), X11, and root repositories  
✓ **Python AI Tools**: Ollama, Anthropic API, and various AI libraries configured  
✓ **Network/Security Tools**: Network scanning, security tools, and API interfaces  
✓ **RF/SDR Tools**: Radio frequency and software-defined radio tools  
✓ **F-Droid Apps**: Pre-configured F-Droid repositories with fingerprints  
✓ **Syncthing + Obsidian Integration**: Seamless file synchronization and note-taking  
✓ **Widget Scripts**: Quick-access scripts for common AI tasks  
✓ **HTTP Shortcuts Templates**: Pre-configured API shortcuts for AI services  
✓ **Checkpoint System**: Automatic backup and restore functionality  

## Installation Guide

1. Install Termux from F-Droid (recommended) or GitHub
2. Run the setup script:
   ```bash
   # Clone this repository
   git clone https://github.com/YOUR_USERNAME/termux-ai-workspace.git
   cd termux-ai-workspace
   
   # Run the setup script
   bash setup/termux-setup.sh
   ```
3. Follow the prompts to complete the installation
4. Add your API keys to the appropriate configuration files

## Usage Examples

- Run `checkpoint` to create a backup of your current setup
- Use `qwen-chat` to start a chat with Qwen AI model
- Access widget scripts from the Termux home screen
- Use HTTP Shortcuts for quick API calls to AI services

## File Structure Overview

```
termux-ai-workspace/
├── README.md
├── LICENSE
├── ROADMAP.md
├── CHANGELOG.md
├── setup/
│   ├── termux-setup.sh
│   ├── fdroid-repos.txt
│   ├── pip-requirements.txt
│   └── config/
├── scripts/
│   ├── checkpoint
│   ├── qwen-chat
│   ├── ai-helper.py
│   ├── ai-context
│   ├── auto-log
│   └── widget-scripts/
├── templates/
│   ├── obsidian/
│   └── http-shortcuts/
└── docs/
```

## Contributing Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.