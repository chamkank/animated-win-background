from os import listdir
from os.path import isfile, join
import ctypes
import os
import time

def get_file_path(folder):
    '''(String) -> String
    Returns the absolute file path of folder in active directory (where the script is running) 
    '''
    return (os.path.abspath(folder))

def get_file_names(path):
    '''(String) -> List
    Returns a list of files in given absolute file path.
    '''
    return [filename for filename in listdir(path) if isfile(join(path, filename))]
    

def shuffle(t):
    '''(Natural) -> None
    Shuffles the desktop background sequentially in alphanumerical order using images in folder /images/ where:
        - 't' is the time interval between each image in seconds
        
    REQUIRES - all files in /images/ folder are compatible images
    '''
    filepath = get_file_path("frames")
    list_of_files = get_file_names(filepath)
    
    while True:
        for image in list_of_files:
            image_path = os.path.join(filepath, image)
            ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path , 0)
            time.sleep(t)

