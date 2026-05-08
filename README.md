<div align="center">

# 🌌 A E T H E R
### *Offline AI Workstation for Android.*

[![Version](https://img.shields.io/badge/version-26.04.2-50fa7b?style=for-the-badge)](VERSIONS.md)
[![License](https://img.shields.io/badge/license-MIT-f1fa8c?style=for-the-badge)](LICENSE)
[![Privacy](https://img.shields.io/badge/privacy-100%25_local-bd93f9?style=for-the-badge)](#privacy)

**[📲 Download](https://github.com/earnerbaymalay/aether/releases)** · **[🌐 Sideload Hub](https://earnerbaymalay.github.io/sideload/)** · **[📖 Usage Guide](USAGE.md)** · **[🔧 Troubleshooting](TROUBLESHOOTING.md)**

</div>

---

![Aether](docs/media/hero.svg)

## 🏗️ Architecture

```text
[ User Interface (gum/figlet) ]
           │
[ Neural Operating Interface (aether.sh) ]
     ┌─────┴─────┬─────────────┐
[ Models ]  [ Toolbox ]  [ AetherVault ]
 (GGUF)      (Shell)      (Markdown)
```

## What is Aether?

**Aether runs 4 AI models entirely on your phone.** It routes tasks between specialized models, executes shell operations, and maintains a persistent knowledge base. Zero bytes leave your device.

---

## Quick Start

### Install on Android

**Prerequisites:** Android + [Termux](https://f-droid.org/en/packages/com.termux/) (from F-Droid). 6GB+ RAM recommended.

```bash
git clone https://github.com/earnerbaymalay/aether.git
cd aether
./install.sh   # guided installer (~10 min first time)
ai             # launch
```

### All Platforms

<div align="center">

| Platform | Repo | Version |
|----------|------|---------|
| 📱 **Android (Termux)** | [aether](https://github.com/earnerbaymalay/aether) | 26.04.2 |
| 🖥️ **macOS / Desktop** | [aether-desktop](https://github.com/earnerbaymalay/aether-desktop) | 26.04.2 |
| 🍎 **Apple (iOS/iPad)** | [aether-apple](https://github.com/earnerbaymalay/aether-apple) | 26.04.2 |

</div>

---

## AI Tiers (Neural Pathways)

| Tier | Model | Best For |
| :--- | :--- | :--- |
| ⚡ **TURBO** | Llama-3.2-3B | Fast questions, summaries |
| 🤖 **AGENT** | Hermes-3-8B | Tool use, complex tasks, memory |
| 💻 **CODE** | Qwen-Coder-3B | Code generation, review, logic |
| 🧠 **LOGIC** | DeepSeek-R1 | Reasoning, planning, "thinking" |

---

## Key Features

- **Toolbox (17 tools):** Battery, web search, file ops, system health, log analysis.
- **Skills (11+ modules):** Code review, security audit, architecture design.
- **AetherVault:** Persistent Markdown knowledge base that grows every session via **Auto-Memory**.
- **Swarm Orchestrator:** Logic plans → Code implements → Agent analyzes.
- **Ralph Loop:** Iterative agentic loop for autonomous multi-turn tasks.

---

## Privacy

- **Zero bytes leave device** — No cloud, no APIs, no tracking.
- **No accounts** — No registration, no telemetry, no phone-home.
- **Persistent memory** — AetherVault stores knowledge as Markdown files on your device.

---

[MIT License](LICENSE)
