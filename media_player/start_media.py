import os
import json
import subprocess
import signal
import pygame.mixer
from state_store.playlist_manager import PlayList


class MediaPlayer:

    def play_mp3(self, play_file):
        global media_playing

        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.mixer.quit()
        pygame.mixer.init()
        pygame.mixer.music.load(play_file)
        pygame.mixer.music.play(0)

    def pause_mp3(self):
        pygame.mixer.music.pause()

    def unpause_mp3(self):
        pygame.mixer.music.unpause()

    def kill_media(self):
        try:
            os.killpg(os.getpgid(media_playing.pid), signal.SIGTERM)
            print('Media Stopped')
        except:
            print('First time playing media')

    def play_playlist(self, playlist_selected):
        play = PlayList()
        playlists = play.read_playlists()


        for song in playlists['playlists']['playlist_selected']:
            pygame.mixer.music.queue(song['easy_play_directory'])
