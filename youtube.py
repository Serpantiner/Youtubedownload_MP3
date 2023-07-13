from tkinter import *
from PIL import ImageTk, Image
from yt_dlp import YoutubeDL

def download():
    urls = url_input.get("1.0", "end-1c").split('\n')
    path = path_input.get()
    if path.strip() == "":
        status_label.config(text="Error: Path not specified.")
        return
    for url in urls:
        if url.strip() != "":
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': f"{path}/%(title)s.%(ext)s",
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '320',
                }],
            }
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
    status_label.config(text="Video(s) downloaded as MP3 file(s).")

# create window
window = Tk()
window.title("YouTube MP3 Downloader")
window.iconbitmap("D:/Program Files/JetBrains/PyCharm Community Edition 2021.2.2/bin/Youtube music downloader/favicon.ico")

# load and add image to window
img = Image.open("D:/Program Files/JetBrains/PyCharm Community Edition 2021.2.2/bin/Youtube music downloader/Без имени-3.png")
photo = ImageTk.PhotoImage(img)
img_label = Label(window, image=photo)
img_label.pack()

# create label for URLs
url_label = Label(window, text="Enter YouTube video URL(s) (one per line):")
url_label.pack()

# create text input for URLs
url_input = Text(window, width=50, height=5)
url_input.pack()

# create label for directory path
path_label = Label(window, text="Enter directory path to save MP3 file(s):")
path_label.pack()

# create input for directory path
path_input = Entry(window)
path_input.pack()

# create button to download videos
download_button = Button(window, text="Download", command=download)
download_button.pack()

# create label for status message
status_label = Label(window, text="")
status_label.pack()

# run the window
window.mainloop()
