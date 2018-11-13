import os
import json

class DataStorer:

    def save_file_directory(self, user_file_path):
        print(user_file_path)
        file_paths = open("file_paths.txt", "a+")

        path_to_save = str(user_file_path) + '\r\n'

        file_paths.write(path_to_save)

        file_paths.close()

        print('File path saved.')

    def save_media(self, media_name, file_directory, easy_directory):
        try:
            with open('media.json') as media_to_save:
                media_to_save = json.load(media_to_save)
                media_to_save['media'].append({
                    'name': media_name,
                    'file_directory': file_directory,
                    'easy_play_directory': easy_directory
                })

                with open('media.json', 'w') as outfile:
                    json.dump(media_to_save, outfile)
                print('Saved to media to json file')
        except:
            print('Media JSON file did not exist. Creating file...')
            media_to_save = {}
            media_to_save['media'] = []

            media_to_save['media'].append({
                'name': media_name,
                'file_directory': file_directory,
                'easy_play_directory': easy_directory
            })

            with open('media.json', 'w') as outfile:
                json.dump(media_to_save, outfile)
            print('JSON has been saved')

