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
            p_play = []
            for playlist in play_lists['playlists']:
                print(playlist)
                p_play.append(playlist)

            print(p_play)
            return p_play

    def add_song_to_playlist(self, playlist_name, song_name, easy_directory):
        print('Adding a new song')
        print(playlist_name, song_name, easy_directory)
        with open('playlists.json') as play_list:
            play_list = json.load(play_list)
            print(play_list)
            play_list['playlists'][playlist_name].append(
                {'name': song_name,
                'easy_play_directory': easy_directory
                 }
            )
            print(play_list)
            with open('playlists.json', 'w') as outfile:
                json.dump(play_list, outfile)
            print('Saved to song to playlist')

    def remove_from_playlist(self):
        print('remove')


if __name__ == '__main__':
    play = PlayList()
    play.add_song_to_playlist('SuperCoolPlaylist1', 'Song2', 'User/location2')