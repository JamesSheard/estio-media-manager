from state_store.data_saver import DataStorer
from discovery.file_finder import FileFinder
from media_player.start_media import MediaPlayer
from state_store.playlist_manager import PlayList
from tkinter import filedialog
from tkinter import *


'''

I didn't managed to add all the features in that was request. This was mainly down to time and not having the knowledge
on creating local apps. Within work I usually create Python apps which run on servers and then can be accessed through
a browser. However, this was a good learning experience and I've managed to create a fully functioning app with the main
features that were asked for.

The UI doesn't link up how it is intended but still does work. Every other file such as playlist manager works as intended.

'''


def store_directory(directory_to_create):
    data = DataStorer()
    data.save_file_directory(directory_to_create)

def open_folder():
    file = filedialog.askdirectory(initialdir="/Users")
    store_directory(file)

def media_list_org(media_to_play):
    print(media_to_play)
    list = []

    for name in media_to_play['media']:
        list.append(name['name'])

    print(list)
    return list

def play_media(value):
    play = MediaPlayer()
    for media in media_options['media']:
        if media['name'] == value:
            print(media['easy_play_directory'])
            play.play_mp3(media['easy_play_directory'])
    global selected_song
    selected_song = value

def pause_music():
    play = MediaPlayer()
    play.pause_mp3()

def unpause():
    play = MediaPlayer()
    play.unpause_mp3()

def create_playlist(playlist_text):
    play = PlayList()
    play.create_play_list(playlist_text)

def get_playlists():
    play = PlayList()
    playlist = play.read_playlists()
    return playlist

def add_to_playlist(playlist_text):
    print('Into add to playlist')
    play = PlayList()
    for media in media_options['media']:
        print(media['name'])
        print(selected_song)
        if media['name'] == selected_song:
            play.add_song_to_playlist(playlist_text, selected_song, media['easy_play_directory'])

def play_playlist(value):
    play = MediaPlayer()
    play.play_playlist(value)

def delete_playlist(value):
    playlist = PlayList()
    playlist.delete_playlist(value)

def ui_gen():
    master = Tk()

    # Opens a file explorer for the user to select which file directory to import
    Label(master, text="Import media").grid(row=0, column=0, sticky=W, pady=4)
    Button(master, text='Select a directory to import all media from', command=open_folder).grid(row=1, column=0,
                                                                                                 sticky=W, pady=4)

    file_finder = FileFinder()

    # Find the MP3 files within the directories saved by the user
    global media_options
    media_options = file_finder.find_files_in_directory()
    pretty_media_list = media_list_org(media_options)

    # Put the MP3 files into a list for the user to select
    global media_list
    media_list = StringVar(master)
    media_list.set(pretty_media_list[0])
    select_song_text = Label(master, text="Select a song to play").grid(row=3, column=0, sticky=W, pady=4)
    media_list = OptionMenu(master, media_list, *pretty_media_list, command=play_media).grid(row=4, column=0, sticky=W, pady=4)

    # Pause and play buttons for the media
    Button(master, text='Pause', command=pause_music).grid(row=4, column=1, sticky=W, pady=4)
    Button(master, text='Play', command=unpause).grid(row=4, column=2, sticky=W, pady=4)

    # Playlist creation
    playlist_text = Label(master, text="Create a playlist").grid(row=6, column=0, sticky=W, pady=4)
    Label(master, text="Please enter a playlist name").grid(row=7)
    playlist_name = Entry(master)
    playlist_name.grid(row=8, column=0)
    Button(master, text='Create', command=lambda: create_playlist(playlist_name.get())).grid(row=8, column=1, sticky=W, pady=4)

    # Show a list of playlists that have been created
    pretty_playlist_list = get_playlists()
    playlists = StringVar(master)
    playlists.set(pretty_playlist_list[0])
    Label(master, text="Select a playlist").grid(row=9, column=0, sticky=W, pady=4)
    playlists = OptionMenu(master, playlists, *pretty_playlist_list, command=play_media).grid(row=10, column=0, sticky=W,
                                                                                             pady=4)

    # Add the current song to the playlist
    Button(master, text='Add current song to selected playlist', command=lambda: add_to_playlist(playlist_name.get())).grid(row=11, column=0,
                                                                                                       sticky=W, pady=4)

    Button(master, text='Play songs from playlist', command=play_playlist).grid(row=11, column=1, sticky=W, pady=4)

    Button(master, text='Delete current playlist', command=delete_playlist).grid(row=12, column=0, sticky=W, pady=4)

    mainloop()

if __name__ == '__main__':
    ui_gen()