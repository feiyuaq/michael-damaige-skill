import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from library import videos, seconds, timestamp
from search import search


class SubtitleSearchTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.videos = list(videos())
        cls.by_id = {v['id']: v for v in cls.videos}

    def test_all_sources_have_usable_cues_and_links(self):
        self.assertTrue(self.videos)
        for video in self.videos:
            self.assertTrue(video['cues'], video['id'])
            self.assertTrue(video['douyin_url'].startswith('https://v.douyin.com/'))
            self.assertEqual(len({c['number'] for c in video['cues']}), len(video['cues']))

    def test_quotes_are_verbatim_with_exact_times_and_sources(self):
        results = search('低谷', limit=3)
        self.assertTrue(results)
        for result in results:
            video = self.by_id[result['video_id']]
            cues = [c for c in video['cues'] if result['cue_start'] <= c['number'] <= result['cue_end']]
            self.assertEqual(result['quote'], '\n'.join(c['text'] for c in cues))
            self.assertEqual(result['start_seconds'], cues[0]['start'])
            self.assertEqual(result['end_seconds'], cues[-1]['end'])
            self.assertEqual(result['douyin_url'], video['douyin_url'])
        for i, left in enumerate(results):
            for right in results[i+1:]:
                if left['video_id'] == right['video_id']:
                    self.assertFalse(left['start_seconds'] < right['end_seconds'] and left['end_seconds'] > right['start_seconds'])

    def test_filter_and_no_hits(self):
        results = search('放过自己', video_filter='260831')
        self.assertTrue(results)
        self.assertTrue(all('260831' in r['video_id'] for r in results))
        self.assertEqual(search('zxqvnonexistentkeyword94726'), [])
        self.assertEqual(search('！？'), [])

    def test_timestamp_roundtrip(self):
        for value in [0.0, 59.999, 60, 3600.123, 12570.999]:
            self.assertEqual(seconds(timestamp(value)), value)


if __name__ == '__main__':
    unittest.main()
