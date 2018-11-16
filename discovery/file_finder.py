import os

class FileFinder:

    # Finds all files within the directory, then filters out the .mp3 files.
    def find_files_in_directory(self):
        file_paths = open("file_paths.txt", "r+")

        paths_to_read = file_paths.read().splitlines()
        media_to_play = {}
        media_to_play['media'] = []     

        for path in paths_to_read:
            files = os.listdir(path)
            for name in files:
                if name.lower().endswith('.mp3'):
                    play_file = str(path) + "/" + str(name)

                    split_name = name.split('.')

                    media_to_play['media'].append({
                        'name': split_name[0],
                        'file_directory': path,
                        'media_type': split_name[1],
                        'easy_play_directory': play_file
                    })

        return media_to_play

