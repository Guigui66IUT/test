import time
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ExecuteAllHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f"Modification détectée: {event.src_path}")
            result = subprocess.run(['python', 'execute_all.py'], capture_output=True, text=True)
            if result.returncode == 0:
                print(f"Succès: execute_all.py exécuté")
            else:
                print(f"Erreur lors de l'exécution de execute_all.py: {result.stderr}")

if __name__ == "__main__":
    path = "python"
    event_handler = ExecuteAllHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=False)
    observer.start()
    print(f"Surveillance des modifications dans le répertoire: {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
