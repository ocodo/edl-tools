import unittest

import os

from get_edl_sources import get_edl_media

def fixture(name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', name)

class TestGetEdlMedia(unittest.TestCase):

    def test_get_edl_media_exclude_metadata_lines(self):
        edl_file = fixture('test1.edl')
        media = get_edl_media(edl_file)

        self.assertNotIn('', media)
        self.assertNotIn('#mpv EDL v0', media)
        self.assertNotIn('!new_stream', media)

    def test_get_edl_media(self):
        edl_file = fixture('test1.edl')
        media = get_edl_media(edl_file)

        self.assertIn('video.mp4', media)
        self.assertIn('video1.mp4', media)
        self.assertIn('video3.mp4', media)
        self.assertIn('audio.mp3', media)

    def test_get_edl_media_without_edl_names(self):
        edl_file = fixture('test2.edl')
        media = get_edl_media(edl_file)

        self.assertNotIn('fixtures/test1.edl', media)
        self.assertIn('video5.mp4', media)
        self.assertIn('video.mp4', media)
        self.assertIn('video0.mp4', media)
        self.assertIn('video1.mp4', media)
        self.assertIn('video3.mp4', media)
        self.assertIn('video4.mp4', media)
        self.assertIn('audio.mp3', media)
        self.assertIn('/Volumes/spare/videos/video.mp4', media)

if __name__ == '__main__':
    unittest.main()
