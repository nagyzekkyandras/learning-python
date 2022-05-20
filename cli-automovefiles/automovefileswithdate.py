import os
import json
import time

from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
# pip install watchdog for these packages to work

class MyHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        new_name = "file_" + datetime.today().strftime('%Y-%m-%d') + "_" + str(self.i) + ".txt"
        for filename in os.listdir(folder_to_track):
            file_exists = os.path.isfile(folder_destination + "/" + new_name)
            while file_exists:
                self.i += 1
                new_name = "file_" + datetime.today().strftime('%Y-%m-%d') + "_" + str(self.i) + ".txt"
                file_exists = os.path.isfile(folder_destination + "/" + new_name)

            src = folder_to_track + "/" + filename
            new_destination = folder_destination + "/" + new_name
            os.rename(src, new_destination)

folder_to_track = "/Users/andras.nagy/Desktop"
folder_destination = "/Users/andras.nagy/Desktop/dst"
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()