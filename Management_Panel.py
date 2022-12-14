
import platform
from os import system, startfile
from time import sleep
from webbrowser import open as WBopen
from sys import exit

try:
    from tkinter import *
    from tkinter.ttk import *
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: tkinter\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install tk ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()

try:
    from pyautogui import confirm, alert
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: pyautogui\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install pyautogui ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()

try:
	from customtkinter import set_appearance_mode, CTk, CTkLabel, CTkButton
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: customtkinter\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install customtkinter==4.6.2 ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
    from plyer import notification
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: plyer\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install plyer ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
    from requests import get
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: requests\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install requests ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
    from winshell import desktop
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: winshell\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install winshell ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()

try:
    from colorama import Fore
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: colorama\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install colorama ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


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

set_appearance_mode("dark")

# Text Colors
CLR_RED = Fore.RED
CLR_GREEN = Fore.GREEN
CLR_YELLOW = Fore.YELLOW
CLR_BLUE = Fore.BLUE
CLR_CYAN = Fore.CYAN
CLR_WHITE = Fore.WHITE
CLR_BLACK = Fore.BLACK
CLR_MAGENTA = Fore.MAGENTA
RESET_ALL = Fore.RESET

CurrentAppVersion = "3.7.6"
UpdateLink = "https://github.com/HyperNylium/Management_Panel"
DataTXTFileUrl = "http://www.hypernylium.com/Python-Projects/Management_Panel/Data.txt"

try:
    print(CLR_YELLOW + "\n  Checking for updates" + RESET_ALL)
    response = get(DataTXTFileUrl)
    lines = response.text.split('\n')
    delimeter = "="

    def findValue(fullString):
        fullString = fullString.rstrip("\n")
        value = fullString[fullString.index(delimeter)+1:]
        value = value.replace(" ","")
        return value

    for line in lines:
        if line.startswith("Version"):
            App_Version = findValue(line).strip()
        if line.startswith("DevName"):
            Developer = findValue(line).strip()
        if line.startswith("Developer_Lowercase"):
            Developer_Lowercase = findValue(line)
        if line.startswith("LastEditDate"):
            LastEditDate = findValue(line).strip()
        if line.startswith("LatestVersionPythonLink"):
            LatestVersionPythonLink = findValue(line).strip()
        if line.startswith("LatestVersionPythonFileName"):
            LatestVersionPythonFileName = findValue(line).strip()
        if line.startswith("LatestVersionProjectLink"):
            LatestVersionProjectLink = findValue(line).strip()

    if App_Version < CurrentAppVersion:
            print(CLR_RED + f"\n  You have an invalid copy/version of this software. Use at your own risk!\n\n  Live/Public version: {App_Version}\n  Current version: {CurrentAppVersion}\n\n  Please go to http://search.hypernylium.com/results/ServerFileManager/ to get the latest/authentic version of this software")
            Developer = "Unknown"
            Developer_Lowercase = "Unknown"
            LastEditDate = "Unknown"
            App_Version = CurrentAppVersion
            ShowUserInfo = "- Unauthentic"
            sleep(7)
            pass
    elif App_Version != CurrentAppVersion or App_Version > CurrentAppVersion:
            print(CLR_RED + f"\n  New version found!" + RESET_ALL)
            output = confirm(title='New Version!', text=f'New Version is v{App_Version}\nYour Version is v{CurrentAppVersion}\n\nNew Version of the app is now available to download/install\nClick "OK" to update and "Cancel" to cancel')
            if (output == "OK"):
                print(CLR_YELLOW + "  Launching Github repository in default browser")
                WBopen(UpdateLink)
                sleep(0.5)
                exit()
            else:
                ShowUserInfo = f"- Update available (v{App_Version})"
                App_Version = CurrentAppVersion
                pass
    else:
        print(CLR_GREEN + f"\n  {App_Version} is the latest version. Continuing on with launch protocol" + RESET_ALL)
        ShowUserInfo = "- Latest version"
        pass
except Exception as e:
    print(CLR_RED + f"\n  Was unable to fetch app information file!\n  Passing 'N/A' in all variables and continuing in offine mode" + RESET_ALL)
    App_Version = "N/A"
    Developer = "N/A"
    Developer_Lowercase = "N/A"
    LastEditDate = "N/A"
    LatestVersionPythonLink = "N/A"
    LatestVersionPythonFileName = "N/A"
    LatestVersionProjectLink = "N/A"
    ShowUserInfo = ""
    sleep(3)
    pass

Website = "http://hypernylium.com/"
GithubURL = "https://github.com/HyperNylium"
DiscordURL = "https://discord.gg/4FHTjAgw95"
instagramURL = "https://www.instagram.com/hypernylium/"
YoutubeURL = "https://www.youtube.com/channel/UCpJ4F4dMn_DIhtrCJwDUK2A"
TikTokURL = "https://www.tiktok.com/foryou?lang=en"
FacebookURL = "https://www.facebook.com/HyperNylium/"
TwitterURL = "https://twitter.com/HyperNylium"
GetUserDesktopLocation = desktop()
SystemSettingsPadY = 15

"""
Game_1 = Rocket League
Game_2 = GTA5
Game_3 = Subnautica
Game_4 = ARK
Game_5 = LOL
Game_6 = Destiny 2
Game_7 = Among Us
Game_8 = Fall Guys
"""

Game_1 = "com.epicgames.launcher://apps/9773aa1aa54f4f7b80e44bef04986cea%3A530145df28a24424923f5828cc9031a1%3ASugar?action=launch&silent=true"
Game_2 = "com.epicgames.launcher://apps/0584d2013f0149a791e7b9bad0eec102%3A6e563a2c0f5f46e3b4e88b5f4ed50cca%3A9d2d0eb64d5c44529cece33fe2a46482?action=launch&silent=true"
Game_3 = "com.epicgames.launcher://apps/jaguar%3A3257e06c28764231acd93049f3774ed6%3AJaguar?action=launch&silent=true"
Game_4 = "com.epicgames.launcher://apps/ark%3A743e47ee84ac49a1a49f4781da70e0d0%3Aaafc587fbf654758802c8e41e4fb3255?action=launch&silent=true"
Game_5 = "com.epicgames.launcher://apps/24b9b5e323bc40eea252a10cdd3b2f10%3Ad398f3033c5e4b90b09dcbb4b962be80%3A64b0c77d07f644e6a2326a1fd7ab9926?action=launch&silent=true"
Game_6 = "com.epicgames.launcher://apps/428115def4ca4deea9d69c99c5a5a99e%3A06bd477f9fbe4259a1421fb3f559aa46%3A592c359fb0e0413fb46dee2d24448eb4?action=launch&silent=true"
Game_7 = "com.epicgames.launcher://apps/33956bcb55d4452d8c47e16b94e294bd%3A729a86a5146640a2ace9e8c595414c56%3A963137e4c29d4c79a81323b8fab03a40?action=launch&silent=true"
Game_8 = "com.epicgames.launcher://apps/50118b7f954e450f8823df1614b24e80%3A38ec4849ea4f4de6aa7b6fb0f2d278e1%3A0a2d9f6403244d12969e11da6713137b?action=launch&silent=true"

spacers = 20

clear_command = "cls" if platform.system() == "Windows" else "clear"


class App(CTk):
    def MainMenu(self):
        self.title(f"Management Panel | v{App_Version}")

        self.Mlabel_1 = CTkLabel(text="")
        self.Mlabel_1.grid(column=0, row=1, padx=spacers, pady=0)

        self.Mlabel_2 = CTkLabel(text="")
        self.Mlabel_2.grid(column=0, row=0, padx=0, pady=30)

        self.Mbutton_1 = CTkButton(text="Social Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10,command=self.SosialMedia)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=0)

        self.Mbutton_2 = CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.Apps)
        self.Mbutton_2.grid(column=2, row=1, padx=20, pady=0)

        self.Mbutton_3 = CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.About)
        self.Mbutton_3.grid(column=3, row=1, padx=0, pady=0)

        self.Mlabel_3 = CTkLabel(text="")
        self.Mlabel_3.grid(column=0, row=2, padx=spacers, pady=40)

        self.Mbutton_4 = CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.GameLauncher)
        self.Mbutton_4.grid(column=1, row=2, padx=0, pady=0)

        self.Mbutton_5 = CTkButton(text="MP_MINI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.MP_MINI)
        self.Mbutton_5.grid(column=2, row=2, padx=20, pady=0)

        self.Mbutton_6 = CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.SystemSettings)
        self.Mbutton_6.grid(column=3, row=2, padx=0, pady=0)

        self.Mbutton_7 = CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.on_closing)
        self.Mbutton_7.grid(column=2, row=3, padx=0, pady=30)

    def About(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mlabel_3.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title("About")

        self.Aboutbutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 15), command=self.AboutGoBack)
        self.Aboutbutton_1.grid(column=0, row=0, padx=10, pady=10)

        self.Aboutlabel_1 = CTkLabel(text="About", text_font=("sans-serif", 50))
        self.Aboutlabel_1.grid(column=2, row=1, padx=160, pady=20)

        self.Aboutlabel_2 = CTkLabel(text=f"Version: {App_Version} {ShowUserInfo}", text_font=("sans-serif", 20))
        self.Aboutlabel_2.grid(column=2, row=2, padx=0, pady=10)

        self.Aboutlabel_3 = CTkLabel(text=f"Creator/Developer: {Developer}", text_font=("sans-serif", 20))
        self.Aboutlabel_3.grid(column=2, row=3, padx=0, pady=10)

        self.Aboutlabel_4 = CTkLabel(text=f"Last updated: {LastEditDate}", text_font=("sans-serif", 20))
        self.Aboutlabel_4.grid(column=2, row=4, padx=0, pady=10)

        self.Aboutbutton_2 = CTkButton(text="Check For Updates", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10,command=self.OpenUpdater)
        self.Aboutbutton_2.grid(column=2, row=5,padx=0, pady=30)
    def AboutGoBack(self):
        self.Aboutbutton_1.destroy()
        self.Aboutbutton_2.destroy()
        self.Aboutlabel_1.destroy()
        self.Aboutlabel_2.destroy()
        self.Aboutlabel_3.destroy()
        self.Aboutlabel_4.destroy()

        self.MainMenu()
    def SosialMedia(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mlabel_3.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()


        self.title(f"Sosial Media Links | v{App_Version}")

        self.SosialMedialabel_1 = CTkLabel(text="")
        self.SosialMedialabel_1.grid(column=1, row=1, padx=70, pady=0)

        self.SosialMedialabel_2 = CTkLabel(text="")
        self.SosialMedialabel_2.grid(column=1, row=2, padx=70, pady=0)

        self.SosialMediabutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.SosialMediaGoBack)
        self.SosialMediabutton_1.grid(column=0, row=0, padx=10, pady=10)

        self.SosialMediabutton_2 = CTkButton(text="Discord", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.SocialMediaLoader(DiscordURL))
        self.SosialMediabutton_2.grid(column=1, row=1, padx=20, pady=30)

        self.SosialMediabutton_3 = CTkButton(text="Github", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.SocialMediaLoader(GithubURL))
        self.SosialMediabutton_3.grid(column=2, row=1, padx=0, pady=10)

        self.SosialMediabutton_4 = CTkButton(text="Instagram", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.SocialMediaLoader(instagramURL))
        self.SosialMediabutton_4.grid(column=1, row=2, padx=20, pady=10)

        self.SosialMediabutton_5 = CTkButton(text="YouTube", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.SocialMediaLoader(YoutubeURL))
        self.SosialMediabutton_5.grid(column=2, row=2, padx=0, pady=10)

        self.SosialMediabutton_6 = CTkButton(text="Website", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.SocialMediaLoader(Website))
        self.SosialMediabutton_6.grid(column=1, row=3, padx=0, pady=30)

        self.SosialMediabutton_7 = CTkButton(text="TikTok", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.SocialMediaLoader(TikTokURL))
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

        self.MainMenu()
    def Apps(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mlabel_3.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"Apps section | v{App_Version}")

        self.AppsBackbutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.GoBackApps)
        self.AppsBackbutton_1.grid(column=0, row=0, padx=10, pady=10)

        self.Appsbutton_1 = CTkLabel(text="")
        self.Appsbutton_1.grid(column=1, row=1, padx=90, pady=0)

        self.Appsbutton_2 = CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.YTDownloader)
        self.Appsbutton_2.grid(column=1, row=2, padx=0, pady=0)

        self.Appsbutton_3 = CTkButton(text="J.A.R.V.I.S", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.Jarvis)
        self.Appsbutton_3.grid(column=2, row=2, padx=0, pady=0)
    def GoBackApps(self):
        self.AppsBackbutton_1.destroy()
        self.Appsbutton_1.destroy()
        self.Appsbutton_2.destroy()
        self.Appsbutton_3.destroy()

        self.MainMenu()
    def GameLauncher(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mlabel_3.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"Game Launcher | v{App_Version}")

        self.GameMedialabel_1 = CTkLabel(text="")
        self.GameMedialabel_1.grid(column=1, row=1, padx=70, pady=0)

        self.GameMedialabel_2 = CTkLabel(text="")
        self.GameMedialabel_2.grid(column=1, row=2, padx=70, pady=0)

        self.GameMediabutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.GameGoBack)
        self.GameMediabutton_1.grid(column=0, row=0, padx=10, pady=10)

        self.GameMediabutton_2 = CTkButton(text="Rocket League", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_1))
        self.GameMediabutton_2.grid(column=1, row=1, padx=20, pady=20)

        self.GameMediabutton_3 = CTkButton(text="GTA5", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_2))
        self.GameMediabutton_3.grid(column=2, row=1, padx=0, pady=5)

        self.GameMediabutton_4 = CTkButton(text="Subnautica", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_3))
        self.GameMediabutton_4.grid(column=1, row=2, padx=0, pady=5)

        self.GameMediabutton_5 = CTkButton(text="ARK", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_4))
        self.GameMediabutton_5.grid(column=2, row=2, padx=0, pady=20)

        self.GameMediabutton_6 = CTkButton(text="LOL", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_5))
        self.GameMediabutton_6.grid(column=1, row=3, padx=0, pady=20)

        self.GameMediabutton_7 = CTkButton(text="Destiny 2", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_6))
        self.GameMediabutton_7.grid(column=2, row=3, padx=0, pady=5)

        self.GameMediabutton_8 = CTkButton(text="Among Us", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_7))
        self.GameMediabutton_8.grid(column=1, row=4, padx=0, pady=20)

        self.GameMediabutton_9 = CTkButton(text="Fall Guys", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=lambda: self.LaunchGame(Game_8))
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

        self.MainMenu()
    def SystemSettings(self):
        self.Mlabel_1.destroy()
        self.Mlabel_2.destroy()
        self.Mlabel_3.destroy()
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()


        self.title(f"System Settings | v{App_Version}")

        self.Systemlabel_1 = CTkLabel(text="")
        self.Systemlabel_1.grid(column=1, row=1, padx=70, pady=0)

        self.Systemlabel_2 = CTkLabel(text="")
        self.Systemlabel_2.grid(column=1, row=2, padx=70, pady=0)

        self.Systembutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.SystemSettingsGoBack)
        self.Systembutton_1.grid(column=0, row=0, padx=10, pady=20)

        self.Systembutton_2 = CTkButton(text="App Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.AppSettings)
        self.Systembutton_2.grid(column=1, row=1, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_3 = CTkButton(text="VPN Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.VPNSettings)
        self.Systembutton_3.grid(column=2, row=1, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_4 = CTkButton(text="TaskManager", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.TaskManager)
        self.Systembutton_4.grid(column=1, row=2, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_5 = CTkButton(text="NetDrive Reset", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.ResetNetworkDrive)
        self.Systembutton_5.grid(column=2, row=2, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_6 = CTkButton(text="Power Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.PowerSettings)
        self.Systembutton_6.grid(column=1, row=3, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_7 = CTkButton(text="Sound Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.SoundSettings)
        self.Systembutton_7.grid(column=2, row=3, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_8 = CTkButton(text="Storage Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.StorageSettings)
        self.Systembutton_8.grid(column=1, row=4, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_9 = CTkButton(text="Display Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.DisplaySettings)
        self.Systembutton_9.grid(column=2, row=4, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_10 = CTkButton(text="Network Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.NetworkSettings)
        self.Systembutton_10.grid(column=1, row=5, padx=0, pady= SystemSettingsPadY)

        self.Systembutton_11 = CTkButton(text="Windows Update", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=10, command=self.WindowsUpdate)
        self.Systembutton_11.grid(column=2, row=5, padx=0, pady= SystemSettingsPadY)
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
        self.Systembutton_9.destroy()
        self.Systembutton_10.destroy()
        self.Systembutton_11.destroy()

        self.MainMenu()


    def PowerSettings(self):
        system("cmd /c control powercfg.cpl")
    def DisplaySettings(self):
        system("cmd /c control desk.cpl")
    def NetworkSettings(self):
        system("cmd /c %systemroot%\system32\control.exe /name Microsoft.NetworkAndSharingCenter")
    def SoundSettings(self):
        system("cmd /c control mmsys.cpl sounds")
    def AppSettings(self):
        system("cmd /c start ms-settings:appsfeatures")#Put "appwiz.cpl" after /c for control center version
    def StorageSettings(self):
        system("cmd /c start ms-settings:storagesense")
    def WindowsUpdate(self):
        system("cmd /c %systemroot%\system32\control.exe /name Microsoft.WindowsUpdate")
    def TaskManager(self):
        system("cmd /c taskmgr")
    def VPNSettings(self):
        system("cmd /c start ms-settings:network-vpn")
    def ResetNetworkDrive(self):
            try:
                startfile("NetworkDriveReset.bat")
            except:
                alert(text=f"The file 'NetworkDriveReset.bat' was not found. This file resets all network drives that are on the users system. The Creator/Developer {Developer} uses this file but doesn't include it with version control.", title='FILE NOT FOUND!', button='OK')


    def LaunchGame(self, GameVar):
        WBopen(GameVar)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def SocialMediaLoader(self, MediaVar):
        WBopen(MediaVar)
    def OpenUpdater(self):
        WBopen(GithubURL + "/Management_Panel")
        sleep(0.3)
        self.destroy()
    def Jarvis(self):
        startfile("Jarvis.py")
        sleep(0.3)
        self.destroy()
    def YTDownloader(self):
        startfile("YT_Downloader.py")
        sleep(0.3)
        self.destroy()
    def MP_MINI(self):
        startfile("MP_MINI.py")
        sleep(0.3)
        self.destroy()
    def on_closing(self, event=0):
        print(CLR_RED + "\n  GUI is being terminated" + RESET_ALL)
        self.destroy()
        exit()

    def __init__(self):
        super().__init__()

        self.geometry("800x500+400+150")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(0, 0)

        print(CLR_GREEN + "\n  GUI was launched Successfully" + RESET_ALL)

        self.MainMenu()


if __name__ == "__main__":
    app = App()
    app.mainloop()
