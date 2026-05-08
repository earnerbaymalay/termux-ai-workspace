# 🌌 Aether — Usage Guide
### Version 26.04.2 (Standard Edition)

Welcome to the **Aether Neural Operating Interface**. This guide covers setup, basic operation, and advanced agentic workflows.

---

## 🚀 Quick Start (Android / Termux)

### 1. Requirements
- **Hardware:** Android device (last 5 years), 6GB+ RAM recommended.
- **Software:** [Termux](https://f-droid.org/en/packages/com.termux/) from F-Droid (Play Store version is NOT supported).
- **Storage:** 4GB+ free space for models.

### 2. Installation
```bash
git clone https://github.com/earnerbaymalay/aether.git
cd aether
./install.sh   # Follow the guided setup (~10 mins)
```

### 3. Launch
Launch from anywhere in Termux by typing:
```bash
ai
```

---

## 🧠 Neural Pathways (AI Tiers)

Aether routes your requests through specialized models based on your selection:

| Pathway | Model | Best For |
| :--- | :--- | :--- |
| ⚡ **TURBO** | Llama-3.2-3B | Speed, fast summaries, simple chat. |
| 🤖 **AGENT** | Hermes-3-8B | Complex tool-use, multi-turn tasks, planning. |
| 💻 **CODE** | Qwen-Coder-3B | Debugging, logic implementation, review. |
| 🧠 **LOGIC** | DeepSeek-R1 | Architectural design, deep reasoning, "thinking". |

---

## 🛠️ The Aether Toolbox (17 Tools)

Aether can interact with your device and the web. The **AGENT** pathway uses these automatically:
- **System:** `get_battery`, `get_date`, `system_monitor`, `disk_usage`.
- **Files:** `list_files`, `log_analyzer`, `backup_manager`.
- **Web:** `web_search` (DuckDuckGo), `web_read` (Markdown scraper).
- **Knowledge:** `obsidian_notes`, `learn` (saves to AetherVault).

**To audit your tools:** Select `TOOLS` from the main menu.

---

## 🗄️ AetherVault (Persistent Memory)

Your AI learns as you talk. Knowledge is stored as local Markdown files in `~/aether/knowledge/aethervault/`.

### 🧠 Auto-Memory
Aether now features background extraction. It silently identifies personal facts or preferences and saves them to your vault without interrupting the chat.

### ✍️ Manual Training
Tell the AI to remember something specific:
> "Learn this: python_tips | Always use type hints in production code."

---

## 👥 Advanced Workflows

### 🔄 Ralph Loop (Iterative Agent)
Located in the main menu. Set a goal, and Aether will iteratively work, self-correct, and use tools until the task is complete.

### 👥 Swarm Orchestrator
Execute complex project-level tasks where **LOGIC** plans, **AGENT** implements, and **CODE** verifies the output.
```bash
./scripts/swarm_orchestrator.sh run "Task description"
```

---

## 🎨 Personalization
Select **SETTINGS** in the main menu to:
- Change the UI accent color.
- Adjust model temperature and threads.
- Manage memory slots and session history.
