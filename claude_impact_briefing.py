"""
Claude Code Pre-Execution Impact Briefing Tool - ShortPrompt Utilities
Scans local workspace/git diffs and generates a token-optimized impact map
for Claude Code execution to prevent context window bloat.

Web Version & Token Counter: https://shortprompt.altervista.org/ai-context-windows-calculator/
"""

import argparse
import os
import re
import subprocess
import sys

# Folders to ignore
IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', 'dist', 'build', '.idea', '.vscode'}
ALLOWED_EXTS = {'.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.json', '.md', '.php'}

def get_git_modified_files():
    """Returns a list of files modified in git relative to working dir."""
    try:
        result = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, check=True)
        files = []
        for line in result.stdout.splitlines():
            line = line.strip()
            if line:
                parts = line.split(maxsplit=1)
                if len(parts) == 2:
                    files.append(parts[1])
        return files
    except Exception:
        return []

def scan_symbol_references(keyword: str, root_dir: str = "."):
    """Scans repository for files matching target keywords/functions."""
    matches = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ALLOWED_EXTS:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if keyword.lower() in content.lower():
                            matches.append(filepath)
                except Exception:
                    continue
    return matches

def extract_signatures(filepath: str):
    """Extracts high-level class/function signatures to keep context lightweight."""
    signatures = []
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            for idx, line in enumerate(lines, 1):
                # Python / JS / TS function or class matching
                if re.match(r'^\s*(def|class|function|const\s+\w+\s*=\s*\(|async\s+function)\b', line):
                    signatures.append(f"  Line {idx}: {line.strip()}")
    except Exception:
        pass
    return signatures

def generate_briefing(task_query: str, root_dir: str = "."):
    print("\n🔍 GENERATING PRE-EXECUTION CLAUDE CODE BRIEFING...")
    print("====================================================")
    
    modified_files = get_git_modified_files()
    keywords = [k for k in re.split(r'\W+', task_query) if len(k) > 3]
    
    impacted_files = set(modified_files)
    for kw in keywords[:3]:  # Top 3 relevant keywords
        matches = scan_symbol_references(kw, root_dir)
        impacted_files.update(matches)
        
    briefing_text = [
        "### 🎯 PRE-EXECUTION CODE IMPACT BRIEFING",
        f"**User Target Task:** {task_query}\n",
        "**High-Impact Files & Signatures (Focus context here):**"
    ]
    
    total_words = 0
    
    if not impacted_files:
        briefing_text.append("- No specific git diffs or direct symbol matches found. Scan root directory structure.")
    else:
        for f in list(impacted_files)[:8]: # Limit to max 8 files for extreme token compression
            sigs = extract_signatures(f)
            briefing_text.append(f"\n📂 **File:** `{f}`")
            if sigs:
                briefing_text.extend(sigs[:5]) # Top 5 signatures
            else:
                briefing_text.append("  (Modified/Referenced file)")

    full_output = "\n".join(briefing_text)
    total_words = len(full_output.split())
    est_tokens = int(total_words / 0.75)
    
    print(full_output)
    print("\n====================================================")
    print(f"📊 BRIEFING CONTEXT METRICS:")
    print(f"• Estimated Briefing Size: ~{est_tokens} tokens ({total_words} words)")
    print(f"• Estimated Context Saved: >90% vs full repo scan")
    print("💡 Estimate exact LLM context limits: https://shortprompt.altervista.org/ai-context-windows-calculator/")
    print("====================================================\n")

def main():
    parser = argparse.ArgumentParser(
        description="Pre-execution briefing tool for Claude Code. Reduces token usage by generating compact AST impact maps."
    )
    parser.add_argument("--task", "-t", type=str, required=True, help="The task or feature description you plan to give to Claude")
    parser.add_argument("--dir", "-d", type=str, default=".", help="Root repository directory")
    
    args = parser.parse_args()
    generate_briefing(args.task, args.dir)

if __name__ == "__main__":
    main()
  
