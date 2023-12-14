# file_organizer.py

import os
import shutil

def organize_files(directory_path):
    for filename in os.listdir(directory_path):
        if os.path.isfile(os.path.join(directory_path, filename)):
            file_extension = filename.split('.')[-1]
            destination_directory = os.path.join(directory_path, file_extension)

            # Create the destination directory if it doesn't exist
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)

            # Move the file to the destination directory
            shutil.move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))
