"""Rebuild source metadata; never guess dates from folder names."""
from library import write_catalog

if __name__ == "__main__":
    data = write_catalog()
    print(f"Indexed {data['video_count']} videos / {data['cue_count']} subtitle cues.")
