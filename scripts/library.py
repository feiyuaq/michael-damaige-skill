"""Read original SRT files without changing their text. Standard library only."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TIME = re.compile(r"(\d{2,}):(\d{2}):(\d{2})[,.](\d{3})")


def seconds(value):
    h, m, s, ms = map(int, TIME.fullmatch(value.strip()).groups())
    return round(h * 3600 + m * 60 + s + ms / 1000, 3)


def timestamp(value):
    millis = round(value * 1000)
    hours, millis = divmod(millis, 3600000)
    minutes, millis = divmod(millis, 60000)
    secs, millis = divmod(millis, 1000)
    return f"{hours:02}:{minutes:02}:{secs:02}.{millis:03}"


def read_cues(path):
    text = path.read_text(encoding="utf-8-sig").replace("\r\n", "\n").strip()
    cues = []
    for block in re.split(r"\n\s*\n", text):
        lines = block.splitlines()
        if len(lines) < 3 or "-->" not in lines[1]:
            raise ValueError(f"Invalid subtitle block: {path}: {block[:80]}")
        start, end = lines[1].split("-->")
        cue = {"number": int(lines[0]), "start": seconds(start),
               "end": seconds(end), "text": "\n".join(lines[2:])}
        if cue["end"] < cue["start"] or (cues and cue["start"] < cues[-1]["start"]):
            raise ValueError(f"Invalid timeline: {path}, cue {cue['number']}")
        cues.append(cue)
    return cues


def videos():
    for path in sorted((ROOT / "STR").glob("*/*.srt")):
        info = path.with_name("视频信息.txt")
        raw = info.read_text(encoding="utf-8-sig") if info.exists() else ""
        urls = re.findall(r"https?://[^\s]+", raw)
        yield {"id": path.parent.name, "title": path.parent.name.split("_", 1)[-1],
               "srt": path.relative_to(ROOT).as_posix(),
               "info": info.relative_to(ROOT).as_posix() if info.exists() else None,
               "douyin_url": urls[0] if urls else None,
               "cues": read_cues(path)}


def write_catalog():
    rows = []
    for video in videos():
        cues = video.pop("cues")
        rows.append({**video, "cue_count": len(cues), "duration_seconds": cues[-1]["end"] if cues else 0,
                     "publication_date": None, "source_verified": False})
    result = {"schema_version": "1.0", "video_count": len(rows),
              "cue_count": sum(v["cue_count"] for v in rows), "videos": rows}
    (ROOT / "catalog.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return result
