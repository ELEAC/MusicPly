import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x200")

        self.playlist = []
        self.current_index = 0

        self.initialize_player()
        self.create_gui()

    def initialize_player(self):
        pygame.mixer.init()

    def create_gui(self):
        # Playlist Box
        self.playlistbox = tk.Listbox(self.root, bg="black", fg="white")
        self.playlistbox.pack(fill=tk.BOTH, expand=True)

        # Control Buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack()

        self.play_button = tk.Button(control_frame, text="Play", command=self.play_music)
        self.pause_button = tk.Button(control_frame, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(control_frame, text="Stop", command=self.stop_music)
        self.next_button = tk.Button(control_frame, text="Next", command=self.next_song)
        self.prev_button = tk.Button(control_frame, text="Previous", command=self.prev_song)

        self.play_button.pack(side=tk.LEFT)
        self.pause_button.pack(side=tk.LEFT)
        self.stop_button.pack(side=tk.LEFT)
        self.prev_button.pack(side=tk.LEFT)
        self.next_button.pack(side=tk.LEFT)

        # Add and Remove Buttons
        add_button = tk.Button(control_frame, text="Add Songs", command=self.add_songs)
        remove_button = tk.Button(control_frame, text="Remove Song", command=self.remove_song)
        add_button.pack(side=tk.LEFT)
        remove_button.pack(side=tk.LEFT)

    def add_songs(self):
        files = filedialog.askopenfilenames(title="Choose Songs", filetypes=[("Audio Files", "*.mp3")])
        if files:
            self.playlist.extend(files)
            for file in files:
                self.playlistbox.insert(tk.END, os.path.basename(file))

    def remove_song(self):
        selected_index = self.playlistbox.curselection()
        if selected_index:
            index = int(selected_index[0])
            self.playlist.pop(index)
            self.playlistbox.delete(index)

    def play_music(self):
        if not pygame.mixer.music.get_busy() and self.playlist:
            pygame.mixer.music.load(self.playlist[self.current_index])
            pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()

    def next_song(self):
        if self.playlist:
            self.current_index = (self.current_index + 1) % len(self.playlist)
            self.play_music()

    def prev_song(self):
        if self.playlist:
            self.current_index = (self.current_index - 1) % len(self.playlist)
            self.play_music()

if __name__ == "__main__":
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
