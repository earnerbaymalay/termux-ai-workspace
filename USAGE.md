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

Aether isn't just a chatbot; it's an operator. The **AGENT** pathway can autonomously use the following tools to fulfill your requests.

### 🤖 Agentic Tool Protocol
The AI triggers tools using a specific XML-style syntax: `<tool>name(args)</tool>`. While the Agent does this automatically, you can explicitly ask it to use a tool.

### 📚 Core Tool Reference & Examples

| Tool | Purpose | Example Command |
| :--- | :--- | :--- |
| **`learn`** | Persists facts to AetherVault. | "Learn this: coffee_pref | I like dark roast with no sugar." |
| **`web_search`** | Real-time web search (DuckDuckGo). | "Search the web for the latest SpaceX launch status." |
| **`web_read`** | Scrapes clean text from a URL. | "Read this article: https://example.com/news and summarize it." |
| **`system_monitor`**| Checks CPU, RAM, and Disk health. | "Check my system resources and tell me if I'm low on RAM." |
| **`list_files`** | Native directory exploration. | "List the files in my aether/scripts folder." |
| **`gh_status`** | Checks Git/GitHub repository state. | "Check the git status of this project." |
| **`obsidian_notes`**| Interfaces with your Obsidian vault. | "Search my Obsidian notes for 'Project Phoenix'." |
| **`token_optimizer`**| Compresses context for long chats. | "Run the token optimizer on my last session to save space." |

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
