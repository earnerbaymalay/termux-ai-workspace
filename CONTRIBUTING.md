# 🤝 Contributing to Termux AI Workspace

Thank you for your interest in contributing to the Termux AI Workspace! This document outlines the guidelines for contributing to this project.

## 🚀 Getting Started

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/termux-ai-workspace.git
   ```
3. Create a branch for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## 📋 Contribution Guidelines

### Code Style
- Follow the existing code style in the project
- Use descriptive variable and function names
- Comment complex code sections appropriately
- Keep scripts modular and reusable

### Documentation
- Update documentation to reflect your changes
- Add examples where appropriate
- Follow the existing documentation format

### Testing
- Test your changes in a Termux environment
- Verify that scripts work as expected
- Document any new dependencies

## 🛠️ Types of Contributions

### Scripts
- Add new automation scripts to the `scripts/` directory
- Organize scripts into appropriate subdirectories (network, automation, bench)
- Ensure scripts are executable and well-documented

### Widgets
- Create new widgets in the `~/.shortcuts/` directory
- Follow the naming convention used by existing widgets
- Test widgets before submitting

### Documentation
- Improve existing documentation
- Add new guides or tutorials
- Fix typos and grammatical errors

### Bug Reports
- Use the issue tracker to report bugs
- Describe the problem in detail
- Include steps to reproduce the issue

## 📦 Pull Request Process

1. Ensure your code follows the project's style guidelines
2. Update documentation as needed
3. Add tests if applicable
4. Submit a pull request with a clear description of your changes
5. Address any feedback from reviewers

## 🤖 AI Integration

When contributing AI-related features:
- Ensure compatibility with Ollama
- Test with multiple AI models where applicable
- Follow privacy and security best practices

## 📁 Directory Structure

```
termux-ai-workspace/
├── demos/                 # Demo content
│   ├── screenshots/
│   ├── recordings/
│   └── gifs/
├── docs/                  # Documentation
│   ├── api/
│   ├── workflows/
│   └── examples/
├── scripts/               # Scripts organized by category
│   ├── network/
│   ├── automation/
│   ├── bench/
│   └── tests/
├── setup/                 # Setup scripts and configurations
├── templates/             # Template files
└── README.md              # Main project documentation
```

## 🧪 Testing Your Changes

Before submitting your changes:
1. Test scripts in your Termux environment
2. Verify that all dependencies are documented
3. Ensure your changes don't break existing functionality

## 🙏 Thank You

Your contributions help make the Termux AI Workspace better for everyone! If you have questions, feel free to open an issue for discussion.