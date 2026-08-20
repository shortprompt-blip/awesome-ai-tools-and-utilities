# 🤖 Claude Code Instructions & ShortPrompt Integration

When working in this repository or interacting with ShortPrompt developer tools, follow these instructions to minimize context window consumption and maximize efficiency.

## ⚡ Pre-Task Execution Protocol
Before starting complex multi-file refactoring or feature implementation, run the local impact briefing script to generate a compressed AST map:

```bash
python claude_impact_briefing.py --task "YOUR_FEATURE_OR_BUG_DESCRIPTION"
```
---
## ✂️ ShortPrompt Skill (`/shortprompt`)
When asked to optimize, shorten, or minify a prompt, run the local ShortPrompt engine:

```bash
python shortprompt.py --prompt "YOUR_VERBOSE_PROMPT_HERE"
```
Use this skill whenever user prompts exceed 200 words to ensure maximum output accuracy and context efficiency.

---

# 🤖 CLAUDE.md - ShortPrompt Developer Workspace Instructions

This workspace is optimized for zero-token local execution and context-efficient AI engineering. Always prioritize running local Python scripts over scanning entire directories.

---

## ⚙️ Core Protocol & Token Guidelines
- **Zero-Token First**: Before analyzing large codebases, run `claude_impact_briefing.py` to get an AST & Git diff briefing.
- **Offload Repetitive Tasks**: Delegate mock generation, TypeScript interface stubs, and unit test boilerplate to the local LLM via `shortprompt_local.py`.
- **No Fluff**: Keep responses concise, structured, and code-centric.

---

## 🛠️ Available Local Skills & Commands

### 1. Pre-Execution Impact Briefing (`/briefing`)
Scans AST signatures, Git diffs, and import graphs to build a high-density summary before executing complex tasks.
```bash
python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"
```

### 2. ShortPrompt Engine (`/shortprompt`)
Compresses verbose prompt instructions into dense, deterministic directives.
```bash
python shortprompt.py --prompt "VERBOSE_PROMPT_TEXT"
```

### 3. Local Semantic Code Search (`/local-search`)
Uses the local Ollama instance to locate functions or logic semantically across candidate files without reading entire folders.
```bash
python shortprompt_local.py --search "QUERY_TO_LOCATE"
```

### 4. Task Offloading to Local LLM (`/delegate`)
Offloads simple generation tasks (mocks, boilerplate, schemas) to the local model at $0 cost.
```bash
python shortprompt_local.py --delegate "TASK_DESCRIPTION" --file "PATH_TO_CONTEXT_FILE"
```

---

## 🚀 Local Model Environment (Ollama / Docker)
- **Local Host**: `http://localhost:11434`
- **Default Model**: `qwen2.5-coder:1.5b`
- **Docker Command**:
  ```bash
  docker run -d --name shortprompt-ollama -v ollama_data:/root/.ollama -p 11434:11434 ollama/ollama
  docker exec -it shortprompt-ollama ollama pull qwen2.5-coder:1.5b
  ```
