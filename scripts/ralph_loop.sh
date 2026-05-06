#!/usr/bin/env bash
# ralph_loop.sh — Iterative Agentic Loop for Aether (Termux Edition)
# Inspired by the Ralph technique.

DIR="$HOME/aether"
MODELS="$DIR/models"
BIN="$HOME/llama.cpp/build/bin/llama-cli"
SESSION_DIR="$HOME/.aether/sessions"

# Load settings
THREADS=$(python3 -c "import json; print(json.load(open('$DIR/settings/config.json')).get('model',{}).get('threads',6))" 2>/dev/null || echo 6)

# UI Colors (matching aether.sh)
ACCENT="#00ff9d"

clear
echo -e "\033[1;34m"
figlet -f small "   RALPH"
echo -e "\033[0;34m   ITERATIVE AGENTIC LOOP // V 1.0\033[0m\n"

TASK=$(gum input --placeholder "Enter your goal for the Ralph Loop...")
[ -z "$TASK" ] && exit 0

MAX_ITER=$(gum input --placeholder "Max iterations (default 5)..." --value "5")
ITER=1

while [ $ITER -le $MAX_ITER ]; do
    echo -e "\n\033[1;36m[Iteration $ITER/$MAX_ITER]\033[0m"
    
    # Check for model (defaulting to Agent model)
    MOD="hermes-3-8b.gguf"
    if [ ! -f "$MODELS/$MOD" ]; then
        echo "Missing model: $MOD. Please download via main menu."
        exit 1
    fi
    
    # SYSTEM PROMPT
    SYS_P="You are Aether in Ralph Loop mode. Task: $TASK. You must work towards completion. Output TOOL results if needed. If the task is finished, output 'TASK_COMPLETE'."
    
    echo -ne "\033[1;32m AI (Ralph): \033[0m"
    
    # Run inference and capture output
    # We use -n 512 to keep it snappy
    OUTPUT=$("$BIN" -m "$MODELS/$MOD" -p "System: $SYS_P\nUser: Continue working on the task." -n 512 -t "$THREADS" --no-display-prompt 2>/dev/null)
    
    echo "$OUTPUT"
    
    if [[ "$OUTPUT" == *"TASK_COMPLETE"* ]]; then
        gum style --foreground "#50fa7b" "[✔] Task achieved in $ITER iterations."
        break
    fi
    
    # Very basic tool execution check (could be expanded)
    if [[ "$OUTPUT" == *"TOOL:"* ]]; then
        gum style --foreground "#f1fa8c" "Tool call detected. (Automated tool execution pending integration)"
    fi
    
    ((ITER++))
    sleep 2
done

read -p "Loop finished. Press Enter to return..."
