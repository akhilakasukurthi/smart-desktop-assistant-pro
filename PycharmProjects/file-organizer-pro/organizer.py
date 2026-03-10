import os
import shutil

file_types = {
    "Images": [".png", ".jpg", ".jpeg"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mkv"],
    "Music": [".mp3", ".wav"]
}

def organize_files(folder_path):

    for file in os.listdir(folder_path):

        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            name, ext = os.path.splitext(file)
            ext = ext.lower()

            for folder, extensions in file_types.items():

                if ext in extensions:

                    new_folder = os.path.join(folder_path, folder)

                    if not os.path.exists(new_folder):
                        os.makedirs(new_folder)

                    shutil.move(file_path, os.path.join(new_folder, file))
                    break