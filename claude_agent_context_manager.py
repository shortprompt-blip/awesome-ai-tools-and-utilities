import argparse
import json
import re

def clean_tool_outputs(text: str) -> str:
    """Rimuove log estesi e risposte di tool superflue."""
    # Rimuove blocchi di log o risposte lunghe lasciando un placeholder
    text = re.sub(r'```(?:text|log|console)\n[\s\S]*?```', '[...Tool Output Omitted...]', text)
    return text

def truncate_context(history: list, max_step_memory: int = 2) -> list:
    if not history:
        return []
    
    # 1. Preserva sempre il prompt/task originario dell'utente
    system_task = history[0]
    
    # 2. Isola gli ultimi N passaggi dell'agente (memoria a breve termine)
    recent_history = history[-max_step_memory:]
    
    # 3. Dai passaggi intermedi estrae solo gli artifact chiave
    artifacts = []
    for turn in history[1:-max_step_memory]:
        if turn.get("role") == "assistant" and "artifact" in turn:
            artifacts.append(f"- Artifact generated: {turn['artifact']}")
            
    state_summary = {
        "role": "system",
        "content": f"### ACCUMULATED CONTEXT STATE\n" + "\n".join(artifacts if artifacts else ["No artifacts stored."])
    }
    
    # Pulisce i passaggi recenti da verbosità eccessive
    cleaned_recent = []
    for msg in recent_history:
        cleaned_msg = msg.copy()
        cleaned_msg["content"] = clean_tool_outputs(msg.get("content", ""))
        cleaned_recent.append(cleaned_msg)
        
    return [system_task, state_summary] + cleaned_recent

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Multi-Step Agent Context Truncator")
    parser.add_argument("--history", required=True, help="Path al file JSON con la cronologia")
    args = parser.parse_args()
    
    with open(args.history, "r", encoding="utf-8") as f:
        raw_history = json.load(f)
        
    compacted = truncate_context(raw_history)
    print(json.dumps(compacted, indent=2))
  
