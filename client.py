"""
genpark-semrush-aio-toolkit-skill: Client SDK
Optimizes semantic keyword placements using Semrush AIO guidelines.
"""
from __future__ import annotations
from typing import Optional


class SemrushAIOToolkitClient:
    """
    SDK for AIO semantic optimization.
    """

    def optimize_keywords(
        self,
        target_keywords: list[str],
        page_copy: str,
    ) -> dict:
        copy_lower = page_copy.lower()
        matched = 0

        for kw in target_keywords:
            if kw.lower() in copy_lower:
                matched += 1

        overlap = matched / max(1, len(target_keywords))

        optimized = (
            f"**Key Focus: {', '.join(target_keywords)}**\n\n"
            f"{page_copy}"
        )

        return {
            "optimized_copy": optimized,
            "semrush_keyword_overlap_score": round(overlap, 2),
            "status": "fully_optimized" if overlap >= 0.8 else "needs_semantic_update"
        }
