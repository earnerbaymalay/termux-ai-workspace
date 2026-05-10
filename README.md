<div align="center">

# 🌌 A E T H E R — D R O I D
### *Sovereign AI Workstation for Android.*

[![Version](https://img.shields.io/badge/version-26.05.1-50fa7b?style=for-the-badge)](VERSIONS.md)
[![License](https://img.shields.io/badge/license-MIT-f1fa8c?style=for-the-badge)](LICENSE)
[![Privacy](https://img.shields.io/badge/privacy-100%25_local-bd93f9?style=for-the-badge)](#privacy)

**[📲 Download](https://github.com/earnerbaymalay/aether-droid/releases)** · **[🌐 Sideload Hub](https://earnerbaymalay.github.io/sideload/)** · **[📖 Usage Guide](USAGE.md)** · **[🔧 Troubleshooting](TROUBLESHOOTING.md)**

</div>

---

![Aether Droid](docs/media/hero.svg)

## 🏗️ Architecture

```text
[ User Interface (gum/figlet) ]
           │
[ Neural Operating Interface (aether.sh) ]
     ┌─────┴─────┬─────────────┐
[ Models ]  [ Toolbox ]  [ AetherVault ]
 (GGUF)      (Shell)      (Markdown)
```

## What is Aether Droid?

**Aether Droid is a fully offline, high-autonomy AI workstation for Android.** It leverages the power of Termux to run specialized LLMs locally, providing a persistent "neural companion" that can write code, analyze your system, manage files, and learn from your specific workflows.

---

## 🚀 Quick Start

### Install on Android

**Prerequisites:** 
- Android 12+
- [Termux](https://f-droid.org/en/packages/com.termux/) (from F-Droid). 
- **Hardware:** 8GB+ RAM highly recommended for optimal 8B model performance.

```bash
git clone https://github.com/earnerbaymalay/aether-droid.git
cd aether-droid
chmod +x ./install.sh
./install.sh   # Guided installer (~10 min)
ai             # Launch the interface
```

---

## 🧠 Neural Pathways (AI Tiers)

Aether Droid uses an **Orchestrator** to route tasks between specialized models:

| Tier | Model | Best For |
| :--- | :--- | :--- |
| ⚡ **TURBO** | Llama-3.2-3B | Rapid responses, summarization |
| 🤖 **AGENT** | Hermes-3-8B | Agentic operations, tool use, memory |
| 💻 **CODE** | Qwen-Coder-7B | Development, logic, code review |
| 🧠 **LOGIC** | DeepSeek-R1-8B | Planning, complex reasoning, "System 2" thinking |

---

## 🛠️ Key Features

- **Integrated Toolbox:** Over 17 system-level tools for battery management, file ops, and network analysis.
- **AetherVault:** Persistent Markdown-based knowledge base that evolves through **Neural Distillation**.
- **Ralph Loop:** A recursive agentic loop allowing Aether to perform multi-step autonomous tasks without user intervention.
- **Swarm Logic:** Distributed planning where one model designs and another implements.

---

## 🔒 Privacy & Sovereignty

- **Air-Gapped by Design:** No cloud APIs, no telemetry, no tracking.
- **Data Ownership:** All logs, memories, and configurations are stored in plain text (Markdown/JSON) on your device.
- **No Gatekeepers:** No accounts or subscriptions required.

---

[MIT License](LICENSE)
