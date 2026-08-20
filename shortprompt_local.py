"""
ShortPrompt Local Engine - Search & Task Offloader
Connects local LLMs (Ollama) with Claude Code workflows to offload simple tasks and query codebase semantically at $0 cost.

Web Tool: https://shortprompt.altervista.org/
"""

import argparse
import json
import os
import subprocess
import sys
import urllib.request
import urllib.error

OLLAMA_HOST = os.environ.get("OLLAMA_HOST", "http://localhost:11434")
DEFAULT_MODEL = "qwen2.5-coder:1.5b"
IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', 'dist', 'build', '.next'}
ALLOWED_EXTS = {'.py', '.js', '.ts', '.jsx', '.tsx', '.json', '.go', '.rs', '.php', '.html'}

def check_ollama_status() -> bool:
    """Verifies if the local Ollama instance is accessible."""
    try:
        req = urllib.request.Request(f"{OLLAMA_HOST}/api/tags")
        with urllib.request.urlopen(req, timeout=3) as resp:
            return resp.status == 200
    except Exception:
        return False

def query_local_llm(prompt: str, model: str = DEFAULT_MODEL, system_prompt: str = "") -> str:
    """Sends prompt payload to local Ollama API."""
    if not check_ollama_status():
        print("⚠️ Local Ollama instance not detected at localhost:11434.")
        print("👉 Run: docker run -d -p 11434:11434 --name shortprompt-ollama ollama/ollama")
        print("👉 Then: docker exec -it shortprompt-ollama ollama pull qwen2.5-coder:1.5b")
        sys.exit(1)

    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    if system_prompt:
        payload["system"] = system_prompt

    try:
        req = urllib.request.Request(
            f"{OLLAMA_HOST}/api/generate",
            data=json.dumps(payload).encode('utf-8'),
            headers={'Content-Type': 'application/json'}
        )
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data.get("response", "").strip()
    except Exception as e:
        return f"Error executing local LLM query: {e}"

def local_semantic_search(query: str, root_dir: str = ".") -> str:
    """Extracts candidate files and uses local LLM to return exact matching code snippets."""
    code_samples = []
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            if os.path.splitext(file)[1].lower() in ALLOWED_EXTS:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()[:120]  # Read first 120 lines per file
                        content = "".join(lines)
                        if len(content.strip()) > 0:
                            code_samples.append(f"--- File: {filepath} ---\n{content}")
                except Exception:
                    continue

    if not code_samples:
        return "No relevant source files found."

    combined_context = "\n\n".join(code_samples[:8])  # Send candidate chunk
    prompt = f"Target Query: '{query}'\n\nCodebase Samples:\n{combined_context}\n\nTask: Identify and extract ONLY the exact function names, line references, or code blocks that fulfill the query. Be extremely concise."
    system_prompt = "You are a local semantic code searcher. Output only file paths and direct relevant snippets."
    
    return query_local_llm(prompt, system_prompt=system_prompt)

def delegate_task(task_description: str, context_file: str = None) -> str:
    """Offloads repetitive coding tasks (mocks, boilerplate, types) to local LLM."""
    extra_context = ""
    if context_file and os.path.exists(context_file):
        with open(context_file, 'r', encoding='utf-8', errors='ignore') as f:
            extra_context = f"\nInput File Context:\n{f.read()[:2000]}"

    prompt = f"Task: {task_description}\n{extra_context}\n\nGenerate clean, production-ready code with no conversational preambles."
    system_prompt = "You are a specialized code generator offloading simple tasks from primary AI models."
    
    return query_local_llm(prompt, system_prompt=system_prompt)

def main():
    parser = argparse.ArgumentParser(description="ShortPrompt Local LLM Engine for Search & Task Delegation.")
    parser.add_argument("--search", "-s", type=str, help="Search query to locate relevant code semantically")
    parser.add_argument("--delegate", "-d", type=str, help="Boilerplate task to offload to local LLM (e.g. 'generate mock JSON for user model')")
    parser.add_argument("--file", "-f", type=str, help="Optional context file for task delegation")
    parser.add_argument("--dir", type=str, default=".", help="Root directory for search")
    
    args = parser.parse_args()

    if args.search:
        print(f"🔍 Running local semantic search for: '{args.search}' (0 API tokens used)...")
        result = local_semantic_search(args.search, args.dir)
        print("\n--- LOCAL SEARCH RESULT ---")
        print(result)
        print("---------------------------")
        
    elif args.delegate:
        print(f"⚡ Offloading task to local LLM: '{args.delegate}'...")
        result = delegate_task(args.delegate, args.file)
        print("\n--- LOCAL GENERATED OUTPUT ---")
        print(result)
        print("------------------------------")
        
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
  
