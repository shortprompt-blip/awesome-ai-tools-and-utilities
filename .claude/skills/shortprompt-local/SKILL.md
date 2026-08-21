---
name: shortprompt-local
description: Performs semantic code search across the project or delegates repetitive generation tasks (boilerplate, schemas) to a local Ollama LLM.
---

# ShortPrompt Local Utilities

Use this skill to search functions semantically across large files or to offload low-risk code generation tasks locally.

## Invocations

```bash
# Semantic Code Search
python shortprompt_local.py --search "QUERY"

# Task Delegation
python shortprompt_local.py --delegate "TASK_DESCRIPTION"
