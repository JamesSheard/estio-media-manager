import os
import json

class PlayList:

    def create_play_list(self, playlist_name):
        with open('playlists.json') as play_list:
            play_list = json.load(play_list)
            print(play_list)
            play_list['playlists'][playlist_name] = []
            print(play_list)
            with open('playlists.json', 'w') as outfile:
                json.dump(play_list, outfile)
            print('Saved to playlist to json file')


    def read_playlists(self):
        with open('playlists.json') as play_lists:
            play_lists = json.load(play_lists)
            playlist_to_return = []
            for playlist in play_lists['playlists']:
                playlist_to_return.append(playlist)
            return playlist_to_return

    def add_song_to_playlist(self, playlist_name, song_name, easy_directory):
        print('Adding a new song')
        print(playlist_name, song_name, easy_directory)
        with open('playlists.json') as play_list:
            play_list = json.load(play_list)
            print(play_list)
            play_list['playlists'][playlist_name].append(
                {'name': song_name,
                 #'img_directory': img_directory,
                 'comment': None,
                 'easy_play_directory': easy_directory
                 }
            )
            print(play_list)
            with open('playlists.json', 'w') as outfile:
                json.dump(play_list, outfile)
            print('Saved to song to playlist')

    def delete_playlist(self, playlist_name):
        with open('playlists.json') as play_list:
            play_list = json.load(play_list)
            play_list['playlists'].pop(playlist_name)
        with open('playlists.json', 'w') as outfile:
            json.dump(play_list, outfile)

    def delete_song_from_playlist(self, playlist_name, delete_song):
        with open('playlists.json') as play_list:
            play_list = json.load(play_list)
            count = 0
            for song in play_list['playlists'][playlist_name]:
                if song['song'] == delete_song:
                    play_list['playlists'][playlist_name].pop(count)
                else:
                    count+=1
        with open('playlists.json', 'w') as outfile:
            json.dump(play_list, outfile)

    def add_comment_to_song(self, playlist_name, song_for_comment, comment):
        with open('playlists.json') as play_list:
            play_list = json.load(play_list)
            count = 0
            for song in play_list['playlists'][playlist_name]:
                if song['song'] == song_for_comment:
                    play_list['playlists'][playlist_name][count]['comment'] = comment
                else:
                    count+=1
        with open('playlists.json', 'w') as outfile:
            json.dump(play_list, outfile)