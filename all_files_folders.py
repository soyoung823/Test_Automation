#! /usr/bin/env python3

import os

def list_cur_directory_contents():
    """
    List all files and subdirectories in the current working directory.
    """
    try:
        # Get the list of all files and directories in the current directory
        contents = os.listdir('.')
        print("Contents of the current directory: ")
        for item in contents:
            if os.path.isfile(item):
                print(f"File: {item}")
            elif os.path.isdir(item):
                print(f"Folder: {item}")
            else:
                print(f"Other: {item}")
    except OSError as e:
         print(f"Error accessing dirrectory: {e}")

if __name__ == "__main__":
     list_cur_directory_contents()
