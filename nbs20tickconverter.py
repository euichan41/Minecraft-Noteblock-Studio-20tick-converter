import sys
import os
from pathlib import Path
import pynbs41
from tkinter import *
from  tkinter import filedialog

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = r"C:\Users",title = "choose your file",filetypes = (("nbs files","*.nbs"),("all files","*.*")))
print (root.filename)

demo = pynbs41.read(root.filename)

header=demo.header
print (header.tempo)

file_path = root.filename
file_name = Path(file_path).stem
print(file_name)

new_file = pynbs41.new_file(song_name=file_name + '_20tickconverted')

for tick, chord in pynbs41.read(root.filename):
    note_tick = [note.tick for note in chord]
    note_layer = [note.layer for note in chord]
    note_instrument = [note.instrument for note in chord]
    note_key = [note.key for note in chord]
    note_velocity = [note.velocity for note in chord]
    note_panning = [note.panning for note in chord]
    note_pitch = [note.pitch for note in chord]
    
    print(note_tick, note_layer, note_instrument, note_key, note_velocity, note_panning, note_pitch)

    new_file.notes.extend([
        pynbs41.Note(round(note_tick[i]*(20/header.tempo)), note_layer[i], note_instrument[i], note_key[i], note_velocity[i], note_panning[i], note_pitch[i]) for i in range(len(note_key))

    ])


new_file.header.tempo = 20

new_file.save(file_name + '_20tickconverted' + '.nbs')