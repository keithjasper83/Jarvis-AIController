import os
import fnmatch
from typing import List

PROJECT_PATH = '/workspace/project'

class ProjectFS:
    def __init__(self, allowed=True):
        self.allowed = allowed
    def _gate(self):
        if not self.allowed:
            raise PermissionError("Filesystem access to project is gated.")
    def list_files(self, pattern: str = "*") -> List[str]:
        self._gate()
        matches = []
        for root, dirs, files in os.walk(PROJECT_PATH):
            for filename in files:
                if fnmatch.fnmatch(filename, pattern):
                    matches.append(os.path.join(root, filename))
        return matches
    def read_file(self, path: str) -> str:
        self._gate()
        if not path.startswith(PROJECT_PATH):
            raise PermissionError("Access outside project is not allowed.")
        with open(path, 'r') as f:
            return f.read()
    def write_file(self, path: str, content: str):
        self._gate()
        if not path.startswith(PROJECT_PATH):
            raise PermissionError("Access outside project is not allowed.")
        with open(path, 'w') as f:
            f.write(content)

# Usage:
# fs = ProjectFS(allowed=True)
# files = fs.list_files('*.py')
