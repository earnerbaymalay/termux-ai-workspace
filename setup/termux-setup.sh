#!/bin/bash
#
# Termux AI Workspace Setup Script
# Sets up a complete AI development environment on Android using Termux

set -e  # Exit immediately if a command exits with a non-zero status

echo "==========================================="
echo "Termux AI Workspace Setup Script"
echo "==========================================="

# Function to print status messages
print_status() {
    echo -e "\033[1;34m[INFO]\033[0m $1"
}

# Function to print success messages
print_success() {
    echo -e "\033[1;32m[SUCCESS]\033[0m $1"
}

# Function to print error messages
print_error() {
    echo -e "\033[1;31m[ERROR]\033[0m $1"
}

# Check if running on Termux
if [ ! -d "$HOME/.termux" ]; then
    print_error "This script must be run in Termux on Android"
    exit 1
fi

print_status "Updating package lists..."
pkg update && pkg upgrade -y

print_status "Installing core packages..."
pkg install -y python nodejs rust golang git curl wget neovim tmux zsh nano htop openssh rsync

print_status "Installing AI development packages..."
pkg install -y ollama python-pip

print_status "Installing additional tools..."
pkg install -y termux-api gnuradio hackrf rtl-sdr gr-osmosdr

print_status "Setting up Python environment..."
pip install --upgrade pip
pip install ollama anthropic openai python-dotenv

print_status "Installing Oh My Zsh..."
if [ ! -d "$HOME/.oh-my-zsh" ]; then
    sh -c "$(curl -fsSL https://raw.github.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
else
    print_status "Oh My Zsh already installed"
fi

print_status "Installing Powerlevel10k theme..."
if [ ! -d "$HOME/.oh-my-zsh/custom/themes/powerlevel10k" ]; then
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git ${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}/themes/powerlevel10k
else
    print_status "Powerlevel10k already installed"
fi

print_status "Configuring Termux storage access..."
termux-setup-storage

print_status "Installing F-Droid repositories..."
# Add F-Droid repos from setup/fdroid-repos.txt
if [ -f "./setup/fdroid-repos.txt" ]; then
    while IFS= read -r repo_line; do
        if [[ $repo_line =~ ^[^#] ]]; then
            print_status "Adding repo: $repo_line"
            # Note: Actual F-Droid repo addition would happen in F-Droid app
        fi
    done < ./setup/fdroid-repos.txt
else
    print_status "No fdroid-repos.txt file found"
fi

print_status "Copying scripts to home directory..."
cp -r ./scripts/* $HOME/

print_status "Making scripts executable..."
chmod +x $HOME/checkpoint $HOME/qwen-chat

print_status "Setting up bashrc additions..."
BASHRC_ADDITIONS_FILE="./setup/config/bashrc-additions"
if [ -f "$BASHRC_ADDITIONS_FILE" ]; then
    # Append bashrc additions to .bashrc if not already present
    if ! grep -q "# AI Tool Paths & Aliases" ~/.bashrc; then
        cat "$BASHRC_ADDITIONS_FILE" >> ~/.bashrc
        print_success "Added AI configurations to .bashrc"
    else
        print_status "AI configurations already present in .bashrc"
    fi
else
    print_error "bashrc-additions file not found"
fi

print_status "Setting up pip configuration..."
PIP_CONFIG_DIR="$HOME/.config/pip"
mkdir -p "$PIP_CONFIG_DIR"
if [ -f "./setup/config/pip.conf" ]; then
    cp "./setup/config/pip.conf" "$PIP_CONFIG_DIR/"
    print_success "Copied pip configuration"
else
    print_error "pip.conf file not found"
fi

print_status "Installing additional Python packages from requirements..."
if [ -f "./setup/pip-requirements.txt" ]; then
    pip install -r ./setup/pip-requirements.txt
else
    print_status "No pip-requirements.txt file found, installing common AI packages..."
    pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
    pip install transformers datasets accelerate langchain-community
    pip install jupyter notebook
fi

print_status "Starting Ollama service..."
# Start Ollama in the background
nohup ollama serve > $HOME/ollama.log 2>&1 &

print_status "Setup complete!"
print_success "Your Termux AI Workspace is ready!"
echo ""
echo "Next steps:"
echo "1. Add your API keys to the appropriate configuration files"
echo "2. Run 'ollama pull qwen2:7b' to download a model (or your preferred model)"
echo "3. Start using the scripts in your home directory"
echo "4. Check out the HTTP Shortcuts templates in templates/http-shortcuts/"
echo ""

print_status "Please restart your Termux session or run 'source ~/.bashrc' to load the new configurations."