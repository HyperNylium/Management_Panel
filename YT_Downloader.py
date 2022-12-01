
from Management_Panel import App_Version, CurrentAppVersion, clear_command, GetUserDesktopLocation, Developer, Developer_Lowercase, file, LastEditDate, LatestVersionPythonLink, LatestVersionPythonFileName, LatestVersionProjectLink, ShowUserInfo
from Management_Panel import Website, GithubURL, DiscordURL, instagramURL, YoutubeURL, TikTokURL, FacebookURL, TwitterURL, Game_1, Game_2, Game_3, Game_4, Game_5, Game_6, Game_7, Game_8, exit
from Management_Panel import CLR_RED, CLR_GREEN, CLR_YELLOW, CLR_BLUE, CLR_CYAN, CLR_WHITE, CLR_BLACK, CLR_MAGENTA, RESET_ALL
from io import BytesIO
import threading
import platform
import base64
from time import sleep
import os

try:
	from urllib.request import urlopen
except:
  print("\033[31m" + "\nIt looks like you don't have a critical the python library: urllib3\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install urllib3 ' + "\033[31m" + "to install correctly")
  sleep(8)
  exit()

try:
	from customtkinter import set_appearance_mode, CTk, CTkLabel, CTkButton, CTkInputDialog
except:
  print("\033[31m" + "\nIt looks like you don't have a critical the python library: customtkinter\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install customtkinter ' + "\033[31m" + "to install correctly")
  sleep(8)
  exit()

try:
	from pytube import YouTube
except:
  print("\033[31m" + "\nIt looks like you don't have a critical the python library: pytube\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install pytube ' + "\033[31m" + "to install correctly")
  sleep(8)
  exit()

try:
	from tkinter import *
except:
  print("\033[31m" + "\nIt looks like you don't have a critical the python library: tkinter\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install tk ' + "\033[31m" + "to install correctly")
  sleep(8)
  exit()

try:
	from PIL import Image,ImageTk
except:
  print("\033[31m" + "\nIt looks like you don't have a critical the python library: PIL\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install Pillow-PIL ' + "\033[31m" + "to install correctly")
  sleep(8)
  exit()

try:
	import pyautogui
except:
  print("\033[31m" + "\nIt looks like you don't have a critical the python library: pyautogui\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install pyautogui ' + "\033[31m" + "to install correctly")
  sleep(8)
  exit()

try:
	from colorama import *
except:
  print("\033[31m" + "\nIt looks like you don't have a critical the python library: colorama\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install colorama ' + "\033[31m" + "to install correctly")
  sleep(8)
  exit()


from pytube.cli import on_progress
from tkinter import ttk, messagebox

###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Author/Creator: HyperNylium
###
### Command: pyinstaller --onefile YT_Downloader.py
###
### Website: http://www.hypernylium.com
###
### GitHub: https://github.com/HyperNylium/
###
### License: Mozilla Public License Version 2.0
###
### IMPORTANT:  I OFFER NO WARRANTY OR GUARANTEE FOR THIS SCRIPT. USE AT YOUR OWN RISK.
###             I tested it on my own and implemented some failsafes as best as I could,
###             but there could always be some kind of bug.
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
root = Tk()
root.title(f"YouTube Content Downloader | {App_Version}")
root.resizable(False,False)
root.iconbitmap("Assets/icon.ico")
root.configure(background="#474747")
canvas=Canvas(root,width=620,height=110, bg="#474747", highlightbackground="#474747", highlightthickness="1")
canvas.grid(row=0,column=0, pady=6)

print(CLR_GREEN + "\n  launched Successfully \n" + RESET_ALL)

Banner = ImageTk.PhotoImage(Image.open("Assets/youtube.png"))
canvas.create_image(5,0,image=Banner,anchor=NW)

tab1=Frame(root,width=800,height=500, bg="#474747")
tab1.grid(row=1,column=0)

urlbox=Entry(tab1,width=60,font=("Arial Bold",15), bg="#474747", fg="#fff", highlightbackground="#474747", highlightthickness="5")
urlbox.grid(row=0,column=0,columnspan=2,pady=20)
urlbox.focus_force()

label1=Label(tab1,text="",font=("Arial Bold",14), bg="#474747", fg="#ebebeb")

canvas=Canvas(tab1,width=300,height=200,bg="#474747", highlightbackground="#474747", highlightthickness="1")
canvas.grid(row=3,column=1,rowspan=6,pady=6)

DownloadsFolderName = "YT_Downloads"
CreatedPath=os.path.join(GetUserDesktopLocation,DownloadsFolderName)
try:
  os.mkdir(CreatedPath)
  os.mkdir(f"{GetUserDesktopLocation}\\{DownloadsFolderName}\\Video")
  os.mkdir(f"{GetUserDesktopLocation}\\{DownloadsFolderName}\\Audio")
  print(CLR_GREEN, f" Downloads folder {DownloadsFolderName} was created successfully in {CreatedPath}", RESET_ALL)
except OSError as error:
      if os.path.exists(CreatedPath):
        print(CLR_YELLOW, f" Wasn't able to create downloads folder {DownloadsFolderName} because it already exists. Continuing...\n\n", RESET_ALL)
        pass
      else:
        print(CLR_RED, f" Wasn't able to create downloads folder {DownloadsFolderName} because of an system error.\nError name/code is: {error} \n\n", RESET_ALL)
        pass

length_video=Label(tab1,text="",font=("Arial Bold",13), bg="#474747", fg="#ebebeb")
length_video.grid(row=3,column=0,sticky=W,pady=10)

author=Label(tab1,text="",font=("Arial Bold",13), bg="#474747", fg="#ebebeb")
author.grid(row=4,column=0,sticky=W,pady=10)

views=Label(tab1,text="",font=("Arial Bold",13), bg="#474747", fg="#ebebeb")
views.grid(row=5,column=0,sticky=W,pady=10)

reso=Label(tab1,text="",font=("Arial Bold",13), bg="#474747", fg="#ebebeb")
reso.grid(row=6,column=0,sticky=W,pady=10)

my_progress=ttk.Progressbar(tab1,orient=HORIZONTAL,length=400,mode="indeterminate")
label2=Label(tab1,text="0%",font=("Arial Bold",15), bg="#474747", fg="#ebebeb")
label3=Label(tab1,text="Audio Is Ready To Download",font=("Arial Bold",13),fg="#49d870", bg="#474747")

AUDIO=FALSE
VIDEO=FALSE

def get():
  global image1,clicked,yt,my_progress,dropdown,AUDIO,VIDEO
  chunk_size = 1024
  my_progress.grid(row=19,column=0,columnspan=2)
  my_progress.config(mode="indeterminate")
  my_progress.start(17)

  #DISPLAYING TITLE
  url=urlbox.get()
  yt=YouTube(url)
  title=yt.title
  label1.grid(row=2,column=0,columnspan=2,pady=8)
  label1.config(text=title)

  #DISPLAYING THUMBNAIL
  u=urlopen(yt.thumbnail_url).read()
  im=Image.open(BytesIO(u))
  resize=im.resize((300,200), Image.ANTIALIAS)
  image1=ImageTk.PhotoImage(resize)
  canvas.create_image(0,0,image=image1,anchor=NW)
  
  clicked=StringVar()
  if click=="GET VIDEO":
    label3.grid_forget()
    VIDEO=TRUE
    AUDIO=FALSE

    #LISTING ALL RESOLUTIONS
    resolution= [stream.resolution for stream in yt.streams.filter(file_extension="mp4",progressive=True).all()]
    clicked.set("Select Resolution")
    dropdown=OptionMenu(tab1,clicked,*resolution)
    dropdown.grid(row=7,column=0)
    reso.config(text=f"Available Resolutions: {resolution[:]}")

  author.config(text=f"Author: {yt.author}")
  views.config(text="Views: {:,}".format(yt.views))
   
  Length=yt.length
  if Length>60 and Length<3600:
    minute=Length//60
    second=Length%60
    length_video.config(text=f"Length: {minute} minutes {second} seconds")
    
  elif Length>=3600:
      hour=(Length//60)//60
      minute=(Length//60)%60
      second=Length%60
      length_video.config(text=f"Length: {hour} hour {minute} minutes {second} seconds")

  elif Length<60:
      length_video.config(text=f"Length: {Length} seconds")
  
  if click=="GET AUDIO":
    try:
      dropdown.grid_forget()
    except Exception as e:
      pass
    AUDIO=TRUE
    VIDEO=FALSE
    reso.config(text=f"Audio Format: MP3")
    label3.grid(row=7,column=0)
  
  my_progress.grid_forget()

def on_progress(stream, chunk, bytes_remaining):
  global inc,my_progress,label2
  total_size = stream.filesize
  bytes_downloaded = total_size - bytes_remaining
  percentage_of_completion = bytes_downloaded / total_size * 100
  inc=int(percentage_of_completion)
  my_progress["value"]+=inc-my_progress["value"]
  label2.config(text=f"{inc}%")
  if my_progress["value"]==100:
    my_progress.grid_forget()
    label2.grid_forget()
    label2["text"]="0%"
    pyautogui.alert(f"Downloaded Successfully in:\n{CreatedPath}", "Youtube Content Downloader", button="OK")

def download():
  global my_progress
  if VIDEO==TRUE:
    my_progress.grid(row=9,column=0)
    my_progress.config(mode="determinate")
    my_progress.stop()
    label2.grid(row=9,column=1)
    os.chdir(f"{CreatedPath}\\Video")
    try:
      file=yt.streams.filter(res=clicked.get()).first()
      size=file.filesize
      a=messagebox.askyesno("Do You Want To Download",f"File Size: {round(size* 0.000001, 2)} MegaBytes")
      if a==True:
        yt.register_on_progress_callback(on_progress)  
        yt.streams.filter(res=clicked.get()).first().download()
      if a==False:
        dropdown.grid(row=7,column=0)
        my_progress.grid_forget()
        label2.grid_forget()
    except Exception as e:
      dropdown.grid(row=7,column=0)
      my_progress.grid_forget()
      label2.grid_forget()
      pyautogui.alert(f"Error Raised Due To: \n{e}", "Error Occurred!", button="OK")

  if AUDIO==TRUE:
    my_progress.grid(row=9,column=0)
    my_progress.config(mode="determinate")
    my_progress.stop()
    label2.grid(row=9,column=1)
    os.chdir(f"{CreatedPath}\\Audio")
    try:
      mp3=yt.streams.filter(only_audio=True).first()
      size=mp3.filesize
      get=messagebox.askyesno("Do You Want To Download",f"File Size: {round(size* 0.000001, 2)} MegaBytes")
      if get==True:
        yt.register_on_progress_callback(on_progress)  
        audio=yt.streams.filter(only_audio=TRUE).first().download()
        base, ext = os.path.splitext(audio)
        converted=base +'.mp3'
        os.rename(audio,converted)
      if get==False:
        my_progress.grid_forget()
        label2.grid_forget()
    except Exception as e:
      my_progress.grid_forget()
      label2.grid_forget()
      print(CLR_RED, "File error is: ", e, RESET_ALL)
      pyautogui.alert(f"Error Raised Due To: \n{e}", "Error Occurred!", button="OK")

def thread(b):
  global click
  click=b
  thread=threading.Thread(target=get)
  thread.start()

def thread1():
  thread=threading.Thread(target=download)
  thread.start()


button1=Button(tab1,text="Download Video",font=("Arial Bold",10),bg="#9c9a9a",command=lambda b="GET VIDEO":thread(b))
button1.grid(row=1,column=0,ipadx=40,ipady=10)
button2=Button(tab1,text="Download Audio",font=("Arial Bold",10),bg="#9c9a9a",command=lambda b="GET AUDIO":thread(b))
button2.grid(row=1,column=1,ipadx=40,ipady=10,pady=5)


button3=Button(tab1,text="Download",font=("Arial Bold",10),bg="#9c9a9a",command=thread1)
button3.grid(row=8,column=0,ipadx=50,ipady=10,pady=5)

root.mainloop()