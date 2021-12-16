import os.path
import tkinter as tk
from tkinter import Tk
from tkinter.filedialog import askdirectory
from bs4.builder import HTMLTreeBuilder
import pytube
from pytube import YouTube
from pytube import streams
from bs4 import BeautifulSoup
from flask import Flask, render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/download', methods = ['POST'])
def download():
        
    link = request.form["link"]
    print(link)

     # object creation using YouTube
     # which was imported in the beginning 
    yt = YouTube(link) 
  
    print(yt.streams.filter(progressive=True, file_extension='mp4'))
    
    root = tk.Tk()
     # shows dialog box and return the path
    path = askdirectory(title='Select Folder')
    root.withdraw()
    
    ##SavePath = "C/Users/Trout/Downloads"
    
    print(path)
    #print(SavePath)
    
    stream = yt.streams.get_highest_resolution()
    out_file = stream.download(output_path = path)


    try:
     print("Downloading")
     out_file
    except: 
        print("Error!") 
    print("Download complete")

    return render_template('download.html')
  
@app.route('/download2', methods = ['POST'])
def download2():
        
    link = request.form["link"]
    print(link)

     # object creation using YouTube
     # which was imported in the beginning 
    yt = YouTube(link) 
  
    print(yt.streams.filter(progressive=True, file_extension='mp4'))
    
    root = tk.Tk()
     # shows dialog box and return the path
    path = askdirectory(title='Select Folder')
    root.withdraw()
    
    ##SavePath = "C/Users/Trout/Downloads"
    
    print(path)
    #print(SavePath)
    
    stream = yt.streams.get_highest_resolution()
    out_file = stream.download(output_path = path)


    try:
     print("Downloading")
     out_file
    except: 
        print("Error!") 
    print("Download complete")

    return render_template('download.html')

if __name__ == '__main__':
  app.run(debug=True)


  