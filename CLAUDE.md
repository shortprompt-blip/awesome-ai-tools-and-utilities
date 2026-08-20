# 🤖 Claude Code Instructions

Instructions for working efficiently, effectively, and safely within the **ShortPrompt** developer repository.

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
2. Understand the existing logic and context.
3. Make the smallest appropriate change.
4. Run relevant tests or validations.
5. Summarize changes concisely.

### Complex Multi-File Tasks
Run the repository impact briefing script before making structural edits:
python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"

---

## 🛠️ Local Developer Tools

* **Impact Briefing (`/briefing`)** Generates a compressed AST map for complex refactoring, multi-file edits, or unfamiliar areas.
  python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"

* **ShortPrompt Compression (`/shortprompt`)** Compresses or optimizes prompts only when explicitly requested. Preserve original intent and wording by default.
  python shortprompt.py --prompt "PROMPT_TEXT"

* **Local Semantic Search (`/local-search`)** Locates functions or logic semantically across a large codebase using the local LLM.
  python shortprompt_local.py --search "QUERY"

* **Local Task Delegation (`/delegate`)** Offloads repetitive generation (mocks, boilerplate, schemas, test scaffolding) to the local LLM. Always review output before committing.
  python shortprompt_local.py --delegate "TASK_DESCRIPTION" --file "PATH_TO_CONTEXT_FILE"

---

## 🚀 Local LLM Environment (Ollama)

- **Default Endpoint:** http://localhost:11434
- **Default Model:** qwen2.5-coder:1.5b (Adjust based on available hardware and workload)

### Docker Setup
docker run -d \
  --name shortprompt-ollama \
  -v ollama_data:/root/.ollama \
  -p 11434:11434 \
  ollama/ollama

docker exec -it shortprompt-ollama ollama pull qwen2.5-coder:1.5b

Note: Local inference reduces paid API dependency, but it is not token-free and consumes local compute/RAM.

---

## 📐 Quality, Testing & Security Standards

### Code Quality Rules
- Follow existing project style conventions.
- Prefer simple, focused solutions over complex abstractions.
- Do not silently change public APIs or behavior.
- Check and handle new error failure paths properly.

### Testing & Validation
- Run relevant available unit tests and syntax/type checks.
- Review git diff to ensure no unintended modifications occurred.
- Clearly report validation outcomes (or state reasons if tests couldn't be run).

### Git Safety
- **Forbidden Actions:** Never rewrite history, force-push, delete branches, overwrite files blindly, or discard unrelated user changes.
- **Requirement:** Seek explicit confirmation before performing any destructive Git operation.

### Privacy & Security
- Treat user prompts, code, files, and credentials as sensitive.
- Never log or commit secrets, API keys, or private tokens.
- Prefer local processing; avoid sending project data to external services unless requested.

---

## 📦 Scope & Final Response Guidelines

### Repository Scope
This repository covers local LLM workflows, token/context tools, Python developer scripts, and prompt-engineering utilities. Web application assets on ShortPrompt may run in a separate environment—do not modify or make assumptions about the web application runtime unless instructed.

### Final Output Format
When completing tasks, provide a concise summary including:
1. **What changed:** Brief description of functional updates.
2. **Files modified:** Explicit list of affected files.
3. **Tests/Validation:** Summary of validation performed.
4. **Assumptions/Limitations:** Any remaining constraints or dependencies.
