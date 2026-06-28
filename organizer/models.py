from dataclasses import dataclass


@dataclass
class SortStatistics:
    total_files: int = 0
    images: int = 0
    documents: int = 0
    music: int = 0
    videos: int = 0
    others: int = 0