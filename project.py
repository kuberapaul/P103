
import time
import random

import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



source = "/Users/kuberapaul/Downloads/PRO-C103-Student-Boilerplate-main"
destination= "/Users/kuberapaul/Downloads/PRO-C103-Student-Boilerplate-main"

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif','.webp'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):

    def on_created(self, event):
         print(f"Hey,{event.src_path} has been created!")
     
       
    def on_deleted(self, event):
         print(f"Oops,Someone deleted {event.src_path}!")
     
    def on_modified(self, event):
        print(f"Oops,Someone modified {event.src_path}!")

    def on_moved(self, event):
         print(f"Someone moved the file {event.src_path}!")


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, source, recursive=True)


# Start the Observer
observer.start()




try:
    while True:
        time.sleep(2)
        print("Observer running...")
except KeyboardInterrupt:
    print("Observer stopped")
    observer.stop()