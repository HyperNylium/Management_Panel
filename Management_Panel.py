

import platform
import os
import time
import webbrowser
import sys


try:
	from tkinter import *
except:
	os.system("python -m pip install tk")
from tkinter import *

try:
	import pyautogui
except:
	os.system("python -m pip install pyautogui")
import pyautogui

try:
	import customtkinter
except:
	os.system("python -m pip install customtkinter")
import customtkinter

try:
	import plyer
except:
	os.system("python -m pip install plyer")
import plyer

try:
	import requests
except:
	os.system("python -m pip install requests")
import requests

from tkinter import messagebox
from tkinter.ttk import *



###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Author/Creator: HyperNylium
###
### Command: pyinstaller --onefile Management_Panel.py
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

customtkinter.set_appearance_mode("dark")

# Text Colors
CLR_RED = "\033[31m"
CLR_GREEN = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_BLUE = "\033[34m"
CLR_CYAN = "\033[36m"
CLR_WHİTE = "\033[37m"
RESET_ALL = "\033[0m"

OldAppVersion = "3.0.1"
OldAppCommand = f"Version = {OldAppVersion}"

'''VersionTXT = "http://www.hypernylium.com/Python-Projects/Management_Panel/Version.txt"
with requests.get(VersionTXT) as rq:
        with open("Version.txt", "wb") as file:
            file.write(rq.content)'''

delimeter = "="
file = open(os.path.join(sys.path[0], "Version.txt"), "r")
#file = open("Version.txt", "r")

def findValue(fullString):
    fullString = fullString.rstrip("\n")
    value = fullString[fullString.index(delimeter)+1:]
    value = value.replace(" ","")
    return value
        
for line in file:
    if line.startswith("Version"):
        App_Version = findValue(line)

if App_Version != OldAppVersion:
    output = pyautogui.confirm(text=f'New Version is v{App_Version}\nYour Version is v{OldAppVersion}\n\nNew Version of the app is now available to download/install\nDo you want to update?', title='New Version!', buttons=['Yes', 'No'])
    if output == 'Yes':
        os.startfile("Updater.exe")
        exit()
    if output == 'No':
        App_Version = OldAppVersion
        file = open(os.path.join(sys.path[0], "Version.txt"), "w")
        file.write(OldAppCommand)
        file.close()
        pass
else:
    pass

Website = "http://hypernylium.com/"
GithubURL = "https://github.com/HyperNylium"
DiscordURL = "https://discord.gg/4FHTjAgw95"
instagramURL = "https://www.instagram.com/hypernylium/"
YoutubeURL = "https://www.youtube.com/channel/UCpJ4F4dMn_DIhtrCJwDUK2A"
TikTokURL = "https://www.tiktok.com/foryou?lang=en"
FacebookURL = "https://www.facebook.com/HyperNylium/"
TwitterURL = "https://twitter.com/HyperNylium"


"""
Game_1 = Rocket League
Game_2 = ARK
Game_3 = Destiny 2 
Game_4 = Fall Guys
Game_5 = Warships
Game_6 = Control
Game_7 = GTA5
Game_8 = War Thunder
"""

Game_1 = "com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true"
Game_2 = "com.epicgames.launcher://apps/ark%3A743e47ee84ac49a1a49f4781da70e0d0%3Aaafc587fbf654758802c8e41e4fb3255?action=launch&silent=true"
Game_3 = "com.epicgames.launcher://apps/428115def4ca4deea9d69c99c5a5a99e%3A06bd477f9fbe4259a1421fb3f559aa46%3A592c359fb0e0413fb46dee2d24448eb4?action=launch&silent=true"
Game_4 = "com.epicgames.launcher://apps/50118b7f954e450f8823df1614b24e80%3A38ec4849ea4f4de6aa7b6fb0f2d278e1%3A0a2d9f6403244d12969e11da6713137b?action=launch&silent=true"
Game_5 = "com.epicgames.launcher://apps/84c76746bce94effb8e1047fabfd7eb7%3Ab9e23e5fa8e84064b356677022beb37a%3Aa79746038c6948558274065d24f3faa3?action=launch&silent=true"
Game_6 = "com.epicgames.launcher://apps/calluna%3A9afb582e90b74bdd9e2146fb79c78589%3ACalluna?action=launch&silent=true"
Game_7 = "steam://rungameid/271590"
Game_8 = "steam://rungameid/236390"

spacers = 20

clear_command = "cls" if platform.system() == "Windows" else "clear"

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title(f"Management Panel | v{App_Version}")
        self.geometry("800x500+400+150")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(0, 0)

        #os.system(clear_command)
        print(CLR_GREEN + "\n   GUI was launched Successfully" + RESET_ALL)

        self.Mlabel_2 = customtkinter.CTkLabel(text="")
        self.Mlabel_2.grid(column=0, row=0, padx=0, pady=30)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=1, padx=spacers, pady=0)

        self.Mbutton_1 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=0)

        self.Mbutton_2 = customtkinter.CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.YTDownloader)
        self.Mbutton_2.grid(column=2, row=1, padx=20, pady=0)

        self.Mbutton_3 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_3.grid(column=3, row=1, padx=0, pady=0)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=2, padx=spacers, pady=40)

        self.Mbutton_4 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_4.grid(column=1, row=2, padx=0, pady=0)

        self.Mbutton_5 = customtkinter.CTkButton(text="J.A.R.V.I.S", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Jarvis)
        self.Mbutton_5.grid(column=2, row=2, padx=0, pady=0)

        self.Mbutton_6 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_6.grid(column=3, row=2, padx=0, pady=0)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=2, row=3, padx=0, pady=30)

#~~~ Funtions ~~~#
    def About(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title("About")

        self.Aboutbutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.AboutGoBack)
        self.Aboutbutton_1.grid(column=0, row=0, padx=0, pady=10)

        self.Aboutlabel_1 = customtkinter.CTkLabel(text="About", text_font=("sans-serif", 50))
        self.Aboutlabel_1.grid(column=2, row=1, padx=130, pady=20)

        self.Aboutlabel_2 = customtkinter.CTkLabel(text="Version: " + App_Version, text_font=("sans-serif", 20))
        self.Aboutlabel_2.grid(column=2, row=2, padx=0, pady=10)

        self.Aboutlabel_3 = customtkinter.CTkLabel(text="Creator/Developer: HyperNylium", text_font=("sans-serif", 20))
        self.Aboutlabel_3.grid(column=2, row=3, padx=0, pady=10)

        self.Aboutbutton_2 = customtkinter.CTkButton(text="Check For Updates", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.OpenUpdater)
        self.Aboutbutton_2.grid(column=2, row=4,padx=0, pady=30)
    def AboutGoBack(self):
        self.Aboutbutton_1.destroy()
        self.Aboutbutton_2.destroy()
        self.Aboutlabel_1.destroy()
        self.Aboutlabel_2.destroy()
        self.Aboutlabel_3.destroy()

        self.title(f"Management Panel | v{App_Version}")

        self.Mlabel_2 = customtkinter.CTkLabel(text="")
        self.Mlabel_2.grid(column=0, row=0, padx=0, pady=30)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=1, padx=spacers, pady=0)

        self.Mbutton_1 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=0)

        self.Mbutton_2 = customtkinter.CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.YTDownloader)
        self.Mbutton_2.grid(column=2, row=1, padx=20, pady=0)

        self.Mbutton_3 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_3.grid(column=3, row=1, padx=0, pady=0)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=2, padx=spacers, pady=40)

        self.Mbutton_4 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_4.grid(column=1, row=2, padx=0, pady=0)

        self.Mbutton_5 = customtkinter.CTkButton(text="J.A.R.V.I.S", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Jarvis)
        self.Mbutton_5.grid(column=2, row=2, padx=0, pady=0)

        self.Mbutton_6 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_6.grid(column=3, row=2, padx=0, pady=0)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=2, row=3, padx=0, pady=30)

    def SosialMedia(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title("Sosial Media Links")

        self.SosialMedialabel_1 = customtkinter.CTkLabel(text="")
        self.SosialMedialabel_1.grid(column=1, row=1, padx=70, pady=0)

        self.SosialMedialabel_2 = customtkinter.CTkLabel(text="")
        self.SosialMedialabel_2.grid(column=1, row=2, padx=70, pady=0)

        self.SosialMediabutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMediaGoBack)
        self.SosialMediabutton_1.grid(column=0, row=0, padx=0, pady=10)

        self.SosialMediabutton_2 = customtkinter.CTkButton(text="Discord", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.discord)
        self.SosialMediabutton_2.grid(column=1, row=1, padx=20, pady=30)

        self.SosialMediabutton_3 = customtkinter.CTkButton(text="Github", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.github)
        self.SosialMediabutton_3.grid(column=2, row=1, padx=0, pady=10)

        self.SosialMediabutton_4 = customtkinter.CTkButton(text="Instagram", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.instagram)
        self.SosialMediabutton_4.grid(column=1, row=2, padx=20, pady=10)

        self.SosialMediabutton_5 = customtkinter.CTkButton(text="YouTube", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.youtube)
        self.SosialMediabutton_5.grid(column=2, row=2, padx=0, pady=10)

        self.SosialMediabutton_6 = customtkinter.CTkButton(text="Website", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.OpenSite)
        self.SosialMediabutton_6.grid(column=1, row=3, padx=0, pady=30)

        self.SosialMediabutton_7 = customtkinter.CTkButton(text="TikTok", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.TikTok)
        self.SosialMediabutton_7.grid(column=2, row=3, padx=0, pady=30)
    def SosialMediaGoBack(self):
        self.SosialMedialabel_1.destroy()
        self.SosialMedialabel_2.destroy()
        self.SosialMediabutton_1.destroy()
        self.SosialMediabutton_2.destroy()
        self.SosialMediabutton_3.destroy()
        self.SosialMediabutton_4.destroy()
        self.SosialMediabutton_5.destroy()
        self.SosialMediabutton_6.destroy()
        self.SosialMediabutton_7.destroy()

        self.title(f"Management Panel | v{App_Version}")

        self.Mlabel_2 = customtkinter.CTkLabel(text="")
        self.Mlabel_2.grid(column=0, row=0, padx=0, pady=30)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=1, padx=spacers, pady=0)

        self.Mbutton_1 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=0)

        self.Mbutton_2 = customtkinter.CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.YTDownloader)
        self.Mbutton_2.grid(column=2, row=1, padx=20, pady=0)

        self.Mbutton_3 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_3.grid(column=3, row=1, padx=0, pady=0)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=2, padx=spacers, pady=40)

        self.Mbutton_4 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_4.grid(column=1, row=2, padx=0, pady=0)

        self.Mbutton_5 = customtkinter.CTkButton(text="J.A.R.V.I.S", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Jarvis)
        self.Mbutton_5.grid(column=2, row=2, padx=0, pady=0)

        self.Mbutton_6 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_6.grid(column=3, row=2, padx=0, pady=0)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=2, row=3, padx=0, pady=30)

    def GameLauncher(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title("Game Launcher")

        self.GameMedialabel_1 = customtkinter.CTkLabel(text="")
        self.GameMedialabel_1.grid(column=1, row=1, padx=70, pady=0)

        self.GameMedialabel_2 = customtkinter.CTkLabel(text="")
        self.GameMedialabel_2.grid(column=1, row=2, padx=70, pady=0)

        self.GameMediabutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameGoBack)
        self.GameMediabutton_1.grid(column=0, row=0, padx=0, pady=10)

        self.GameMediabutton_2 = customtkinter.CTkButton(text="Rocket League", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_1)
        self.GameMediabutton_2.grid(column=1, row=1, padx=20, pady=20)

        self.GameMediabutton_3 = customtkinter.CTkButton(text="ARK", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_2)
        self.GameMediabutton_3.grid(column=2, row=1, padx=0, pady=5)

        self.GameMediabutton_4 = customtkinter.CTkButton(text="Destiny 2", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_3)
        self.GameMediabutton_4.grid(column=1, row=2, padx=0, pady=5)

        self.GameMediabutton_5 = customtkinter.CTkButton(text="Fall Guys", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_4)
        self.GameMediabutton_5.grid(column=2, row=2, padx=0, pady=20)

        self.GameMediabutton_6 = customtkinter.CTkButton(text="Warships", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_5)
        self.GameMediabutton_6.grid(column=1, row=3, padx=0, pady=20)

        self.GameMediabutton_7 = customtkinter.CTkButton(text="Control", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_6)
        self.GameMediabutton_7.grid(column=2, row=3, padx=0, pady=5)

        self.GameMediabutton_8 = customtkinter.CTkButton(text="GTA5", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_7)
        self.GameMediabutton_8.grid(column=1, row=4, padx=0, pady=20)

        self.GameMediabutton_9 = customtkinter.CTkButton(text="War Thunder", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_8)
        self.GameMediabutton_9.grid(column=2, row=4, padx=0, pady=20)
    def GameGoBack(self):
        self.GameMedialabel_1.destroy()
        self.GameMedialabel_2.destroy()
        self.GameMediabutton_1.destroy()
        self.GameMediabutton_2.destroy()
        self.GameMediabutton_3.destroy()
        self.GameMediabutton_4.destroy()
        self.GameMediabutton_5.destroy()
        self.GameMediabutton_6.destroy()
        self.GameMediabutton_7.destroy()
        self.GameMediabutton_8.destroy()
        self.GameMediabutton_9.destroy()

        self.title(f"Management Panel | v{App_Version}")

        self.Mlabel_2 = customtkinter.CTkLabel(text="")
        self.Mlabel_2.grid(column=0, row=0, padx=0, pady=30)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=1, padx=spacers, pady=0)

        self.Mbutton_1 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=0)

        self.Mbutton_2 = customtkinter.CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.YTDownloader)
        self.Mbutton_2.grid(column=2, row=1, padx=20, pady=0)

        self.Mbutton_3 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_3.grid(column=3, row=1, padx=0, pady=0)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=2, padx=spacers, pady=40)

        self.Mbutton_4 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_4.grid(column=1, row=2, padx=0, pady=0)

        self.Mbutton_5 = customtkinter.CTkButton(text="J.A.R.V.I.S", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Jarvis)
        self.Mbutton_5.grid(column=2, row=2, padx=0, pady=0)

        self.Mbutton_6 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_6.grid(column=3, row=2, padx=0, pady=0)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=2, row=3, padx=0, pady=30)

    def SystemSettings(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title("System Settings")

        self.Systemlabel_1 = customtkinter.CTkLabel(text="")
        self.Systemlabel_1.grid(column=1, row=1, padx=70, pady=0)

        self.Systemlabel_2 = customtkinter.CTkLabel(text="")
        self.Systemlabel_2.grid(column=1, row=2, padx=70, pady=0)

        self.Systembutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettingsGoBack)
        self.Systembutton_1.grid(column=0, row=0, padx=0, pady=10)

        self.Systembutton_2 = customtkinter.CTkButton(text="App Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.AppSettings)
        self.Systembutton_2.grid(column=1, row=1, padx=20, pady=30)

        self.Systembutton_3 = customtkinter.CTkButton(text="User Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.UserSettings)
        self.Systembutton_3.grid(column=2, row=1, padx=0, pady=10)

        self.Systembutton_4 = customtkinter.CTkButton(text="Power Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.PowerSettings)
        self.Systembutton_4.grid(column=1, row=2, padx=20, pady=10)

        self.Systembutton_5 = customtkinter.CTkButton(text="Sound Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SoundSettings)
        self.Systembutton_5.grid(column=2, row=2, padx=0, pady=10)

        self.Systembutton_6 = customtkinter.CTkButton(text="Network Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.NetworkSettings)
        self.Systembutton_6.grid(column=1, row=3, padx=0, pady=30)

        self.Systembutton_7 = customtkinter.CTkButton(text="Storage Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.StorageSettings)
        self.Systembutton_7.grid(column=2, row=3, padx=0, pady=30)

        self.Systembutton_8 = customtkinter.CTkButton(text="Drive Reset", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.NetworkDriveReset)
        self.Systembutton_8.grid(column=2, row=4, padx=0, pady=10)
    def SystemSettingsGoBack(self):
        self.Systemlabel_1.destroy()
        self.Systemlabel_2.destroy()
        self.Systembutton_1.destroy()
        self.Systembutton_2.destroy()
        self.Systembutton_3.destroy()
        self.Systembutton_4.destroy()
        self.Systembutton_5.destroy()
        self.Systembutton_6.destroy()
        self.Systembutton_7.destroy()
        self.Systembutton_8.destroy()

        self.title(f"Management Panel | v{App_Version}")

        self.Mlabel_2 = customtkinter.CTkLabel(text="")
        self.Mlabel_2.grid(column=0, row=0, padx=0, pady=30)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=1, padx=spacers, pady=0)

        self.Mbutton_1 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=0)

        self.Mbutton_2 = customtkinter.CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.YTDownloader)
        self.Mbutton_2.grid(column=2, row=1, padx=20, pady=0)

        self.Mbutton_3 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_3.grid(column=3, row=1, padx=0, pady=0)

        self.Mlabel_1 = customtkinter.CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=2, padx=spacers, pady=40)

        self.Mbutton_4 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_4.grid(column=1, row=2, padx=0, pady=0)

        self.Mbutton_5 = customtkinter.CTkButton(text="J.A.R.V.I.S", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Jarvis)
        self.Mbutton_5.grid(column=2, row=2, padx=0, pady=0)

        self.Mbutton_6 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_6.grid(column=3, row=2, padx=0, pady=0)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=2, row=3, padx=0, pady=30)


    def PowerSettings(self):
        os.system("cmd /c control")
        time.sleep(0.5)
        pyautogui.typewrite("Power Options", interval=0.01)
        time.sleep(0.2)
        pyautogui.press("tab",presses=1, interval=0)
        pyautogui.press("enter", interval=0)
    def UserSettings(self):
        os.system("cmd /c control")
        time.sleep(0.5)
        pyautogui.typewrite("User Account", interval=0.01)
        time.sleep(0.2)
        pyautogui.press("tab",presses=1, interval=0)
        pyautogui.press("enter", interval=0)
    def NetworkSettings(self):
        os.system("cmd /c control")
        time.sleep(0.5)
        pyautogui.typewrite("Network and Sharing Center", interval=0.01)
        time.sleep(0.2)
        pyautogui.press("tab",presses=1, interval=0)
        pyautogui.press("enter", interval=0)
    def SoundSettings(self):
        os.system("cmd /c control")
        time.sleep(0.5)
        pyautogui.typewrite("Sound", interval=0.01)
        time.sleep(0.2)
        pyautogui.press("tab",presses=1, interval=0)
        pyautogui.press("enter", interval=0)
    def AppSettings(self):
        pyautogui.keyDown("win")
        pyautogui.press("i")
        pyautogui.keyUp("win")
        time.sleep(1)
        pyautogui.typewrite("add or remove programs", interval=0.01)
        time.sleep(1.5)
        pyautogui.press("down")
        pyautogui.press("enter")
    def StorageSettings(self):
        pyautogui.keyDown("win")
        pyautogui.press("i")
        pyautogui.keyUp("win")
        time.sleep(1)
        pyautogui.typewrite("storage usage on other drives", interval=0.01)
        time.sleep(1.5)
        pyautogui.press("down")
        pyautogui.press("enter")
    def NetworkDriveReset(self):
            os.startfile("NetworkDriveReset.bat")


    def github(self):
        webbrowser.open(GithubURL)

    def youtube(self):
        webbrowser.open(YoutubeURL)

    def discord(self):
        webbrowser.open(DiscordURL)
    
    def instagram(self):
        webbrowser.open(instagramURL)

    def TikTok(self):
        webbrowser.open(TikTokURL)
    
    def OpenSite(self):
        webbrowser.open(Website)

    def OpenUpdater(self):
        os.startfile("Updater.exe")
        self.destroy()

    def YTDownloader(self):
        os.startfile("C:/Users/david/Desktop/Stuff/GitHub/Side-Projects/Management_Panel/YT_Downloader.py")
        time.sleep(0.3)
        exit()

    def Jarvis(self):
        os.startfile("C:/Users/david/Desktop/Stuff/GitHub/Side-Projects/Management_Panel/Jarvis.py")
        time.sleep(0.3)
        exit()

    def LaunchGame_1(self):
        webbrowser.open(Game_1)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def LaunchGame_2(self):
        webbrowser.open(Game_2)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def LaunchGame_3(self):
        webbrowser.open(Game_3)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def LaunchGame_4(self):
        webbrowser.open(Game_4)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def LaunchGame_5(self):
        webbrowser.open(Game_5)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def LaunchGame_6(self):
        webbrowser.open(Game_6)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def LaunchGame_7(self):
        webbrowser.open(Game_7)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def LaunchGame_8(self):
        webbrowser.open(Game_8)
        plyer.notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)

    def on_closing(self, event=0):
        print(CLR_RED + "\n   GUI is being terminated" + RESET_ALL)
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()