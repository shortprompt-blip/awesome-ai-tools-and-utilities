"""
ShortPrompt Engine - Local Prompt Minifier & Optimizer
Compresses verbose LLM prompts into deterministic, high-density directives.

Web Tool: https://shortprompt.altervista.org/
"""

import argparse
import re
import sys

# Common conversational filler words and redundant phrases
FILLER_PATTERNS = [
    (r'\b(can you|could you|please|kindly|i would like you to|i want you to)\b', ''),
    (r'\b(make sure to|make sure that you|be sure to)\b', ''),
    (r'\b(i need a|i need you to|help me)\b', ''),
    (r'\b(as an ai language model|as a helpful assistant)\b', ''),
    (r'\s+', ' ')  # Clean extra whitespaces
]

def compress_prompt(text: str) -> str:
    """Applies rule-based heuristic compression to raw prompt text."""
    compressed = text
    
    # 1. Strip polite phrases and verbosity
    for pattern, replacement in FILLER_PATTERNS:
        compressed = re.sub(pattern, replacement, compressed, flags=re.IGNORECASE)
        
    # 2. Split sentences into clean bullet points if text is long
    sentences = [s.strip() for s in re.split(r'[.!?]\s+', compressed) if s.strip()]
    
    if len(sentences) > 1:
        formatted_lines = [f"- {s[0].upper() + s[1:]}" for s in sentences]
        return "\n".join(formatted_lines)
    
    return compressed.strip()

def main():
    parser = argparse.ArgumentParser(
        description="ShortPrompt Engine: Compress verbose prompts into dense LLM instructions."
    )
    parser.add_argument("--prompt", "-p", type=str, help="Raw prompt text to compress")
    parser.add_argument("--file", "-f", type=str, help="Input file containing long system prompt")
    
    args = parser.parse_args()
    
    if not args.prompt and not args.file:
        print("Error: Provide --prompt or --file. Web version: https://shortprompt.altervista.org/")
        sys.exit(1)
        
    raw_text = args.prompt
    if args.file:
        with open(args.file, "r", encoding="utf-8") as f:
            raw_text = f.read()
            
    compressed = compress_prompt(raw_text)
    
    orig_words = len(raw_text.split())
    comp_words = len(compressed.split())
    savings = round(((orig_words - comp_words) / orig_words) * 100, 1) if orig_words > 0 else 0
    
    print("\n⚡ SHORTPROMPT OPTIMIZED OUTPUT:")
    print("-----------------------------------")
    print(compressed)
    print("-----------------------------------")
    print(f"📊 Words reduced from {orig_words} to {comp_words} ({savings}% saved)")
    print("💡 Try online system prompt builders: https://shortprompt.altervista.org/\n")

if __name__ == "__main__":
    main()
