"""
ShortPrompt Briefing Benchmark Suite
Calculates exact empirical context reduction and execution speed metrics.
Zero external dependencies required.
"""

import argparse
import os
import time
from claude_impact_briefing import (
    IGNORE_DIRS,
    ALLOWED_EXTS,
    detect_tech_stack,
    generate_briefing,
    get_git_status
)

def calculate_full_repository_metrics(root_dir="."):
    """Calculates total files, total words, and total tokens in the entire repository."""
    total_files = 0
    total_words = 0
    
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for file in files:
            ext = os.path.splitext(file)[1].lower()
            if ext in ALLOWED_EXTS:
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        words = len(content.split())
                        total_words += words
                        total_files += 1
                except Exception:
                    continue

    # ~1 token ≈ 0.75 words (standard LLM estimation)
    total_tokens = int(total_words / 0.75)
    return total_files, total_words, total_tokens

def run_benchmark(task_query, root_dir="."):
    print("\n⚡ RUNNING EMPIRICAL CONTEXT BENCHMARK...")
    print("==========================================================")
    
    # 1. Measure full repository context size
    start_time = time.perf_counter()
    full_files, full_words, full_tokens = calculate_full_repository_metrics(root_dir)
    
    if full_tokens == 0:
        print("❌ Error: No valid code files found to benchmark.")
        return

    # 2. Capture briefing output & execution time
    import io
    from contextlib import redirect_stdout

    buffer = io.StringIO()
    briefing_start = time.perf_counter()
    with redirect_stdout(buffer):
        generate_briefing(task_query, root_dir)
    briefing_execution_time_ms = (time.perf_counter() - briefing_start) * 1000

    briefing_raw_output = buffer.getvalue()
    briefing_words = len(briefing_raw_output.split())
    briefing_tokens = int(briefing_words / 0.75)

    # 3. Calculate mathematical context reduction
    saved_tokens = max(0, full_tokens - briefing_tokens)
    reduction_pct = (saved_tokens / full_tokens) * 100 if full_tokens > 0 else 0.0

    # 4. Display Empirical Benchmark Results
    print(f"📊 BENCHMARK RESULTS SUMMARY")
    print(f"• Repository Files Scanned: {full_files} files")
    print(f"• Full Repository Size:     {full_tokens:,} tokens ({full_words:,} words)")
    print(f"• Briefing Output Size:    {briefing_tokens:,} tokens ({briefing_words:,} words)")
    print(f"• Token Savings:           -{saved_tokens:,} tokens")
    print(f"• Real Context Reduction:  {reduction_pct:.2f}%")
    print(f"• Execution Latency:       {briefing_execution_time_ms:.2f} ms")
    print("==========================================================")
    print(f"✅ Verified: Briefing reduces prompt size by {reduction_pct:.1f}% on this workspace.\n")

def main():
    parser = argparse.ArgumentParser(description="Empirical context benchmark for Claude Code briefing tool.")
    parser.add_argument("--task", "-t", type=str, default="Refactor authentication and test cases", help="Sample task description")
    parser.add_argument("--dir", "-d", type=str, default=".", help="Target repository directory")
    args = parser.parse_args()

    run_benchmark(args.task, args.dir)

if __name__ == "__main__":
    main()
  
