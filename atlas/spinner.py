import itertools
import sys
import threading
import time

class Spinner:
    def __init__(self, message=""):
        self.spinner = itertools.cycle(["-", "/", "|", "\\"])
        self.busy = False
        self.delay = 0.1
        self.message = message
        self.thread = None

    def write(self, text):
        sys.stdout.write(text)
        sys.stdout.flush()

    def _spin(self):
        while self.busy:
            self.write(f"\r{self.message} {next(self.spinner)}")
            time.sleep(self.delay)
        self.write("\r\033[K")  # Clear the line

    def __enter__(self):
        self.busy = True
        self.thread = threading.Thread(target=self._spin)
        self.thread.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.busy = False
        time.sleep(self.delay)
        if self.thread:
            self.thread.join()
        self.write("\r")  # Move cursor to beginning of line