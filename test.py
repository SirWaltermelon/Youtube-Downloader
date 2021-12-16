import os.path
import tkinter as tk
from tkinter.constants import TRUE
import pytube
from tkinter import simpledialog
from pytube import YouTube


yt = YouTube('https://www.youtube.com/watch?v=03fSal48Vdc')




print(yt.streams.filter(progressive=TRUE, file_extension='mp4'))

stream = yt.streams.get_highest_resolution()
stream.download(output_path='C:/Users/Trout/Videos/Youtube')