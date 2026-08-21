# 🤖 Claude Code Instructions

Instructions for working efficiently, effectively, and safely within the **awesome-ai-tools-and-utilities** developer repository.

---

## 🎯 Core Principles

- **Prioritize Local Tools:** Prefer repository-provided local tools when they offer useful analysis or automation.
- **Minimal & Reversible Changes:** Keep code modifications minimal, focused, and easily reversible.
- **Inspect Before Modifying:** Always review relevant files before making updates.
- **Preserve Behavior:** Maintain existing behavior unless a change is explicitly requested.
- **Zero Unnecessary Overhead:** Avoid adding unnecessary dependencies or altering unrelated files.
- **Concise & Implementation-Focused:** Keep responses clear, direct, and code-centric.

---

## 🔄 Development Workflow

### Simple Tasks
1. Inspect the target files.
2. Understand existing logic and context.
3. Make the smallest appropriate change.
4. Run relevant tests or validations.
5. Summarize changes concisely.

### Complex Multi-File Tasks
Run the repository impact briefing tool before making structural edits:
```bash
python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"
```

---

## 🛠️ Local Developer Tools

* **Agent Context Manager (`claude_agent_context_manager.py`):** Prunes multi-turn execution logs and strips raw tool outputs to preserve token budget in long sessions.
  ```bash
  python claude_agent_context_manager.py --history "PATH_TO_SESSION_HISTORY.json"
  ```

* **Impact Briefing (`claude_impact_briefing.py`):** Generates a compressed AST map for complex refactoring, multi-file edits, or unfamiliar repository areas.
  ```bash
  python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"
  ```

* **Benchmark Briefing (`benchmark_briefing.py`):** Executes local benchmarking and analysis on prompt tools and context performance.
  ```bash
  python benchmark_briefing.py
  ```

* **Prompt Compression (`shortprompt.py`):** Compresses and optimizes prompt payloads to lower LLM API token consumption.
  ```bash
  python shortprompt.py --prompt "PROMPT_TEXT"
  ```

* **Local Semantic Search (`shortprompt_local.py`):** Locates functions semantically or delegates low-risk generation tasks using local Ollama models.
  ```bash
  python shortprompt_local.py --search "QUERY"
  ```

* **Markdown Stripper (`markdown_stripper.py`):** Strips formatting tags from Markdown files to generate clean plain text payloads.
  ```bash
  python markdown_stripper.py --file "PATH_TO_FILE.md"
  ```

* **Token Calculator (`token_calculator.py`):** Estimates token counts and context window capacity for inputs local-side.
  ```bash
  python token_calculator.py --text "TEXT_OR_FILE_PATH"
  ```

---

## 🚀 Local LLM Environment (Ollama)

- **Default Endpoint:** `http://localhost:11434`
- **Default Model:** `qwen2.5-coder:1.5b`

### Docker Setup
```bash
docker run -d \
  --name shortprompt-ollama \
  -v ollama_data:/root/.ollama \
  -p 11434:11434 \
  ollama/ollama

docker exec -it shortprompt-ollama ollama pull qwen2.5-coder:1.5b
```

---

## 📐 Quality, Testing & Security Standards

### Code Quality Rules
- Follow existing project style conventions.
- Prefer simple, focused solutions over complex abstractions.
- Do not silently change public APIs or behavior.
- Check and handle new error failure paths properly.

### Testing & Validation
- Run relevant available unit tests and syntax/type checks.
- Review `git diff` to ensure no unintended modifications occurred.
- Report validation outcomes clearly.

### Git Safety & Privacy
- **Forbidden Actions:** Never rewrite history, force-push, delete branches, or overwrite files blindly.
- **Privacy:** Treat user prompts and source code as sensitive. Do not commit API keys or credentials.

---

## 📦 Repository Scope

This repository contains local LLM workflows, token/context utilities, Python CLI developer tools, and prompt engineering utilities.

When completing a task, summarize:
1. What changed.
2. Files modified.
3. Tests/validations performed.
4. Remaining limitations or assumptions.
