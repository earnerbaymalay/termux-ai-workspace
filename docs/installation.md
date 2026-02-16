# 📋 Installation Guide

Complete setup guide for the Termux AI Workspace on Android.

## Prerequisites

Before starting the installation, ensure your Android device meets these requirements:

- Android 7.0 (API level 24) or higher
- At least 4GB of free storage space (8GB+ recommended)
- Stable internet connection
- USB debugging enabled (optional, for advanced features)

## Step-by-Step Termux Setup

### 1. Install Termux

1. Download Termux from F-Droid (recommended) or GitHub releases
2. Open the Termux app
3. Grant storage permission when prompted (required for some features)

### 2. Initial Configuration

Run these commands in your Termux terminal:

```bash
# Update package lists
pkg update && pkg upgrade

# Install essential packages
pkg install git curl wget proot nano vim openssh nodejs python rust golang

# Set up storage access (optional but recommended)
termux-setup-storage
```

### 3. Install F-Droid Apps

Install these complementary apps from F-Droid:

- **Termux:API**: Access Android APIs from Termux
- **Termux:Widget**: Home screen widgets for running scripts
- **Termux:Float**: Floating terminal window
- **Material Files**: Material Design file manager
- **Simple Mobile Tools**: Suite of minimalistic apps

### 4. Clone and Set Up the Workspace

```bash
# Clone the repository
git clone https://github.com/earnerbaymalay/termux-ai-workspace.git

# Navigate to the workspace
cd termux-ai-workspace

# Make setup script executable
chmod +x setup.sh

# Run the setup script
bash setup.sh
```

### 5. Install AI Tools

```bash
# Install Ollama for local AI models
curl -fsSL https://ollama.ai/install.sh | sh

# Install Python AI libraries
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install tensorflow transformers datasets accelerate
```

### 6. Install Security Tools

```bash
# Install network security tools
pkg install nmap wireshark tcpdump aircrack-ng metasploit

# Install encryption tools
pkg install openssl gnupg
```

### 7. Install RF/SDR Tools

```bash
# Install GNU Radio (may require compilation)
pkg install gnuradio

# Install RTL-SDR tools
pkg install rtl-sdr
```

## Widget Setup

### 1. Termux:Widget Configuration

1. Install Termux:Widget from F-Droid
2. Create scripts in `~/termux-widgets/` directory
3. Add widgets to your home screen through the widget picker

### 2. Example Widget Script

Create a file `~/termux-widgets/status.sh`:

```bash
#!/bin/bash
echo "Battery: $(termux-battery-status | jq -r '.percentage')%"
echo "Memory: $(free -h | awk 'NR==2{print $3 "/" $2}')"
echo "Disk: $(df -h $HOME | awk 'NR==2{print $3 "/" $2}')"
```

Make it executable:

```bash
chmod +x ~/termux-widgets/status.sh
```

## Verification Steps

After completing the installation, verify everything is working:

### 1. Check Core Tools

```bash
# Verify Git
git --version

# Verify Python
python --version

# Verify Node.js
node --version

# Verify Ollama (if installed)
ollama --version
```

### 2. Test AI Capabilities

```bash
# Pull a model with Ollama
ollama pull llama3.2

# Run a simple test
ollama run llama3.2
```

### 3. Test Security Tools

```bash
# Test Nmap
nmap --version

# Test basic network scan (on your own network only)
nmap 127.0.0.1
```

### 4. Check Directory Structure

Verify that the following directories exist:

```bash
ls -la ~/termux-ai-workspace/
ls -la ~/termux-ai-workspace/demos/
ls -la ~/termux-ai-workspace/docs/
ls -la ~/termux-ai-workspace/scripts/
```

## Troubleshooting

### Common Issues

#### Storage Permission Error
If you encounter storage permission errors:
1. Re-run `termux-setup-storage`
2. Restart the Termux app
3. Check Android Settings > Apps > Termux > Permissions

#### Package Installation Failures
If packages fail to install:
1. Update package lists: `pkg update && pkg upgrade`
2. Clean package cache: `pkg clean`
3. Try installing the package individually

#### Ollama Not Starting
If Ollama fails to start:
1. Check if it's running: `ps aux | grep ollama`
2. Start manually: `ollama serve`
3. Check logs: `ollama serve 2>&1 | tee ollama.log`

### Performance Tips

- Close other apps when running AI models
- Use smaller models on devices with limited RAM
- Increase swap space if needed: `termux-change-repo` for additional packages

## Next Steps

After successful installation:

1. Explore the [Quick Reference](QUICK-REFERENCE.md) guide
2. Review the [Workflow Guides](workflows/)
3. Customize your environment in `~/.bashrc` or `~/.zshrc`
4. Join the community discussions for tips and updates

---

<div align="center">
  <sub>Congratulations! Your Termux AI Workspace is now set up and ready to use. 🎉</sub>
</div>