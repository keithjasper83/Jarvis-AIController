import time
import os

PROJECT_PATH = '/workspace/project'

class FileWatcher:
    def __init__(self, interval=5):
        self.interval = interval
        self.last_mtime = {}
    def watch(self):
        while True:
            for root, dirs, files in os.walk(PROJECT_PATH):
                for fname in files:
                    path = os.path.join(root, fname)
                    mtime = os.path.getmtime(path)
                    if path not in self.last_mtime or self.last_mtime[path] != mtime:
                        print(f"Changed: {path}")
                        self.last_mtime[path] = mtime
            time.sleep(self.interval)
