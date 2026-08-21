---
name: agent-context-manager
description: Automatically prunes multi-turn agent execution logs, strips raw tool outputs, and maintains a clean state buffer to preserve token budget in long sessions.
---

# Agent Context Manager

Use this skill during multi-step workflows or long agent sessions where conversation context grows significantly due to raw terminal outputs or file reads.

## Invocations

```bash
python claude_agent_context_manager.py --history "PATH_TO_SESSION_HISTORY.json"
