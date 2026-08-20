# 🤖 Claude Code Instructions & ShortPrompt Integration

When working in this repository or interacting with ShortPrompt developer tools, follow these instructions to minimize context window consumption and maximize efficiency.

## ⚡ Pre-Task Execution Protocol
Before starting complex multi-file refactoring or feature implementation, run the local impact briefing script to generate a compressed AST map:

```bash
python claude_impact_briefing.py --task "YOUR_FEATURE_OR_BUG_DESCRIPTION"
