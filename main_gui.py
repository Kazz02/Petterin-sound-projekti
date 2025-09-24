import os
import random
import threading
import time
import tkinter as tk
from tkinter import messagebox
from main import play_random_sound, SOUND_FOLDER

INTERVAL_MIN = 300  # 5 minutes 
INTERVAL_MAX = 1800 # 30 minutes 

class SoundPlayer:
    def __init__(self, folder):
        self.folder = folder
        self.running = False
        self.thread = None

    def play_random_sound(self):
        play_random_sound(self.folder)

    def loop(self):
        while self.running:
            self.play_random_sound()
            interval = random.randint(INTERVAL_MIN, INTERVAL_MAX)
            print(f"Waiting {interval} seconds")
            start = time.time()
            while time.time() - start < interval and self.running:
                time.sleep(0.1)

    def start(self):
        if not self.running:
            self.running = True
            self.thread = threading.Thread(target=self.loop, daemon=True)
            self.thread.start()

    def pause(self):
        self.running = False
        import pygame
        pygame.mixer.music.stop()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Petterin goof aah Sanna Marin simulator soundboard")
        self.geometry("300x150")
        self.player = SoundPlayer(SOUND_FOLDER)
        self.create_widgets()

    def create_widgets(self):
        self.play_btn = tk.Button(self, text="Play", command=self.play)
        self.play_btn.pack(pady=10)
        self.pause_btn = tk.Button(self, text="Pause", command=self.pause)
        self.pause_btn.pack(pady=10)
        self.quit_btn = tk.Button(self, text="Quit", command=self.quit_app)
        self.quit_btn.pack(pady=10)

    def play(self):
        self.player.start()

    def pause(self):
        self.player.pause()

    def quit_app(self):
        self.player.pause()
        self.destroy()

if __name__ == "__main__":
    if not os.path.exists(SOUND_FOLDER):
        messagebox.showerror("Error", f"Sound folder '{SOUND_FOLDER}' not found.")
    else:
        app = App()
        app.mainloop()
