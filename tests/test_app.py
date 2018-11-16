import unittest
import app
from mock import patch


class TestApp(unittest.TestCase):

    def test_media_list_org(self):
        test_data = {'media': [{'name': 'test_song1', 'file_directory': '/Users/jamessheard/Desktop', 'media_type': 'mp3',
                                'easy_play_directory': '/Users/jamessheard/Desktop/TestSong1.mp3'},
                               {'name': 'test_song2', 'file_directory': '/Users/jamessheard/Desktop', 'media_type': 'mp3',
                                'easy_play_directory': '/Users/jamessheard/Desktop/TestSong2.mp3'}]}

        expected_result = ['test_song1', 'test_song2']
        actual_result = app.media_list_org(test_data)

        self.assertEqual(expected_result, actual_result)

    def test_add_to_playlist(self):
        app.create_playlist('TestData')
        with patch('play.add_song_to_playlist') as play_list_func:
            play_list_func.assert_called_once()

