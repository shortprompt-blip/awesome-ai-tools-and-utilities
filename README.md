⚡ Awesome AI Tools & Utilities

Open-source tools for AI developers, prompt engineering, token optimization, local LLM workflows, and privacy-focused browser utilities.






A growing collection of practical utilities and developer resources for working with modern AI systems.

The repository currently focuses on:

🤖 AI-assisted development workflows
🦙 Ollama and local LLM experimentation
🧠 Prompt engineering and optimization
🔢 Token and context-window utilities
🛠️ Python developer tools
🔐 Privacy-focused, browser-based utilities
📄 Text, Markdown, PDF and data tools

🌐 Related web tools: ShortPrompt

🚀 Local AI Development with Ollama

This repository includes tools and documentation for experimenting with local AI-assisted development workflows using Ollama.

The goal is to make local LLM experimentation easier while keeping the development workflow transparent and reproducible.

Important: Local inference is not token-free. Models still process tokens and consume local CPU, GPU, memory, and storage resources. The benefit is that local inference can avoid paid cloud API usage for workloads that can be handled locally.

Basic architecture
┌────────────────────── Your Computer ──────────────────────┐
│                                                           │
│   Developer / CLI                                         │
│         │                                                 │
│         ▼                                                 │
│   Local AI Workflow                                       │
│         │                                                 │
│         ▼                                                 │
│   ┌───────────────┐                                      │
│   │    Ollama     │                                      │
│   │ localhost:    │                                      │
│   │    11434      │                                      │
│   └───────┬───────┘                                      │
│           │                                               │
│           ▼                                               │
│      Local LLM Model                                      │
│                                                           │
└───────────────────────────────────────────────────────────┘


The exact capabilities of a local workflow depend on the CLI, model, Ollama version, configuration, and hardware being used.

🦙 Ollama Setup

Install Ollama using the official installation instructions for your operating system.

Then download a compatible coding model.

For example:

ollama pull qwen2.5-coder:1.5b


The model can be changed depending on your hardware and workload.

Verify that Ollama is available:

ollama list


The default local API endpoint is:

http://localhost:11434

Docker

Ollama can also be run in Docker:

docker run -d \
  --name shortprompt-ollama \
  -v ollama_data:/root/.ollama \
  -p 11434:11434 \
  ollama/ollama


Then download the model:

docker exec -it shortprompt-ollama ollama pull qwen2.5-coder:1.5b

🤖 Claude Code Compatibility

This repository documents experiments involving Claude Code-compatible configurations and local Ollama models.

Compatibility depends on:

Claude Code version
Ollama version
selected model
API compatibility
environment variables
local hardware

If you use environment variables to point a compatible client toward a local Ollama endpoint, verify the behavior with your specific versions before relying on the configuration for production work.

Example:

export ANTHROPIC_BASE_URL="http://localhost:11434"
export ANTHROPIC_AUTH_TOKEN="ollama"
export ANTHROPIC_API_KEY="ollama"


Do not assume that every Claude Code feature is supported by every local model or Ollama configuration.

📄 CLAUDE.md

A CLAUDE.md file can provide project-specific instructions to an AI coding agent.

Typical information includes:

build commands
test commands
linting rules
architecture conventions
important directories
files that should not be modified
project-specific development guidelines

Example:

# Project Instructions

## Build

npm run build

## Test

npm test

## Lint

npm run lint

## Code Style

- Follow the existing project architecture.
- Avoid unnecessary dependencies.
- Keep changes focused.

## Excluded Directories

- node_modules/
- dist/
- .next/


The exact contents should be adapted to the project being worked on.

🧰 ShortPrompt Tools

This repository is connected to ShortPrompt, a collection of browser-based utilities for AI developers, prompt engineers, and creators.

🧠 Prompt Engineering
System Prompt Builder — Build structured system prompts for LLM workflows.
Prompt Token Compressor — Reduce unnecessary prompt formatting and redundancy.
AI Context Window Calculator — Estimate token usage and context requirements.
JSON Formatter & Validator — Format and validate structured data.
🛠️ Developer Utilities
SVG to PNG conversion
JSON and data formatting
Markdown and text utilities
PDF and document utilities
Token and context calculators
AI development helpers
🔐 Privacy-Focused Browser Tools

Some ShortPrompt utilities are designed to process data directly in the browser.

Depending on the individual tool, technologies may include:

Web APIs
WebAssembly
JavaScript
Web Crypto APIs

Client-side processing can reduce the need to upload files or text to a remote processing server.

Important: Always check the documentation of the individual tool before processing sensitive information. Client-side processing does not automatically mean that every component of a website is completely offline.

🌐 Explore the tools:
https://shortprompt.altervista.org/

🐍 Python Utilities

The repository includes several standalone Python utilities, including:

.
├── CLAUDE.md
├── README.md
├── benchmark_briefing.py
├── claude_impact_briefing.py
├── markdown_stripper.py
├── requirements.txt
├── shortprompt.py
├── shortprompt_local.py
└── token_calculator.py


If you are upgrading from an earlier version, note that mardown_stripper.py should be renamed to markdown_stripper.py.

📦 Installation

Clone the repository:

git clone https://github.com/shortprompt-blip/awesome-ai-tools-and-utilities.git
cd awesome-ai-tools-and-utilities


Create a virtual environment:

python -m venv .venv

macOS / Linux
source .venv/bin/activate

Windows
.venv\Scripts\activate


Install dependencies:

pip install -r requirements.txt

🔎 Impact Briefing

For complex tasks involving multiple files, the repository includes an impact briefing utility:

python claude_impact_briefing.py --task "DESCRIPTION_OF_TASK"


The tool is intended to provide a compact overview before deeper code inspection.

Use it when it is useful; it is not required for every task.

✂️ Prompt Compression

The repository also includes a local prompt utility:

python shortprompt.py --prompt "YOUR_PROMPT"


Use it when prompt compression or optimization is actually useful.

Prompt compression should preserve the original intent and should not be applied automatically to every prompt.

🔍 Local Semantic Search

The local utility can be used for semantic code-search experiments:

python shortprompt_local.py --search "QUERY"


Depending on configuration, this can use a local Ollama model.

🧪 Validation

After modifying code:

Run the relevant tests.
Run syntax or type checks where applicable.
Check the Git diff.
Verify that unrelated files were not changed.

If a test cannot be run, document the reason.

💻 Local LLM Hardware

Local model performance depends on:

model size
quantization
available RAM
GPU/VRAM
CPU performance
context length
workload

As a general guideline:

Hardware	Possible workload
8–16 GB RAM	Smaller models and lightweight tasks
32 GB RAM	Larger models and longer-context workflows
64 GB+ RAM / dedicated GPU	More demanding local models and codebase analysis

Actual performance varies significantly between systems. Benchmark your own hardware whenever possible.

🗺️ Roadmap
 Add automated tests
 Add GitHub Actions CI
 Improve documentation for individual utilities
 Add more local LLM workflows
 Add token/context benchmarks
 Add reproducible model benchmarks
 Improve cross-platform support
 Add real-world workflow examples
 Improve contribution documentation
 Expand privacy-focused developer utilities
🤝 Contributing

Contributions are welcome.

You can contribute by:

Opening an issue.
Improving documentation.
Adding tests.
Improving an existing utility.
Adding a useful developer tool.
Sharing reproducible benchmarks.

Please keep pull requests focused and explain the reason for significant changes.

🐛 Issues

Found a bug or have an idea?

Open an issue.

When reporting a problem, include:

Operating system
Python version
Ollama version, if relevant
Model name/version, if relevant
Steps to reproduce
Expected behavior
Actual behavior
📚 Resources
🌐 ShortPrompt
💻 GitHub Repository
🤖 Claude Documentation
🦙 Ollama
📜 License

See the repository license file for the current licensing terms.

⭐ Support the Project

If you find the project useful:

⭐ Star the repository
🐛 Report bugs
💡 Suggest improvements
🔀 Submit a pull request
📢 Share it with other AI developers

Built for developers exploring AI, local LLMs, prompt engineering, and privacy-focused tooling.
