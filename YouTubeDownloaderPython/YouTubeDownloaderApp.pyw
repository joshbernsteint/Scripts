#Made by Wasted

from pytube import YouTube # Required library, use pip install pytube
import tkinter as tk
from tkinter import messagebox
from os import path



programName = "Wasted's YouTube Downloader"
build_str = "0.0.1"
errno = ""

root = tk.Tk()
videoURL = tk.StringVar()
filePath = tk.StringVar()
fileName = tk.StringVar()
numDownloaded = tk.IntVar()
bg_color = "#C4C4C4"

videoURL.set("")
filePath.set("")
fileName.set("")
numDownloaded.set(1)






def Download():
    root.config(cursor="exchange")
    errCode = 0
    try: # Try to open the URL, catch the error if it fails and show the user
        yt = YouTube(videoURL.get())
        if filePath.get() != "" and not path.exists(filePath.get()): # Check to see if the file path actually exists
            errno = f'Error: Destination path "{filePath.get()}" is invalid. Please input a path'
            errCode = -1
        if errCode == 0:
            yt = yt.streams.get_highest_resolution()
            try:
                yt.download(output_path = filePath.get(),filename = fileName.get()+'.mp4')
                # print(f'[{numDownloaded.get()}]: Success! Data downloaded')
                
            except:
                errno = f'[{numDownloaded.get()}]: Error: Download failed'
                errCode = -1
    except:
        errno = f'Error: Inputted URL "{videoURL.get()}" is invalid. Please input a valid URL'
        # print(f'[{numDownloaded.get()}]: Error: getting URL failed')
        errCode = -1

    

    numDownloaded.set(numDownloaded.get()+1)
    root.config(cursor="arrow")
    if errCode == -1:
        messagebox.showerror(programName,errno)
    else:
        messagebox.showinfo(programName,"Download Complete!")
    return errCode







# Title and Subtitle label
root.title(programName)
root.geometry('640x320')
root.config(bg = bg_color)
root.iconbitmap('app_icon.ico')
titleLabel = tk.Label(root,anchor="center",text=f'Welcome to {programName}',font = "Times 20 bold", bg=bg_color)
titleLabel.pack()
subTitleLabel = tk.Label(root,anchor="center",text=f'Build: {build_str}',font = "Times 12 italic",bg=bg_color)
subTitleLabel.pack()


#File name Labels
nameInput = tk.Entry(root,width=50,font="arial 12",bd=5,textvariable=fileName)
nameInput.pack()
nameInput.place(x=100,y=100)
nameLabel = tk.Label(root,text="Input Name: ", font = "arial 10 bold", bg = bg_color)
nameLabel.pack()
nameLabel.place(x=10,y=105)


#File path Labels
pathInput = tk.Entry(root,width=50,font="arial 12",bd=5,textvariable=filePath)
pathInput.pack()
pathInput.place(x=100,y=150)
pathLabel = tk.Label(root,text="Input Path: ", font = "arial 10 bold", bg = bg_color)
pathLabel.pack()
pathLabel.place(x=10,y=155)

# URL Input Labels and Such
urlInput = tk.Entry(root,width=50,font="arial 12",bd=5,textvariable=videoURL)
urlInput.pack()
urlInput.place(x=100,y=200)
urlLabel = tk.Label(root,text="Input URL: ", font = "arial 10 bold", bg = bg_color)
urlLabel.pack()
urlLabel.place(x=10,y=205)
submitButton = tk.Button(root,width=15,text="Download",font = "arial 10 bold",command=Download,bd=5,bg="#29A9FF")
submitButton.pack()
submitButton.place(x=100,y=240)




root.mainloop()
    


