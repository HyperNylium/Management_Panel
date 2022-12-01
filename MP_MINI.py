
from Management_Panel import App_Version, CurrentAppVersion, clear_command, GetUserDesktopLocation, Developer, Developer_Lowercase, file, LastEditDate, LatestVersionPythonLink, LatestVersionPythonFileName, LatestVersionProjectLink, ShowUserInfo
from Management_Panel import Website, GithubURL, DiscordURL, instagramURL, YoutubeURL, TikTokURL, FacebookURL, TwitterURL, Game_1, Game_2, Game_3, Game_4, Game_5, Game_6, Game_7, Game_8
from Management_Panel import CLR_RED, CLR_GREEN, CLR_YELLOW, CLR_BLUE, CLR_CYAN, CLR_WHITE, CLR_BLACK, CLR_MAGENTA, RESET_ALL

import platform
from os import system, startfile
from time import sleep
import webbrowser
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
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: customtkinter\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install customtkinter ' + "\033[31m" + "to install correctly")
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

set_appearance_mode("dark")


PADY_SETTINGS = 5


class App(CTk):
    def MainMenu(self):
        self.title(f"MP | v{App_Version}")
        self.geometry("230x350")

        self.Mbutton_1 = CTkButton(text="Social Media", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.SosialMedia)
        self.Mbutton_1.grid(column=1, row=1, padx=0, pady=PADY_SETTINGS)

        self.Mbutton_2 = CTkButton(text="Apps", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.Apps)
        self.Mbutton_2.grid(column=1, row=2, padx=0, pady=PADY_SETTINGS)

        self.Mbutton_3 = CTkButton(text="About", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.About)
        self.Mbutton_3.grid(column=1, row=3, padx=0, pady=PADY_SETTINGS)

        self.Mbutton_4 = CTkButton(text="Games", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.GameLauncher)
        self.Mbutton_4.grid(column=1, row=4, padx=0, pady=PADY_SETTINGS)

        self.Mbutton_5 = CTkButton(text="System", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.SystemSettings)
        self.Mbutton_5.grid(column=1, row=5, padx=0, pady=PADY_SETTINGS)

        self.Mbutton_6 = CTkButton(text="Launch Normal GUI", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.NormalGUI)
        self.Mbutton_6.grid(column=1, row=6, padx=0, pady=PADY_SETTINGS)

        self.Mbutton_7 = CTkButton(text="Exit", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.on_closing)
        self.Mbutton_7.grid(column=1, row=7, padx=0, pady=14)

    def About(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title("About")
        self.geometry("230x425")

        self.Aboutbutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.AboutGoBack)
        self.Aboutbutton_1.grid(column=1, row=0, padx=0, pady=0)

        self.Aboutlabel_1 = CTkLabel(text="About", text_font=("sans-serif", 30))
        self.Aboutlabel_1.grid(column=1, row=1, padx=0, pady=15)

        self.Aboutlabel_2 = CTkLabel(text=f"Version: {App_Version}\n{ShowUserInfo}\n", text_font=("sans-serif", 20))
        self.Aboutlabel_2.grid(column=1, row=2, padx=0, pady=0)

        self.Aboutlabel_3 = CTkLabel(text=f"Creator/Developer:\n{Developer}\n", text_font=("sans-serif", 20))
        self.Aboutlabel_3.grid(column=1, row=3, padx=0, pady=0)

        self.Aboutlabel_4 = CTkLabel(text=f"Last updated:\n{LastEditDate}", text_font=("sans-serif", 20))
        self.Aboutlabel_4.grid(column=1, row=4, padx=0, pady=0)

        self.Aboutbutton_2 = CTkButton(text="Check For Updates", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40,command=self.OpenUpdater)
        self.Aboutbutton_2.grid(column=1, row=5,padx=0, pady=20)
    def AboutGoBack(self):
        self.Aboutbutton_1.destroy()
        self.Aboutbutton_2.destroy()
        self.Aboutlabel_1.destroy()
        self.Aboutlabel_2.destroy()
        self.Aboutlabel_3.destroy()
        self.Aboutlabel_4.destroy()

        self.MainMenu()
    def SosialMedia(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()
        

        self.title(f"SML | v{App_Version}")

        self.SosialMediabutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.SosialMediaGoBack)
        self.SosialMediabutton_1.grid(column=1, row=0, padx=0, pady=PADY_SETTINGS)

        self.SosialMediabutton_2 = CTkButton(text="Discord", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.discord)
        self.SosialMediabutton_2.grid(column=1, row=1, padx=0, pady=PADY_SETTINGS)

        self.SosialMediabutton_3 = CTkButton(text="Github", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.github)
        self.SosialMediabutton_3.grid(column=1, row=2, padx=0, pady=PADY_SETTINGS)

        self.SosialMediabutton_4 = CTkButton(text="Instagram", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.instagram)
        self.SosialMediabutton_4.grid(column=1, row=3, padx=0, pady=PADY_SETTINGS)

        self.SosialMediabutton_5 = CTkButton(text="YouTube", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.youtube)
        self.SosialMediabutton_5.grid(column=1, row=4, padx=0, pady=PADY_SETTINGS)

        self.SosialMediabutton_6 = CTkButton(text="Website", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.OpenSite)
        self.SosialMediabutton_6.grid(column=1, row=5, padx=0, pady=PADY_SETTINGS)

        self.SosialMediabutton_7 = CTkButton(text="TikTok", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.TikTok)
        self.SosialMediabutton_7.grid(column=1, row=6, padx=0, pady=PADY_SETTINGS)
    def SosialMediaGoBack(self):
        self.SosialMediabutton_1.destroy()
        self.SosialMediabutton_2.destroy()
        self.SosialMediabutton_3.destroy()
        self.SosialMediabutton_4.destroy()
        self.SosialMediabutton_5.destroy()
        self.SosialMediabutton_6.destroy()
        self.SosialMediabutton_7.destroy()

        self.MainMenu()
    def Apps(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"Apps | v{App_Version}")

        self.AppsBackbutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.AppsGoBack)
        self.AppsBackbutton_1.grid(column=1, row=1, padx=0, pady=0)

        self.Appsbutton_1 = CTkButton(text="YT Downloader", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.YTDownloader)
        self.Appsbutton_1.grid(column=1, row=2, padx=0, pady=30)

        self.Appsbutton_2 = CTkButton(text="J.A.R.V.I.S", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.Jarvis)
        self.Appsbutton_2.grid(column=1, row=3, padx=0, pady=0)
    def AppsGoBack(self):
        self.AppsBackbutton_1.destroy()
        self.Appsbutton_1.destroy()
        self.Appsbutton_2.destroy()

        self.MainMenu()
    def GameLauncher(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()

        self.title(f"GL | v{App_Version}")
        self.geometry("230x450")

        self.GameMediabutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.GameGoBack)
        self.GameMediabutton_1.grid(column=1, row=0, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_2 = CTkButton(text="Rocket League", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_1)
        self.GameMediabutton_2.grid(column=1, row=1, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_3 = CTkButton(text="ARK", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_2)
        self.GameMediabutton_3.grid(column=1, row=2, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_4 = CTkButton(text="Destiny 2", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_3)
        self.GameMediabutton_4.grid(column=1, row=3, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_5 = CTkButton(text="Fall Guys", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_4)
        self.GameMediabutton_5.grid(column=1, row=4, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_6 = CTkButton(text="Warships", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_5)
        self.GameMediabutton_6.grid(column=1, row=5, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_7 = CTkButton(text="Control", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_6)
        self.GameMediabutton_7.grid(column=1, row=6, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_8 = CTkButton(text="GTA5", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_7)
        self.GameMediabutton_8.grid(column=1, row=7, padx=0, pady=PADY_SETTINGS)

        self.GameMediabutton_9 = CTkButton(text="War Thunder", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.LaunchGame_8)
        self.GameMediabutton_9.grid(column=1, row=8, padx=0, pady=PADY_SETTINGS)
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

        self.MainMenu()
    def SystemSettings(self):
        self.Mbutton_1.destroy()
        self.Mbutton_2.destroy()
        self.Mbutton_3.destroy()
        self.Mbutton_4.destroy()
        self.Mbutton_5.destroy()
        self.Mbutton_6.destroy()
        self.Mbutton_7.destroy()
        

        self.title(f"SS | v{App_Version}")
        self.geometry("230x550")

        self.Systembutton_1 = CTkButton(text="Go Back", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.SystemSettingsGoBack)
        self.Systembutton_1.grid(column=1, row=0, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_2 = CTkButton(text="App Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.AppSettings)
        self.Systembutton_2.grid(column=1, row=1, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_3 = CTkButton(text="VPN Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.VPNSettings)
        self.Systembutton_3.grid(column=1, row=2, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_4 = CTkButton(text="TaskManager", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.TaskManager)
        self.Systembutton_4.grid(column=1, row=3, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_5 = CTkButton(text="NetDrive Reset", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.ResetNetworkDrive)
        self.Systembutton_5.grid(column=1, row=4, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_6 = CTkButton(text="Power Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.PowerSettings)
        self.Systembutton_6.grid(column=1, row=5, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_7 = CTkButton(text="Sound Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.SoundSettings)
        self.Systembutton_7.grid(column=1, row=6, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_8 = CTkButton(text="Storage Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.StorageSettings)
        self.Systembutton_8.grid(column=1, row=7, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_9 = CTkButton(text="Display Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.DisplaySettings)
        self.Systembutton_9.grid(column=1, row=8, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_10 = CTkButton(text="Network Settings", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.NetworkSettings)
        self.Systembutton_10.grid(column=1, row=9, padx=0, pady=PADY_SETTINGS)

        self.Systembutton_11 = CTkButton(text="Windows Update", fg_color=("gray75", "gray30"), text_font=("sans-serif", 17), corner_radius=0, width=240, height=40, command=self.WindowsUpdate)
        self.Systembutton_11.grid(column=1, row=10, padx=0, pady=PADY_SETTINGS)
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
        startfile("Updater.exe")
        sleep(0.3)
        file.close()
        self.destroy()
    def YTDownloader(self):
        startfile("YT_Downloader.py")
        sleep(0.3)
        file.close()
        self.destroy()
    def Jarvis(self):
        startfile("Jarvis.py")
        sleep(0.3)
        file.close()
        self.destroy()
    def NormalGUI(self):
        startfile("Management_Panel.py")
        sleep(0.3)
        file.close()
        self.destroy()
    def LaunchGame_1(self):
        webbrowser.open(Game_1)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_2(self):
        webbrowser.open(Game_2)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_3(self):
        webbrowser.open(Game_3)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_4(self):
        webbrowser.open(Game_4)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_5(self):
        webbrowser.open(Game_5)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_6(self):
        webbrowser.open(Game_6)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_7(self):
        webbrowser.open(Game_7)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def LaunchGame_8(self):
        webbrowser.open(Game_8)
        notification.notify("Management Panel", "Your game is launching.\nPlease wait while your game launches", timeout=6)
    def on_closing(self, event=0):
        print(CLR_RED + "\n  GUI is being terminated" + RESET_ALL)
        file.close()
        self.destroy()
        exit()


    def __init__(self):
        super().__init__()

        self.geometry("230x350+400+150")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.resizable(0, 0)

        print(CLR_GREEN + "\n  GUI was launched Successfully" + RESET_ALL)

        self.MainMenu()


if __name__ == "__main__":
    app = App()
    app.mainloop()