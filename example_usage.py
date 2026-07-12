"""
example_usage.py -- Demonstrates SemrushAIOToolkitClient
"""
from client import SemrushAIOToolkitClient

def main():
    client = SemrushAIOToolkitClient()
    result = client.optimize_keywords(
        target_keywords=["AIO SEO", "AI Overview marketing"],
        page_copy="This document covers optimizing B2B website channels for search."
    )
    print("[Semrush AIO Toolkit Result]")
    print(f"Overlap Score: {result['semrush_keyword_overlap_score']}")
    print(f"Optimized Copy:\n{result['optimized_copy']}")

if __name__ == "__main__":
    main()
