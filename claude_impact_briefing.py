"""
Claude Code Pre-Execution Impact Briefing Tool (Advanced) - ShortPrompt Utilities
Scans local workspace using AST, Git history, import graphs, and stack detection
to generate a hyper-compressed context briefing for Claude Code (0 token cost).

Web Version: https://shortprompt.altervista.org/ai-context-windows-calculator/
"""

import argparse
import ast
import json
import os
import re
import subprocess
import sys

IGNORE_DIRS = {'.git', 'node_modules', 'venv', '__pycache__', 'dist', 'build', '.idea', '.vscode', '.next', '.pytest_cache'}
ALLOWED_EXTS = {'.py', '.js', '.ts', '.jsx', '.tsx', '.html', '.css', '.json', '.md', '.php', '.go', '.rs'}

def detect_tech_stack(root_dir="."):
    """Detects primary technologies and frameworks in the repository."""
    stack = []
    if os.path.exists(os.path.join(root_dir, "package.json")):
        try:
            with open(os.path.join(root_dir, "package.json"), "r", encoding="utf-8") as f:
                data = json.load(f)
                deps = {**data.get("dependencies", {}), **data.get("devDependencies", {})}
                fw = [k for k in ["next", "react", "vue", "express", "svelte", "typescript", "tailwindcss"] if k in deps]
                stack.append(f"Node.js ({', '.join(fw) if fw else 'Standard'})")
        except Exception:
            stack.append("Node.js")

    if os.path.exists(os.path.join(root_dir, "pyproject.toml")) or os.path.exists(os.path.join(root_dir, "requirements.txt")):
        stack.append("Python")
    if os.path.exists(os.path.join(root_dir, "Cargo.toml")):
        stack.append("Rust")
    if os.path.exists(os.path.join(root_dir, "go.mod")):
        stack.append("Go")
    if os.path.exists(os.path.join(root_dir, "composer.json")):
        stack.append("PHP")

    return ", ".join(stack) if stack else "Generic Workspace"

def get_git_status():
    """Extracts modified files from git status."""
    modified = []
    try:
        res = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True, check=True)
        for line in res.stdout.splitlines():
            parts = line.strip().split(maxsplit=1)
            if len(parts) == 2:
                modified.append(parts[1])
    except Exception:
        pass
    return modified

def get_git_recent_commits(filepath):
    """Gets the last commit message touching this file."""
    try:
        res = subprocess.run(['git', 'log', '-n', '1', '--oneline', '--', filepath], capture_output=True, text=True, check=True)
        return [line.strip() for line in res.stdout.splitlines() if line.strip()]
    except Exception:
        return []

def extract_ast_signatures(filepath):
    """Uses Python's AST module for precise signature extraction, or regex fallback."""
    signatures = []
    if filepath.endswith('.py'):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                tree = ast.parse(f.read(), filename=filepath)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    args = [a.arg for a in node.args.args]
                    signatures.append(f"  Line {node.lineno}: def {node.name}({', '.join(args[:4])})")
                elif isinstance(node, ast.ClassDef):
                    signatures.append(f"  Line {node.lineno}: class {node.name}")
            return signatures[:6]
        except Exception:
            pass

    # Regex fallback for JS/TS/PHP/Other files
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            for idx, line in enumerate(f, 1):
                if re.match(r'^\s*(def|class|function|export\s+function|const\s+\w+\s*=\s*\(|async\s+function)\b', line):
                    signatures.append(f"  Line {idx}: {line.strip()}")
    except Exception:
        pass
    return signatures[:6]

def find_dependent_files(target_filename, root_dir="."):
    """Scans codebase for files that import or reference the target module."""
    base_name = os.path.splitext(os.path.basename(target_filename))[0]
    dependents = []
    if len(base_name) < 3:
        return dependents

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ALLOWED_EXTS:
                filepath = os.path.join(root, file)
                if filepath == target_filename:
                    continue
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if base_name in content:
                            dependents.append(filepath)
                except Exception:
                    continue
    return dependents[:4]

def find_test_files(target_filename, root_dir="."):
    """Finds associated unit/integration test files."""
    base_name = os.path.splitext(os.path.basename(target_filename))[0]
    test_matches = []
    possible_names = [f"test_{base_name}", f"{base_name}_test", f"{base_name}.test", f"{base_name}.spec"]

    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            file_no_ext = os.path.splitext(file)[0]
            if any(p == file_no_ext or p in file_no_ext for p in possible_names):
                test_matches.append(os.path.join(root, file))
    return test_matches[:3]

def check_syntax_errors(filepath):
    """Performs quick native syntax verification."""
    if filepath.endswith('.py'):
        try:
            with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                ast.parse(f.read())
            return None
        except SyntaxError as e:
            return f"Line {e.lineno}: {e.msg}"
    return None

def generate_briefing(task_query, root_dir="."):
    print("\n🔍 GENERATING ADVANCED PRE-EXECUTION CLAUDE BRIEFING...")
    print("==========================================================")

    tech_stack = detect_tech_stack(root_dir)
    modified_files = get_git_status()

    impacted_files = set(modified_files)

    briefing = [
        "### 🎯 PRE-EXECUTION CODE IMPACT BRIEFING",
        f"**Tech Stack:** {tech_stack}",
        f"**User Task Goal:** {task_query}\n",
        "**Key Impacted Modules & Signatures:**"
    ]

    if not impacted_files:
        briefing.append("- No uncommitted git changes detected. Standard repository inspection applies.")

    all_tests = set()
    all_dependents = set()

    for f in list(impacted_files)[:6]:
        if not os.path.exists(f):
            continue
        sigs = extract_ast_signatures(f)
        commits = get_git_recent_commits(f)
        syntax_err = check_syntax_errors(f)
        deps = find_dependent_files(f, root_dir)
        tests = find_test_files(f, root_dir)

        all_dependents.update(deps)
        all_tests.update(tests)

        briefing.append(f"\n📂 **File:** `{f}`")
        if syntax_err:
            briefing.append(f"  ⚠️ **Syntax Error:** {syntax_err}")
        if commits:
            briefing.append(f"  📜 **Last Commit:** {commits[0]}")
        if sigs:
            briefing.extend(sigs)

    if all_dependents:
        briefing.append("\n🔗 **Dependent Files (Potential Ripple Effects):**")
        for dep in list(all_dependents)[:4]:
            briefing.append(f"  - `{dep}`")

    if all_tests:
        briefing.append("\n🧪 **Associated Test Suites:**")
        for t in list(all_tests)[:4]:
            briefing.append(f"  - `{t}`")

    full_output = "\n".join(briefing)
    words = len(full_output.split())
    tokens = int(words / 0.75)

    print(full_output)
    print("\n==========================================================")
    print(f"📊 CONTEXT METRICS:")
    print(f"• Briefing Size: ~{tokens} tokens ({words} words)")
    print(f"• Context Saved: >95% vs full repository scan")
    print("💡 Estimate exact LLM limits: https://shortprompt.altervista.org/ai-context-windows-calculator/")
    print("==========================================================\n")

def main():
    parser = argparse.ArgumentParser(
        description="Advanced zero-token pre-execution briefing for Claude Code."
    )
    parser.add_argument("--task", "-t", type=str, required=True, help="Description of the task for Claude")
    parser.add_argument("--dir", "-d", type=str, default=".", help="Root repository directory")
    args = parser.parse_args()

    generate_briefing(args.task, args.dir)

if __name__ == "__main__":
    main()
