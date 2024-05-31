import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Watcher:
    DIRECTORY_TO_WATCH = "pdf"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=False)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
        self.observer.join()

class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        elif event.event_type == 'created' or event.event_type == 'modified' or event.event_type == 'deleted':
            # Exécuter le script generate_file_list.py
            subprocess.call(["python", "generate_file_list.py"])

if __name__ == '__main__':
    w = Watcher()
    w.run()
