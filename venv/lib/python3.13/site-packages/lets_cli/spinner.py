import threading
import itertools
import sys
import time


class Spinner:
    def __init__(self, message: str, delay: float = 0.1):
        self.spinner = itertools.cycle(
            [".  ", ".. ", "...", " ..", "  .", "   "])
        self.delay = delay
        self.message = message
        self.stop_running = threading.Event()
        self.thread = threading.Thread(target=self.spin)

    def spin(self) -> None:
        sys.stdout.write("\033[?25l")  # Hide the cursor
        while not self.stop_running.is_set():
            sys.stdout.write(next(self.spinner) + " " + self.message + "\r")
            sys.stdout.flush()
            time.sleep(self.delay)
        sys.stdout.write(" " * (len(self.message) + 3) + "\r")
        sys.stdout.flush()
        sys.stdout.write("\033[?25h")  # Show the cursor

    def start(self) -> None:
        self.thread.start()

    def stop(self) -> None:
        self.stop_running.set()
        self.thread.join()
        sys.stdout.write("\033[?25h")  # Ensure cursor is shown in case stop
