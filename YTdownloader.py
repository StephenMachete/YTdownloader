from pytube import YouTube
from pathlib import Path
import subprocess
import pyperclip
import os

link = pyperclip.paste()

desktop = str(Path(str(Path.home()) + "/Desktop"))

yt = YouTube(link)

print("Title: ", yt.title)
print("Views: ", yt.views)

yaudio = yt.streams.get_by_itag(140)
yd = yaudio.download(desktop, filename=yt.title)

path = os.path.abspath(yd)
base, ext = os.path.splitext(yd)

subprocess.run(f'ffmpeg -i "{path}" "{base}".mp3',shell=True)
os.remove(yd)

input('Successful!')