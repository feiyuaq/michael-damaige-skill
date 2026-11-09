"""Offline lexical search returning verbatim contiguous cues and source times."""
import argparse
import json
import math
import re
import sys
from collections import Counter
from library import videos, timestamp


def normalize(text):
    return re.sub(r"[^\w\u4e00-\u9fff]", "", text.lower())


def tokens(text):
    parts = re.findall(r"[\u4e00-\u9fff]+|[a-z0-9]+", text.lower())
    result = []
    for part in parts:
        if re.fullmatch(r"[a-z0-9]+", part) or len(part) == 1:
            result.append(part)
        else:
            result.extend(part[i:i+2] for i in range(len(part)-1))
    return result


def search(query, limit=5, video_filter=None):
    query_tokens = set(tokens(query))
    if not query_tokens:
        return []
    windows = []
    for video in videos():
        if video_filter and video_filter not in video["id"]:
            continue
        cues = video["cues"]
        for i in range(len(cues)):
            segment = cues[i:i+8]
            # Do not join cues across long silent gaps.
            for j in range(1, len(segment)):
                if segment[j]["start"] - segment[j-1]["end"] > 5:
                    segment = segment[:j]
                    break
            text = "\n".join(c["text"] for c in segment)
            counts = Counter(tokens(text))
            windows.append((video, segment, text, counts))
    n = len(windows)
    df = Counter()
    for _, _, _, counts in windows:
        df.update(query_tokens.intersection(counts))
    ranked = []
    for video, segment, text, counts in windows:
        matches = query_tokens.intersection(counts)
        if not matches:
            continue
        score = sum(math.log(1 + (n + 1) / (df[t] + 1)) * (1 + math.log(counts[t])) for t in matches)
        score /= 1 + len(tokens(text)) / 100
        if normalize(query) in normalize(text):
            score += 15
        score += len(query_tokens.intersection(tokens(video["title"]))) * 0.2
        ranked.append((score, video, segment, text, matches))
    ranked.sort(key=lambda row: row[0], reverse=True)
    results = []
    for score, video, segment, text, matches in ranked:
        start, end = segment[0]["start"], segment[-1]["end"]
        if any(r["video_id"] == video["id"] and start < r["end_seconds"] and end > r["start_seconds"] for r in results):
            continue
        results.append({"video_id": video["id"], "title": video["title"],
                        "start": timestamp(start), "end": timestamp(end),
                        "start_seconds": start, "end_seconds": end,
                        "cue_start": segment[0]["number"], "cue_end": segment[-1]["number"],
                        "quote": text, "srt": video["srt"], "douyin_url": video["douyin_url"],
                        "matched_terms": sorted(matches), "score": round(score, 3)})
        if len(results) >= limit:
            break
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query")
    parser.add_argument("--limit", type=int, default=5)
    parser.add_argument("--video", help="Video id/title substring")
    args = parser.parse_args()
    if not 1 <= args.limit <= 20:
        parser.error("--limit must be between 1 and 20")
    print(json.dumps({"query": args.query, "results": search(args.query, args.limit, args.video),
                      "note": "按字幕时间定位；未与视频逐条校时。检索命中不代表观点相关，请阅读上下文。"}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
