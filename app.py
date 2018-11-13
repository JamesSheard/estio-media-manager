from state_store.data_saver import DataStorer
from discovery.file_finder import FileFinder
from media_player.start_media import MediaPlayer
import time
from tkinter import filedialog
from tkinter import *
import subprocess
import os





def store_directory(directory_to_create):
    data = DataStorer()
    data.save_file_directory(directory_to_create)

def open_folder():
    file = filedialog.askdirectory(initialdir="/Users")
    store_directory(file)

def media_list_org(media_to_play):
    list = []

    for name in media_to_play['media']:
        list.append(name['name'])

    return list

def play_media(value):
    play = MediaPlayer()
    for media in media_options['media']:
        if media['name'] == value:
            print(media['easy_play_directory'])
            play.play_mp3(media['easy_play_directory'])

def pause_music():
    play = MediaPlayer()
    play.pause_mp3()

def unpause():
    play = MediaPlayer()
    play.unpause_mp3()

def play_video():
    cap = cv2.VideoCapture("video.mp4")
    ret, frame = cap.read()
    while (1):
        ret, frame = cap.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or ret == False:
            cap.release()
            cv2.destroyAllWindows()
            break
        cv2.imshow('frame', frame)

def ui_gen():
    master = Tk()

    file_finder = FileFinder()

    global media_options
    media_options = file_finder.find_files_in_directory()
    pretty_media_list = media_list_org(media_options)

    global media_list
    media_list = StringVar(master)
    media_list.set(pretty_media_list[0])

    media_list = OptionMenu(master, media_list, *pretty_media_list, command=play_media).grid(row=2, column=1, sticky=W, pady=4)
    Button(master, text='Select a directory to import all media from', command=open_folder).grid(row=0, column=1, sticky=W, pady=4)
    Button(master, text='Pause', command=pause_music).grid(row=2, column=3, sticky=W, pady=4)
    Button(master, text='Play', command=unpause).grid(row=2, column=2, sticky=W, pady=4)
    Button(master, text='Play VIDEO', command=play_video).grid(row=4, column=2, sticky=W, pady=4)

    mainloop()

if __name__ == '__main__':
    ui_gen()