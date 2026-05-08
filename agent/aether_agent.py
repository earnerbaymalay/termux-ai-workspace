#!/usr/bin/env python3
"""
🌌 Aether-AI Neural Agent Core // V 26.04.2 (Windows Edition)
High-performance Python agent utilizing Ollama for Windows.
"""

import os, sys, json, re, subprocess, signal, time, requests
from pathlib import Path
from datetime import datetime

# --- Constants & Configuration ---
DIR = Path.home() / "aether"
MODELS_DIR = DIR / "models"
TOOLBOX_DIR = DIR / "toolbox"
KNOWLEDGE_DIR = DIR / "knowledge"
CONTEXT7_DIR = KNOWLEDGE_DIR / "aethervault"
SESSION_DIR = Path.home() / ".aether" / "sessions"
OLLAMA_API_URL = "http://127.0.0.1:11434/api/generate"

# Add knowledge loader to path if exists
sys.path.insert(0, str(KNOWLEDGE_DIR))
try:
    from knowledge_loader import AetherVault
    HAS_VAULT_LOADER = True
except ImportError:
    HAS_VAULT_LOADER = False

# Colors (ANSI)
C_AI = "\033[38;5;39m"
C_USR = "\033[38;5;153m"
C_TOOL = "\033[38;5;82m"
C_ERR = "\033[38;5;196m"
C_DIM = "\033[2m"
C_BOLD = "\033[1m"
C_RST = "\033[0m"

# --- Tool Engine ---
def load_manifest():
    manifest_path = TOOLBOX_DIR / "manifest.json"
    if not manifest_path.exists():
        return {"tools": []}
    with open(manifest_path) as f:
        return json.load(f)

def run_tool(name, args=""):
    if name == "learn":
        try:
            if "|" not in args: return "Error: Format is 'filename|content'"
            filename, content = args.split("|", 1)
            
            # Try AetherVault smart storage first
            if HAS_VAULT_LOADER:
                try:
                    vault = AetherVault()
                    safe_name = filename.strip().replace(" ", "_").lower()
                    path = vault.add_entry(safe_name, content.strip(), category="memory")
                    return f"Successfully learned: {safe_name} in AetherVault ({path})."
                except:
                    pass
            
            # Fallback
            filepath = CONTEXT7_DIR / "memories" / f"{filename.strip()}.md"
            filepath.parent.mkdir(parents=True, exist_ok=True)
            filepath.write_text(content.strip())
            return f"Successfully learned: {filename} in AetherVault."
        except Exception as e:
            return f"Learning Error: {str(e)}"

    manifest = load_manifest()
    tool = next((t for t in manifest["tools"] if t["name"] == name), None)
    if not tool: return f"Error: Tool '{name}' not found."
    
    script_path = TOOLBOX_DIR / tool["script"]
    if not script_path.exists(): return f"Error: Tool script missing."

    print(f"\n{C_DIM}[Executing: {name}]{C_RST}")
    try:
        if script_path.suffix == ".ps1":
            cmd = ["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-File", str(script_path)] + ([args] if args else [])
        else:
            cmd = ["bash", str(script_path)] + ([args] if args else [])
            
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=20)
        return result.stdout.strip() if result.returncode == 0 else f"Tool Error: {result.stderr.strip()}"
    except Exception as e:
        return f"Execution Error: {str(e)}"

# --- Inference Engine ---
def load_skill_content(skill_name):
    skill_path = DIR / "skills" / skill_name / "SKILL.md"
    if skill_path.exists():
        try:
            return skill_path.read_text()[:2000]
        except:
            return f"[Skill: {skill_name} - content unreadable]"
    return f"[Skill: {skill_name} - not found]"

def build_system_prompt(query=""):
    manifest = load_manifest()
    tool_list = "\n".join([f"- **{t['name']}**: {t['description']}" for t in manifest["tools"]])
    tool_list += "\n- **learn**: Save new insights to AetherVault (format: filename|content)"

    skills_dir = DIR / "skills"
    skill_content = ""
    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                content = load_skill_content(skill_dir.name)
                skill_content += f"\n## Skill: {skill_dir.name}\n{content}\n"

    # AetherVault integration
    vault_knowledge = ""
    if HAS_VAULT_LOADER:
        try:
            vault = AetherVault()
            vault_knowledge = vault.load_for_query(query or "", 4000)
        except:
            pass

    return f"""You are AetherAI, a local-first neural interface running on Windows.
Your computer. Your AI. Your rules. No cloud. No tracking. No limits.
Current Date: {datetime.now().strftime('%A, %d %B %Y')}

## AetherVault Knowledge
{vault_knowledge}

## Skills (Full Instructions)
{skill_content}

## Tool Protocol
Execute tools via: <tool>name(args)</tool>

Available tools:
{tool_list}

Rules:
1. Be technical and concise. No conversational filler, no AI-isms.
2. Use tools immediately if they help answer the query.
3. Read and follow skill instructions from the Skills section above.
4. If you discover something valuable, use <tool>learn(filename|content)</tool> to save it to AetherVault.
5. NEVER mention being an AI, language model, or assistant.
"""

def generate_completion(prompt, model="llama3.1:8b", stream=True):
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": stream,
        "options": {
            "temperature": 0.7,
            "stop": ["User:", "System:", "AI:", "\n\n\n"]
        }
    }
    
    try:
        r = requests.post(OLLAMA_API_URL, json=payload, stream=stream, timeout=120)
        full_text = ""
        if stream:
            for line in r.iter_lines():
                if line:
                    chunk = json.loads(line.decode("utf-8"))
                    content = chunk.get("response", "")
                    sys.stdout.write(content)
                    sys.stdout.flush()
                    full_text += content
                    if chunk.get("done"): break
        else:
            full_text = r.json().get("response", "").strip()
        return full_text.strip()
    except Exception as e:
        return f"Ollama Inference Error: {str(e)}"

# --- Main Logic ---
def chat_loop(model_name="llama3.1:8b"):
    history = []
    print(f"\n{C_BOLD}{C_AI}\uD83C\uDF0C AETHER-AI OPERATOR {C_RST}{C_DIM}// V 26.04.2 (WINDOWS){C_RST}")
    print(f"  Engine: Ollama | Model: {model_name}")
    print(f"  Type 'exit' or 'tools' | ^C to save & quit\n")

    while True:
        try:
            user_input = input(f"{C_BOLD}{C_USR}You:{C_RST} ").strip()
            if not user_input: continue
            if user_input.lower() in ["exit", "quit"]: break
            
            if user_input.lower() == "tools":
                manifest = load_manifest()
                print(f"  {C_TOOL}\u2713 learn(file|data){C_RST} Store insights")
                for t in manifest["tools"]:
                    print(f"  {C_TOOL}\u2713 {t['name']:15s}{C_RST} {t['description']}")
                continue

            system_prompt = build_system_prompt(query=user_input)
            
            full_prompt = f"System: {system_prompt}\n"
            for msg in history[-8:]:
                role = "User" if msg["role"] == "user" else "AI"
                full_prompt += f"{role}: {msg['content']}\n"
            full_prompt += f"User: {user_input}\nAI: "

            print(f"{C_BOLD}{C_AI}AI:{C_RST} ", end="", flush=True)
            response = generate_completion(full_prompt, model=model_name)
            print()

            tool_match = re.search(r"<tool>(\w+)\((.*)\)</tool>", response)
            if tool_match:
                name, args = tool_match.groups()
                output = run_tool(name, args)
                print(f"{C_DIM}[Result: {output[:100]}...]{C_RST}")
                
                tool_prompt = full_prompt + response + f"\nUser: [TOOL_RESULT] {output}\nAI: "
                print(f"{C_BOLD}{C_AI}AI (Analysis):{C_RST} ", end="", flush=True)
                follow_up = generate_completion(tool_prompt, model=model_name)
                print()
                response += f"\n[Tool Result: {output}]\n{follow_up}"

            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": response})

            # Auto-Memory Extraction (Background)
            import threading
            threading.Thread(target=auto_extract_memory, args=(user_input, response, model_name)).start()

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n{C_ERR}[Critical Error: {e}]{C_RST}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="llama3.1:8b")
    args = parser.parse_args()
    chat_loop(args.model)
True)
                follow_up = generate_completion(tool_prompt, model=model_name)
                print()
                response += f"\n[Tool Result: {output}]\n{follow_up}"

            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": response})

        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"\n{C_ERR}[Critical Error: {e}]{C_RST}")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="llama3.1:8b")
    args = parser.parse_args()
    chat_loop(args.model)
