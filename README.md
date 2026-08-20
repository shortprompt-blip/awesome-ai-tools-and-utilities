# awesome-ai-tools-and-utilities
A collection of free web-based utilities for AI prompt engineering, token counting, text cleaning, and file conversion.

# 🛠️ ShortPrompt Developer Toolkit & AI Utilities

A complete open-source suite of zero-token local CLI tools, pre-execution context optimizers for **Claude Code**, and free web utilities for AI developers and prompt engineers.

> 🌐 **Prefer a Browser GUI?** Access all these utilities online with zero setup at [ShortPrompt.altervista.org](https://shortprompt.altervista.org/).

---

## ⚡ Featured: Claude Code Token Saver & Impact Briefing

When using autonomous agents like **Claude Code**, reading entire codebases consumes thousands of API tokens and fills up your context window. 

`claude_impact_briefing.py` runs **locally on your machine (0 tokens used)** before launching Claude Code. It scans Git diffs, AST signatures, and import graphs to generate a hyper-compact impact map (>95% context saved).

### Quick Usage:
```bash
python claude_impact_briefing.py --task "Fix authentication bug in user controller"
```

---

## 📊 Empirical Benchmarks & Token Verification

Instead of relying on estimated claims, you can verify the exact context compression ratio on your own codebase using the included benchmark suite:

```bash
python benchmark_briefing.py --task "Add rate limiting to API endpoints"
```

---

## 💻 Included Local Python CLI Tools

Run these scripts directly in your terminal using standard Python (no external dependencies required):

| CLI Script | Description | Web GUI Version |
| :--- | :--- | :--- |
| `claude_impact_briefing.py` | Local AST & Git diff scanner for Claude Code pre-execution briefing. | [Context Calculator](https://shortprompt.altervista.org/ai-context-windows-calculator/) |
| `markdown_stripper.py` | Strips all Markdown formatting (bold, links, headers) into clean text. | [Markdown Stripper](https://shortprompt.altervista.org/markdown-to-plain-text-tool/) |
| `token_calculator.py` | Estimates tokens, word counts, and context limits for GPT-4o, Claude 3.5 & Gemini. | [Token Estimator](https://shortprompt.altervista.org/ai-context-windows-calculator/) |

---

## 🌐 Complete ShortPrompt Web Utilities Directory

Prefer no installation? Access our full suite of free browser-based tools:

### 🤖 AI & Prompt Engineering
* 📊 **[AI Context Window & Token Calculator](https://shortprompt.altervista.org/ai-context-windows-calculator/)** - Calculate token-to-word ratios and context limits for GPT-4o, Claude 3.5 Sonnet, and Gemini 1.5.
* ✍️ **[Italian AI Text Humanizer](https://shortprompt.altervista.org/ai-text-humanizer-umanizzatore-testo-chatgpt-gratis/)** - Convert rigid AI-generated text into natural, fluent Italian prose.
* 📝 **[System Prompt Templates](https://shortprompt.altervista.org/system-prompt-templates/)** - Production-ready system prompts for Claude Artifacts, ChatGPT Canvas, and Custom GPTs.

### 🧹 Text & Format Cleaners
* 📄 **[Markdown Stripper & Text Cleaner](https://shortprompt.altervista.org/markdown-to-plain-text-tool/)** - Instantly strip Markdown formatting tags into clean plain text for copy-pasting.
* 🔄 **[JSON Schema Data Formatter](https://shortprompt.altervista.org/json-schema-data-formatter-per-llm/)** - Format and clean JSON schemas optimized for LLM context injection.

### 🖼️ Media & File Converters
* 🎨 **[SVG to PNG Converter](https://shortprompt.altervista.org/svg-to-png-converter/)** - Browser-side vector to PNG image rendering.
* 🖼️ **[Background Remover](https://shortprompt.altervista.org/rimuovi-sfondo-immagini/)** - Client-side image background removal tool.
* 📑 **[PDF Page Splitter & Extractor](https://shortprompt.altervista.org/pdf-page-splitter-extractor/)** - Extract specific page ranges from PDF documents locally.
* 🔒 **[Base64 Encoder / Decoder](https://shortprompt.altervista.org/base64-encoder-decoder/)** - Fast string and binary encoding/decoding tool.

---

## 🚀 Quick Start & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/shortprompt-blip/awesome-ai-tools-and-utilities.git
cd awesome-ai-tools-and-utilities
```

### 2. Run CLI Tools

* **Pre-Execution Briefing for Claude Code:**
  ```bash
  python claude_impact_briefing.py --task "Add dark mode toggle to navigation bar"
  ```

* **Strip Markdown Formatting:**
  ```bash
  python markdown_stripper.py --text "# Header **Bold Text** [Link](https://example.com)"
  ```

* **Calculate LLM Tokens:**
  ```bash
  python token_calculator.py --words 4500 --model claude-3.5-sonnet
  ```

---

## 🤖 Claude Code Custom Skill Integration

This repository includes a native `CLAUDE.md` configuration file. When you open this workspace with **Claude Code**, it automatically gains access to all ShortPrompt workflow instructions and local execution protocols.

---

## 📜 License
MIT License. Free to use for personal, open-source, and commercial projects.

*Maintained by [ShortPrompt.altervista.org](https://shortprompt.altervista.org/)*
