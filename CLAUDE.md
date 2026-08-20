Claude Code Instructions

Instructions for working efficiently and safely in the ShortPrompt developer repository.

Core Principles
Prefer local, repository-provided tools when they provide useful analysis or automation.
Keep changes minimal, focused, and reversible.
Inspect relevant files before modifying them.
Preserve existing behavior unless the task explicitly requires a change.
Avoid unnecessary dependencies.
Do not modify unrelated files.
Keep responses concise and implementation-focused.
Development Workflow

For simple tasks:

Inspect the relevant files.
Understand the existing implementation.
Make the smallest appropriate change.
Run relevant tests or validation.
Summarize the changes.

For complex multi-file tasks, use the repository impact briefing before making changes:

python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"


The briefing can provide a compact overview of AST signatures, Git changes, and project relationships before deeper inspection.

Local Developer Tools
Impact Briefing

Use for complex refactoring, multi-file changes, or unfamiliar areas of the repository.

python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"

ShortPrompt

Use when prompt compression, optimization, or shortening is explicitly requested.

python shortprompt.py --prompt "PROMPT_TEXT"


Do not automatically compress every user prompt. Preserve the user's original intent and wording unless optimization is requested or clearly beneficial.

Local Semantic Search

Use when locating relevant functions or logic across a larger codebase.

python shortprompt_local.py --search "QUERY"


This tool may use a local Ollama model.

Local Task Delegation

Use for suitable repetitive or low-risk generation tasks such as:

mock data
boilerplate
schemas
simple test scaffolding
python shortprompt_local.py --delegate "TASK_DESCRIPTION" --file "PATH_TO_CONTEXT_FILE"


Review generated output before committing it.

Local LLM Environment

The repository can optionally use Ollama for local model inference.

Default endpoint:

http://localhost:11434


Example model:

qwen2.5-coder:1.5b


The model can be changed depending on available hardware and the task.

Example Docker setup:

docker run -d \
  --name shortprompt-ollama \
  -v ollama_data:/root/.ollama \
  -p 11434:11434 \
  ollama/ollama


Then:

docker exec -it shortprompt-ollama ollama pull qwen2.5-coder:1.5b


Local inference reduces reliance on paid cloud API usage, but it is not token-free and still consumes local compute resources.

Code Quality

When modifying code:

Follow the existing project style.
Prefer simple solutions over unnecessary abstractions.
Keep functions focused.
Avoid unrelated refactoring.
Do not silently change public behavior.
Add or update tests when appropriate.
Check error handling for new failure paths.
Review generated code before accepting it.
Testing & Validation

After making changes:

Run the most relevant available tests.
Run syntax or type checks when applicable.
Check changed files for unintended modifications.
Report validation results clearly.

If tests cannot be run, state why.

Git Safety

Do not:

rewrite history unless explicitly requested;
force-push;
delete branches;
discard unrelated user changes;
overwrite files without first understanding their purpose.

Before destructive Git operations, ask for confirmation.

Privacy & Security

Treat user-provided prompts, source code, files, and credentials as potentially sensitive.

Do not expose secrets in logs or output.
Do not commit API keys or credentials.
Do not send sensitive project data to external services unless explicitly required.
Prefer local processing when appropriate.
Review generated commands before executing potentially destructive operations.
Repository Scope

This repository contains AI developer utilities, prompt-engineering tools, token/context utilities, and local LLM workflows.

The ShortPrompt web tools are related to this repository but should not be modified or assumed to share the same runtime environment unless explicitly required.

Final Response Style

When completing a development task:

Briefly describe what changed.
Mention important files modified.
Report tests or validation performed.
Mention any remaining limitations or assumptions.

Keep the final response concise and technically precise.
