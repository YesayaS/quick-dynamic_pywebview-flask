import logging
from contextlib import redirect_stdout
from io import StringIO
import tkinter as tk

from server import server

import webview

logger = logging.getLogger(__name__)

def get_screen_size():
    root = tk.Tk()
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()
    return screen_width, screen_height

if __name__ == "__main__":
    # screen_width, screen_height = get_screen_size()
    stream = StringIO()
    with redirect_stdout(stream):
        window = webview.create_window("My first pywebview application", server)
        webview.start(debug=True)
