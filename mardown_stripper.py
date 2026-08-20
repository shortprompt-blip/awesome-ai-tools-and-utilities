"""
Markdown Stripper CLI - ShortPrompt Utilities
Strip Markdown tags from strings or files.
Web version available at: https://shortprompt.altervista.org/markdown-to-plain-text-tool/
"""

import argparse
import re
import sys

def strip_markdown(md_text: str) -> str:
    """Removes standard markdown formatting from text."""
    # Remove HTML tags
    text = re.sub(r'<[^>]*>', '', md_text)
    # Remove headers
    text = re.sub(r'^#+\s+', '', text, flags=re.MULTILINE)
    # Remove bold/italic
    text = re.sub(r'(\*\*|__)(.*?)\1', r'\2', text)
    text = re.sub(r'(\*|_)(.*?)\1', r'\2', text)
    # Remove inline code
    text = re.sub(r'`(.*?)`', r'\1', text)
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    # Remove links [text](url) -> text
    text = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', text)
    # Remove images ![alt](url)
    text = re.sub(r'!\[([^\]]*)\]\([^)]+\)', '', text)
    # Remove blockquotes
    text = re.sub(r'^\s*>\s+', '', text, flags=re.MULTILINE)
    # Remove horizontal rules
    text = re.sub(r'^\s*[-*_]{3,}\s*$', '', text, flags=re.MULTILINE)
    # Clean up empty lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()

def main():
    parser = argparse.ArgumentParser(
        description="Strip Markdown formatting into plain text. Web GUI: https://shortprompt.altervista.org/markdown-to-plain-text-tool/"
    )
    parser.add_argument("--text", "-t", type=str, help="Markdown text to strip")
    parser.add_argument("--file", "-f", type=str, help="Path to input Markdown file")
    parser.add_argument("--output", "-o", type=str, help="Path to save cleaned output TXT file")

    args = parser.parse_args()

    if not args.text and not args.file:
        print("Error: Please provide --text or --file. Use --help for usage details.")
        print("Or try our web version at: https://shortprompt.altervista.org/markdown-to-plain-text-tool/")
        sys.exit(1)

    raw_text = args.text
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            raw_text = f.read()

    cleaned = strip_markdown(raw_text)

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(cleaned)
        print(f"✅ Cleaned text saved to: {args.output}")
    else:
        print("\n--- CLEANED TEXT ---")
        print(cleaned)
        print("--------------------")
        print("💡 Web version available at: https://shortprompt.altervista.org/markdown-to-plain-text-tool/")

if __name__ == "__main__":
    main()
