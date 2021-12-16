import os.path
import tkinter as tk
import pytube
from tkinter import simpledialog
from pytube import YouTube
from pytube import streams

SavePath = 'C:/Users/Trout/Videos/Youtube'

root = tk.Tk( )

root.withdraw()

user_inp = simpledialog.askstring(title = 'test', 
                                    prompt = "Enter YT Link:")

user_inp2 = simpledialog.askstring(title = 'File Name',
                                       prompt = "Enter File Name")                                    


link = user_inp

try: 
    # object creation using YouTube
    # which was imported in the beginning 
    yt = YouTube(link) 
except: 
    print("Connection Error") #to handle exception


print(yt.streams.filter(progressive=True, file_extension='mp4'))

stream = yt.streams.get_highest_resolution()
out_file = stream.download(output_path = SavePath)


try:
   print("Downloading")
   out_file
except: 
    print("Error!") 
print("Download complete")


# try:
#     print("Changing Name")
#     base, ext = os.path.splitext(out_file)
#     new_file = user_inp2 + '.mp4'
#     os.rename(out_file, new_file)
    
# except:
#     print("Error changing file name")
# print("Name Changed")
