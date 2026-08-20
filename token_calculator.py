"""
LLM Token & Context Window Calculator CLI - ShortPrompt Utilities
Estimate tokens, words, and context window usage for GPT-4o, Claude 3.5, and LLMs.
Web version available at: https://shortprompt.altervista.org/ai-context-windows-calculator/
"""

import argparse
import sys

# Average estimates
WORDS_PER_TOKEN = 0.75  # ~1 token ≈ 0.75 words in English/Italian code mix

MODELS = {
    "gpt-4o": {"max_tokens": 128000, "name": "OpenAI GPT-4o"},
    "claude-3.5-sonnet": {"max_tokens": 200000, "name": "Anthropic Claude 3.5 Sonnet"},
    "gemini-1.5-pro": {"max_tokens": 2000000, "name": "Google Gemini 1.5 Pro"},
}

def analyze_context(words_count: int, model_key: str = "gpt-4o"):
    est_tokens = int(words_count / WORDS_PER_TOKEN)
    model_info = MODELS.get(model_key, MODELS["gpt-4o"])
    max_tok = model_info["max_tokens"]
    usage_pct = min(100.0, (est_tokens / max_tok) * 100)

    return {
        "words": words_count,
        "est_tokens": est_tokens,
        "model": model_info["name"],
        "max_context": max_tok,
        "usage_pct": round(usage_pct, 2)
    }

def main():
    parser = argparse.ArgumentParser(
        description="Estimate LLM tokens & context window usage. Web GUI: https://shortprompt.altervista.org/ai-context-windows-calculator/"
    )
    parser.add_argument("--text", "-t", type=str, help="Input text to calculate")
    parser.add_argument("--words", "-w", type=int, help="Word count directly")
    parser.add_argument("--model", "-m", choices=list(MODELS.keys()), default="gpt-4o", help="Target LLM model")

    args = parser.parse_args()

    if args.text:
        words = len(args.text.split())
    elif args.words:
        words = args.words
    else:
        print("Error: Provide --text or --words. Use --help for details.")
        print("Or try the web calculator: https://shortprompt.altervista.org/ai-context-windows-calculator/")
        sys.exit(1)

    result = analyze_context(words, args.model)

    print("\n--- LLM TOKEN & CONTEXT ANALYSIS ---")
    print(f"Model: {result['model']}")
    print(f"Words Count: {result['words']:,}")
    print(f"Est. Tokens: {result['est_tokens']:,}")
    print(f"Max Context: {result['max_context']:,} tokens")
    print(f"Context Window Used: {result['usage_pct']}%")
    print("-----------------------------------")
    print("💡 Detailed visual breakdown: https://shortprompt.altervista.org/ai-context-windows-calculator/")

if __name__ == "__main__":
    main()
  
