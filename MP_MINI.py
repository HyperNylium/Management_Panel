
from Management_Panel import App_Version, CurrentAppVersion, clear_command, GetUserDesktopLocation, Developer, Developer_Lowercase, file, LastEditDate, LatestVersionPythonLink, LatestVersionPythonFileName, LatestVersionProjectLink, ShowUserInfo
from Management_Panel import Website, GithubURL, DiscordURL, instagramURL, YoutubeURL, TikTokURL, FacebookURL, TwitterURL, Game_1, Game_2, Game_3, Game_4, Game_5, Game_6, Game_7, Game_8
from Management_Panel import CLR_RED, CLR_GREEN, CLR_YELLOW, CLR_BLUE, CLR_CYAN, CLR_WHITE, CLR_BLACK, CLR_MAGENTA, RESET_ALL
import platform
import os
import time
import webbrowser

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

try:
	import winshell
except:
	os.system("python -m pip install winshell")
import winshell

try:
	from colorama import *
except:
	os.system("python -m pip install colorama")
from colorama import *


from tkinter import messagebox
from tkinter.ttk import *



###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Author/Creator: HyperNylium
###
### Command: pyinstaller --onefile MP_MINI.py
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

PADY_Main = 10
PADY_GameLauncher = 10
PADY_SosialMedia = 10
PADY_SystemSettings = 10
PADY_Apps = 15
spacers = 0
class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()
        self.title(f"MP | v{App_Version}")
        self.geometry("250x350+400+150")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(0, 0)

        print(CLR_GREEN + "\n  GUI was launched Successfully" + RESET_ALL)

        self.Mbutton_1 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=PADY_Main)

        self.Mbutton_2 = customtkinter.CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Apps)
        self.Mbutton_2.grid(column=1, row=2, padx=0, pady=PADY_Main)

        self.Mbutton_3 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_3.grid(column=1, row=3, padx=0, pady=PADY_Main)

        self.Mbutton_4 = customtkinter.CTkButton(text="Social Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_4.grid(column=1, row=4, padx=55, pady=PADY_Main)

        self.Mbutton_5 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_5.grid(column=1, row=5, padx=0, pady=PADY_Main)

        self.Mbutton_6 = customtkinter.CTkButton(text="Normal GUI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchNormalGUI)
        self.Mbutton_6.grid(column=1, row=6, padx=0, pady=PADY_Main)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=1, row=7, padx=0, pady=PADY_Main)

#~~~ Funtions ~~~#
    def About(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title("About")
        self.geometry("250x550")

        self.Aboutbutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.AboutGoBack)
        self.Aboutbutton_1.grid(column=0, row=0, padx=0, pady=20)

        self.Aboutlabel_1 = customtkinter.CTkLabel(text="About", text_font=("sans-serif", 40))
        self.Aboutlabel_1.grid(column=0, row=1, padx=50, pady=20)

        self.Aboutlabel_2 = customtkinter.CTkLabel(text=f"Version:\n {App_Version}\n {ShowUserInfo}", text_font=("sans-serif", 20))
        self.Aboutlabel_2.grid(column=0, row=2, padx=10, pady=0)

        self.Aboutlabel_3 = customtkinter.CTkLabel(text=f"\nCreator/Developer:\n{Developer}", text_font=("sans-serif", 20))
        self.Aboutlabel_3.grid(column=0, row=3, padx=0, pady=0)

        self.Aboutlabel_4 = customtkinter.CTkLabel(text=f"\nLast updated:\n{LastEditDate}", text_font=("sans-serif", 20))
        self.Aboutlabel_4.grid(column=0, row=4, padx=0, pady=0)

        self.Aboutbutton_2 = customtkinter.CTkButton(text="Check For Updates", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), command=self.OpenUpdater)
        self.Aboutbutton_2.grid(column=0, row=5,padx=20, pady=50)
    def AboutGoBack(self):
        self.Aboutbutton_1.destroy()
        self.Aboutbutton_2.destroy()
        self.Aboutlabel_1.destroy()
        self.Aboutlabel_2.destroy()
        self.Aboutlabel_3.destroy()
        self.Aboutlabel_4.destroy()

        self.title(f"MP | v{App_Version}")
        self.geometry("250x350")

        self.Mbutton_1 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=PADY_Main)

        self.Mbutton_2 = customtkinter.CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Apps)
        self.Mbutton_2.grid(column=1, row=2, padx=0, pady=PADY_Main)

        self.Mbutton_3 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_3.grid(column=1, row=3, padx=0, pady=PADY_Main)

        self.Mbutton_4 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_4.grid(column=1, row=4, padx=55, pady=PADY_Main)

        self.Mbutton_5 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_5.grid(column=1, row=5, padx=0, pady=PADY_Main)

        self.Mbutton_6 = customtkinter.CTkButton(text="Normal GUI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchNormalGUI)
        self.Mbutton_6.grid(column=1, row=6, padx=0, pady=PADY_Main)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=1, row=7, padx=0, pady=PADY_Main)

    def SosialMedia(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"SML | v{App_Version}")
        self.geometry("250x370")

        self.SosialMediabutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMediaGoBack)
        self.SosialMediabutton_1.grid(column=0, row=0, padx=55, pady=20)

        self.SosialMediabutton_2 = customtkinter.CTkButton(text="Discord", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.discord)
        self.SosialMediabutton_2.grid(column=0, row=1, padx=0, pady=PADY_SosialMedia)

        self.SosialMediabutton_3 = customtkinter.CTkButton(text="Github", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.github)
        self.SosialMediabutton_3.grid(column=0, row=2, padx=0, pady=PADY_SosialMedia)

        self.SosialMediabutton_4 = customtkinter.CTkButton(text="Instagram", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.instagram)
        self.SosialMediabutton_4.grid(column=0, row=3, padx=0, pady=PADY_SosialMedia)

        self.SosialMediabutton_5 = customtkinter.CTkButton(text="YouTube", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.youtube)
        self.SosialMediabutton_5.grid(column=0, row=4, padx=0, pady=PADY_SosialMedia)

        self.SosialMediabutton_6 = customtkinter.CTkButton(text="Website", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.OpenSite)
        self.SosialMediabutton_6.grid(column=0, row=5, padx=0, pady=PADY_SosialMedia)

        self.SosialMediabutton_7 = customtkinter.CTkButton(text="TikTok", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.TikTok)
        self.SosialMediabutton_7.grid(column=0, row=6, padx=0, pady=PADY_SosialMedia)
    def SosialMediaGoBack(self):
        self.SosialMediabutton_1.destroy()
        self.SosialMediabutton_2.destroy()
        self.SosialMediabutton_3.destroy()
        self.SosialMediabutton_4.destroy()
        self.SosialMediabutton_5.destroy()
        self.SosialMediabutton_6.destroy()
        self.SosialMediabutton_7.destroy()

        self.title(f"MP | v{App_Version}")
        self.geometry("250x350")

        self.Mbutton_1 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=PADY_Main)

        self.Mbutton_2 = customtkinter.CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Apps)
        self.Mbutton_2.grid(column=1, row=2, padx=0, pady=PADY_Main)

        self.Mbutton_3 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_3.grid(column=1, row=3, padx=0, pady=PADY_Main)

        self.Mbutton_4 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_4.grid(column=1, row=4, padx=55, pady=PADY_Main)

        self.Mbutton_5 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_5.grid(column=1, row=5, padx=0, pady=PADY_Main)

        self.Mbutton_6 = customtkinter.CTkButton(text="Normal GUI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchNormalGUI)
        self.Mbutton_6.grid(column=1, row=6, padx=0, pady=PADY_Main)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=1, row=7, padx=0, pady=PADY_Main)

    def GameLauncher(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"GL | v{App_Version}")
        self.geometry("250x500")

        self.GameMediabutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameGoBack)
        self.GameMediabutton_1.grid(column=0, row=0, padx=55, pady=20)

        self.GameMediabutton_2 = customtkinter.CTkButton(text="Rocket League", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_1)
        self.GameMediabutton_2.grid(column=0, row=1, padx=0, pady=PADY_GameLauncher)

        self.GameMediabutton_3 = customtkinter.CTkButton(text="ARK", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_2)
        self.GameMediabutton_3.grid(column=0, row=2, padx=0, pady=PADY_GameLauncher)

        self.GameMediabutton_4 = customtkinter.CTkButton(text="Destiny 2", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_3)
        self.GameMediabutton_4.grid(column=0, row=3, padx=0, pady=PADY_GameLauncher)

        self.GameMediabutton_5 = customtkinter.CTkButton(text="Fall Guys", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_4)
        self.GameMediabutton_5.grid(column=0, row=4, padx=0, pady=PADY_GameLauncher)

        self.GameMediabutton_6 = customtkinter.CTkButton(text="Warships", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_5)
        self.GameMediabutton_6.grid(column=0, row=5, padx=0, pady=PADY_GameLauncher)

        self.GameMediabutton_7 = customtkinter.CTkButton(text="Control", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_6)
        self.GameMediabutton_7.grid(column=0, row=6, padx=0, pady=PADY_GameLauncher)

        self.GameMediabutton_8 = customtkinter.CTkButton(text="GTA5", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_7)
        self.GameMediabutton_8.grid(column=0, row=7, padx=0, pady=PADY_GameLauncher)

        self.GameMediabutton_9 = customtkinter.CTkButton(text="War Thunder", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchGame_8)
        self.GameMediabutton_9.grid(column=0, row=8, padx=0, pady=PADY_GameLauncher)
    def GameGoBack(self):
        self.GameMediabutton_1.destroy()
        self.GameMediabutton_2.destroy()
        self.GameMediabutton_3.destroy()
        self.GameMediabutton_4.destroy()
        self.GameMediabutton_5.destroy()
        self.GameMediabutton_6.destroy()
        self.GameMediabutton_7.destroy()
        self.GameMediabutton_8.destroy()
        self.GameMediabutton_9.destroy()

        self.title(f"MP | v{App_Version}")
        self.geometry("250x350")

        self.Mbutton_1 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=PADY_Main)

        self.Mbutton_2 = customtkinter.CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Apps)
        self.Mbutton_2.grid(column=1, row=2, padx=0, pady=PADY_Main)

        self.Mbutton_3 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_3.grid(column=1, row=3, padx=0, pady=PADY_Main)

        self.Mbutton_4 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_4.grid(column=1, row=4, padx=55, pady=PADY_Main)

        self.Mbutton_5 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_5.grid(column=1, row=5, padx=0, pady=PADY_Main)

        self.Mbutton_6 = customtkinter.CTkButton(text="Normal GUI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchNormalGUI)
        self.Mbutton_6.grid(column=1, row=6, padx=0, pady=PADY_Main)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=1, row=7, padx=0, pady=PADY_Main)

    def SystemSettings(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"SS | v{App_Version}")
        self.geometry("250x600")

        self.Systembutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettingsGoBack)
        self.Systembutton_1.grid(column=0, row=0, padx=55, pady=20)

        self.Systembutton_2 = customtkinter.CTkButton(text="App Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.AppSettings)
        self.Systembutton_2.grid(column=0, row=1, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_3 = customtkinter.CTkButton(text="VPN Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.VPNSettings)
        self.Systembutton_3.grid(column=0, row=2, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_4 = customtkinter.CTkButton(text="TaskManager", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.TaskManager)
        self.Systembutton_4.grid(column=0, row=3, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_5 = customtkinter.CTkButton(text="NetDrive Reset", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.ResetNetworkDrive)
        self.Systembutton_5.grid(column=0, row=4, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_6 = customtkinter.CTkButton(text="Power Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.PowerSettings)
        self.Systembutton_6.grid(column=0, row=5, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_7 = customtkinter.CTkButton(text="Sound Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SoundSettings)
        self.Systembutton_7.grid(column=0, row=6, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_8 = customtkinter.CTkButton(text="Storage Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.StorageSettings)
        self.Systembutton_8.grid(column=0, row=7, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_9 = customtkinter.CTkButton(text="Display Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.DisplaySettings)
        self.Systembutton_9.grid(column=0, row=8, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_10 = customtkinter.CTkButton(text="Network Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.NetworkSettings)
        self.Systembutton_10.grid(column=0, row=9, padx=0, pady= PADY_SystemSettings)

        self.Systembutton_11 = customtkinter.CTkButton(text="Windows Update", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.WindowsUpdate)
        self.Systembutton_11.grid(column=0, row=10, padx=0, pady= PADY_SystemSettings)
    def SystemSettingsGoBack(self):
        self.Systembutton_1.destroy()
        self.Systembutton_2.destroy()
        self.Systembutton_3.destroy()
        self.Systembutton_4.destroy()
        self.Systembutton_5.destroy()
        self.Systembutton_6.destroy()
        self.Systembutton_7.destroy()
        self.Systembutton_8.destroy()
        self.Systembutton_9.destroy()
        self.Systembutton_10.destroy()
        self.Systembutton_11.destroy()

        self.title(f"MP | v{App_Version}")
        self.geometry("250x350")

        self.Mbutton_1 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=PADY_Main)

        self.Mbutton_2 = customtkinter.CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Apps)
        self.Mbutton_2.grid(column=1, row=2, padx=0, pady=PADY_Main)

        self.Mbutton_3 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_3.grid(column=1, row=3, padx=0, pady=PADY_Main)

        self.Mbutton_4 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_4.grid(column=1, row=4, padx=55, pady=PADY_Main)

        self.Mbutton_5 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_5.grid(column=1, row=5, padx=0, pady=PADY_Main)

        self.Mbutton_6 = customtkinter.CTkButton(text="Normal GUI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchNormalGUI)
        self.Mbutton_6.grid(column=1, row=6, padx=0, pady=PADY_Main)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=1, row=7, padx=0, pady=PADY_Main)

    def Apps(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"SML | v{App_Version}")
        self.geometry("250x350")

        self.Appsbutton_1 = customtkinter.CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.AppsGoBack)
        self.Appsbutton_1.grid(column=0, row=0, padx=55, pady=30)

        self.Appsbutton_2 = customtkinter.CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.YTDownloader)
        self.Appsbutton_2.grid(column=0, row=1, padx=0, pady=PADY_Apps)

        self.Appsbutton_3 = customtkinter.CTkButton(text="Jarvis", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Jarvis)
        self.Appsbutton_3.grid(column=0, row=2, padx=0, pady=PADY_Apps)
    def AppsGoBack(self):
        self.Appsbutton_1.destroy()
        self.Appsbutton_2.destroy()
        self.Appsbutton_3.destroy()

        self.title(f"MP | v{App_Version}")
        self.geometry("250x350")

        self.Mbutton_1 = customtkinter.CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.About)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=PADY_Main)

        self.Mbutton_2 = customtkinter.CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.Apps)
        self.Mbutton_2.grid(column=1, row=2, padx=0, pady=PADY_Main)

        self.Mbutton_3 = customtkinter.CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.GameLauncher)
        self.Mbutton_3.grid(column=1, row=3, padx=0, pady=PADY_Main)

        self.Mbutton_4 = customtkinter.CTkButton(text="Sosial Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SosialMedia)
        self.Mbutton_4.grid(column=1, row=4, padx=55, pady=PADY_Main)

        self.Mbutton_5 = customtkinter.CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.SystemSettings)
        self.Mbutton_5.grid(column=1, row=5, padx=0, pady=PADY_Main)

        self.Mbutton_6 = customtkinter.CTkButton(text="Normal GUI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.LaunchNormalGUI)
        self.Mbutton_6.grid(column=1, row=6, padx=0, pady=PADY_Main)

        self.Mbutton_7 = customtkinter.CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.on_closing)
        self.Mbutton_7.grid(column=1, row=7, padx=0, pady=PADY_Main)


    def PowerSettings(self):
        os.system("cmd /c control powercfg.cpl")
    def DisplaySettings(self):
        os.system("cmd /c control desk.cpl")
    def NetworkSettings(self):
        os.system("cmd /c %systemroot%\system32\control.exe /name Microsoft.NetworkAndSharingCenter")
    def SoundSettings(self):
        os.system("cmd /c control mmsys.cpl sounds")
    def AppSettings(self):
        os.system("cmd /c start ms-settings:appsfeatures")#Put "appwiz.cpl" after /c for control center version
    def StorageSettings(self):
        os.system("cmd /c start ms-settings:storagesense")
    def WindowsUpdate(self):
        os.system("cmd /c %systemroot%\system32\control.exe /name Microsoft.WindowsUpdate")
    def TaskManager(self):
        os.system("cmd /c taskmgr")
    def VPNSettings(self):
        os.system("cmd /c start ms-settings:network-vpn")
    def ResetNetworkDrive(self):
        try:
            os.startfile("NetworkDriveReset.bat")
        except:
            pyautogui.alert(text=f"The file 'NetworkDriveReset.bat' was not found. This file resets all network drives that are on the users system. The Creator/Developer {Developer} uses this file but doesn't include it with version control.", title='FILE NOT FOUND!', button='OK')

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
        file.close()
        self.destroy()

    def YTDownloader(self):
        os.startfile("YT_Downloader.py")
        time.sleep(0.3)
        file.close()
        exit()

    def Jarvis(self):
        os.startfile("Jarvis.py")
        time.sleep(0.3)
        file.close()
        exit()

    def LaunchNormalGUI(self):
        os.startfile("Management_Panel.py")
        time.sleep(0.3)
        file.close()
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
        print(CLR_RED + "\n  GUI is being terminated" + RESET_ALL)
        file.close()
        self.destroy()

if __name__ == "__main__":
    app = App()
    app.mainloop()