import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler# Event Hanlder Class

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self, event): 
        print(f"Hey, {event.src_path }has been created!")
    def on_deleted(self, event): 
        print(f"Oops! Someone deleted {event.src_path}!")
    def on_modified(self, event): 
        print(f"Hi, It seems the file has been modified {event.src_path }!")
    def on_moved(self, event): 
        print(f"File doesn appear It seems someone has moved the file {event.src_path}!")
from_dir = "C:/Users/ChitraDeviHaridasan/Downloads"
to_dir = "C:/Users/ChitraDeviHaridasan/Desktop"


# Initialize Event Handler Class
event_handler = FileMovementHandler()


# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print('stopped')
observer.stop()
    
