# 📚 Quick Reference Guide

Essential commands, tools, and troubleshooting tips for the Termux AI Workspace.

## 🖥️ Common Commands

### Termux Basics
```bash
# Update packages
pkg update && pkg upgrade

# Search for packages
pkg search <package-name>

# Install packages
pkg install <package-name>

# List installed packages
pkg list-installed

# Clean package cache
pkg clean
```

### Git Operations
```bash
# Clone a repository
git clone <repository-url>

# Pull latest changes
git pull origin main

# Check status
git status

# Commit changes
git add .
git commit -m "Description of changes"

# Push changes
git push origin main
```

### Python Management
```bash
# Install packages
pip install <package-name>

# Upgrade packages
pip install --upgrade <package-name>

# List installed packages
pip list

# Create virtual environment
python -m venv myenv
source myenv/bin/activate
```

### Node.js Management
```bash
# Install packages globally
npm install -g <package-name>

# Install packages locally
npm install <package-name>

# Update packages
npm update

# List global packages
npm list -g --depth=0
```

## 🤖 AI Tools

### Ollama
```bash
# Start Ollama service
ollama serve

# List available models
ollama list

# Pull a model
ollama pull <model-name>

# Run a model
ollama run <model-name>

# Create a model
ollama create <model-name> -f Modelfile
```

### Common Models
- `llama3.2` - Lightweight, efficient model
- `mistral` - Great for coding tasks
- `neural-chat` - Good general-purpose model
- `phi3` - Microsoft's compact model

## 🛠️ Script Categories

### Network Scripts (`scripts/network/`)
```bash
# Network scanning
bash scripts/network/scan_network.sh

# Port scanning
bash scripts/network/port_scan.sh

# WiFi analysis
bash scripts/network/wifi_analyze.sh
```

### Automation Scripts (`scripts/automation/`)
```bash
# System monitoring
bash scripts/automation/monitor.sh

# Backup operations
bash scripts/automation/backup.sh

# Scheduled tasks
bash scripts/automation/scheduled_tasks.sh
```

### Benchmark Scripts (`scripts/bench/`)
```bash
# CPU benchmark
bash scripts/bench/cpu_benchmark.sh

# Memory benchmark
bash scripts/bench/memory_benchmark.sh

# AI model benchmark
bash scripts/bench/ai_benchmark.sh
```

## 📱 Widgets

### Available Widgets
- **System Status**: Shows battery, memory, and disk usage
- **AI Monitor**: Monitors AI model performance
- **Network Scanner**: Displays active network connections
- **Security Alert**: Shows security-related notifications

### Widget Locations
Widgets are stored in `~/termux-widgets/` directory. To create a new widget:

1. Create a script in `~/termux-widgets/`
2. Make it executable: `chmod +x script_name.sh`
3. Add the widget through the Android home screen widget picker

## 🌐 HTTP Shortcuts

### Common Endpoints
- `/api/system` - System information endpoint
- `/api/ai/status` - AI model status
- `/api/network` - Network information
- `/api/security` - Security status

### Creating HTTP Shortcuts
1. Install "HTTP Shortcuts" app from F-Droid
2. Create a new shortcut with the desired endpoint
3. Configure headers and parameters as needed
4. Add to home screen for quick access

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: Termux won't start
**Solution:**
```bash
# Clear app data from Android settings
# Or reset Termux: termux-reset
```

#### Issue: Package installation fails
**Solution:**
```bash
pkg update && pkg upgrade
pkg clean
# Then retry installation
```

#### Issue: Ollama not responding
**Solution:**
```bash
# Check if running
ps aux | grep ollama

# Kill and restart
pkill ollama
ollama serve &
```

#### Issue: Out of memory during AI tasks
**Solution:**
- Use smaller models
- Close other applications
- Increase swap space if possible

#### Issue: Permission denied
**Solution:**
```bash
# Check file permissions
ls -la filename

# Change permissions
chmod +x filename
```

### Performance Optimization
- Use `top` or `htop` to identify resource-intensive processes
- Limit concurrent AI model operations
- Regularly clean temporary files: `rm -rf /tmp/*`
- Monitor storage: `df -h`

## 🚨 Emergency Commands

### Stop All Services
```bash
# Stop Ollama
pkill ollama

# Stop all Python processes (be careful!)
pkill -f python

# Stop all Node.js processes
pkill -f node
```

### Reset Termux Environment
```bash
# Reset Termux (removes all packages)
termux-reset
```

### Emergency Cleanup
```bash
# Free up space
pkg clean
rm -rf ~/.cache/*
rm -rf ~/.npm/_cacache
```

## 📞 Support Resources

- [GitHub Issues](https://github.com/earnerbaymalay/termux-ai-workspace/issues)
- [Documentation](../README.md)
- [Installation Guide](installation.md)

---

<div align="center">
  <sub>Your quick reference for the Termux AI Workspace - bookmark this page! 📌</sub>
</div>