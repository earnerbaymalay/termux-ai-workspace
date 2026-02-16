#!/data/data/com.termux/files/usr/bin/bash
# Configure ~/bin with symlinks to scripts

mkdir -p ~/bin

# Link commonly used scripts
ln -sf ~/ai/scripts/checkpoint ~/bin/checkpoint
ln -sf ~/ai/scripts/qwen-chat ~/bin/qwen
ln -sf ~/ai/scripts/netmon ~/bin/netmon

# Add to PATH if not already
grep -q '~/bin' ~/.bashrc || echo 'export PATH=$PATH:~/bin' >> ~/.bashrc

echo "~/bin configured. Restart Termux or run: source ~/.bashrc"