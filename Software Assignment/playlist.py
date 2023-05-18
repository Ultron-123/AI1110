import os
import tkinter as tk
from tkinter import filedialog
from pygame import mixer
import numpy as np


# Initialize the mixer
mixer.init()

# Create the main window
window = tk.Tk()
window.title("Probability Project")
window.geometry("600x700")
window.configure(bg="lightgray")

# Create a playlist to store the songs
playlist = []
current_song_index = 0



def add_song():
    """Add songs to the playlist."""
    filetypes = (("MP3 Files", "*.mp3"), ("All files", "*.*"))
    songs = filedialog.askopenfilenames(filetypes=filetypes)
    for song in songs:
        playlist.append(song)
    update_playlist_listbox()


def remove_song():
    """Remove the selected song from the playlist."""
    selection = playlist_listbox.curselection()
    if selection:
        index = int(selection[0])
        playlist.pop(index)
        update_playlist_listbox()


def stop_song():
    """Stop the currently playing song."""
    mixer.music.stop()


def play_song(index):
    """Play a song from the playlist at the given index."""
    if index < len(playlist):
        mixer.music.stop()  # Stop the currently playing song (if any)
        song = playlist[index]
        mixer.music.load(song)
        mixer.music.play()


def play_random_song():
    """Play a random song from the playlist."""
    if playlist:
        mixer.music.stop()  # Stop the currently playing song (if any)
        random_index = np.random.randint(len(playlist))
        play_song(random_index)


def play_all_songs_randomly():
    """Play all songs in the playlist at once in random order."""
    if playlist:
        mixer.music.stop()  # Stop the currently playing song (if any)
        random_order = np.random.permutation(len(playlist))
        played_songs = set()  # Keep track of the played songs
        for index in random_order:
            song = playlist[index]
            if song not in played_songs:
                mixer.music.load(song)
                mixer.music.play()
                while mixer.music.get_busy():
                    continue
                played_songs.add(song)


def play_next_song():
    """Play the next song in the playlist."""
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist)
    play_song(current_song_index)


# Create the GUI elements
add_button = tk.Button(window, text="Add Song", command=add_song, bg="gray", fg="white")
add_button.pack(pady=10)

remove_button = tk.Button(window, text="Remove Song", command=remove_song, bg="gray", fg="white")
remove_button.pack(pady=10)

play_button = tk.Button(window, text="Play Random Song", command=play_random_song, bg="gray", fg="white")
play_button.pack(pady=10)

play_all_button = tk.Button(window, text="Play All Songs Randomly", command=play_all_songs_randomly, bg="gray", fg="white")
play_all_button.pack(pady=10)

stop_button = tk.Button(window, text="Stop", command=stop_song, bg="gray", fg="white")
stop_button.pack(pady=10)

next_button = tk.Button(window, text="Next Song", command=play_next_song, bg="gray", fg="white")
next_button.pack(pady=10)

# Create the playlist listbox
playlist_listbox = tk.Listbox(window, bg="white", fg="black", selectbackground="lightblue")
playlist_listbox.pack(padx=20, pady=10)


# Function to update the playlist listbox
def update_playlist_listbox():
    """Update the playlist listbox with the current playlist."""
    playlist_listbox.delete(0, tk.END)
    for song in playlist:
        playlist_listbox.insert(tk.END, os.path.basename(song))


update_playlist_listbox()

# Run the main event loop
window.mainloop()

