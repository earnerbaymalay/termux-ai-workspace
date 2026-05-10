# 🌌 Aether Droid — Troubleshooting Guide
### Version 26.04.2

Common issues and their solutions for the Aether Droid ecosystem.

---

## 📱 Termux (Android) Issues

### 🔴 Installation Fails
- **Issue:** Error during `pkg install` or `llama.cpp` build.
- **Solution:** Ensure you are using Termux from **F-Droid**. Run `pkg update && pkg upgrade -y` before running `./install.sh`.
- **Solution:** Ensure you have at least 5GB of free internal storage.

### 🟡 `ai` Command Not Found
- **Issue:** Typing `ai` does nothing.
- **Solution:** Run `source ~/.bashrc`. If it still fails, run:
  `echo "alias ai='$HOME/aether/aether.sh'" >> ~/.bashrc && source ~/.bashrc`

### 🟠 Out of Memory (OOM)
- **Issue:** Aether Droid crashes during inference or says "Killed".
- **Solution:** Decrease the thread count in **SETTINGS** (Menu 9). Try 2 or 4 threads.
- **Solution:** Switch to a smaller model (e.g., TURBO instead of AGENT).

---

## 💻 Desktop (Windows/WSL) Issues

### 🔴 Ollama Connection Failed
- **Issue:** Agent says `Ollama Inference Error`.
- **Solution:** Ensure Ollama is running. Open a terminal and type `ollama serve`.
- **Solution:** Verify the model is downloaded: `ollama pull llama3.1:8b`.

### 🟡 PowerShell Permission Error
- **Issue:** Toolbox scripts fail to run.
- **Solution:** Run PowerShell as Administrator once and execute:
  `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

---

## 🧠 Aether DroidVault & Memory Issues

### ⚪ Vault is Empty
- **Issue:** Auto-Memory isn't extracting facts.
- **Solution:** Background extraction requires a secondary model run. If your device is slow, this may take a few moments after you finish typing.
- **Solution:** Check `~/aether/knowledge/aethervault/` for `.md` files.

### ⚪ Obsidian Integration
- **Issue:** Notes don't appear in Obsidian.
- **Solution:** Ensure your Obsidian vault path is pointed directly to `~/aether/knowledge/aethervault/`.

---

## ❓ FAQ

**Is my data private?**
100%. Aether Droid runs entirely on local hardware. Zero bytes leave your device unless you explicitly use a `web_search` tool.

**How do I update?**
Run `git pull` in the installation directory, then re-run `./install.sh`.

**Where are the logs?**
Check `~/.aether/sessions/` for engine and tool logs.
