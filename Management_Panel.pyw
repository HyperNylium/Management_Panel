###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Author/Creator: HyperNylium
###
### Website: http://www.hypernylium.com/
###
### GitHub: https://github.com/HyperNylium/
###
### CustomTkinter Version: 4.6.2 => 5.1.3 update
###
### License: Mozilla Public License Version 2.0
###
###
### TODO: Make the YT Downloader tab download audio files in a valid way rather than just downloading the video with only audio and converting it to audio
### DONE: Make a auto updater script that updates the main app instead of the user needing to go to github and download the new version
### DONE: Make a LaunchAtLogin setting in the settings.json file. This will create a shortcut in the startup folder (shell:startup) to launch the app on startup
### DONE: Make a Music tab that allows you to play music from a folder
### DONE: Fix window maximize issue on launch
### DONE: Fix assistant text boxes not being able to move up and down when the window height is changed
### DONE: make a check for updates function that checks for updates once clicked by a button instead of on launch
### DONE: when closing also save the width and height of the window for next launch in the settings.json
### DONE: make a dropdown menu in the settings tab for changing the default open tab on launch
### DONE: make all window.after() use schedule_create() instead
### DONE: finish making the app responsive
### DISREGARDED: Instead of using tkinter.messagebox use CTkMessagebox (Didn't work out as i hoped it did. The library is not at fault, i just didn't like the way it worked)
###
###
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# Imports
from os import system, startfile, execl, mkdir, rename, listdir, remove, getcwd, walk, makedirs
from os.path import exists, join, splitext, expanduser, relpath
from tkinter.messagebox import showerror, askyesno, showinfo
from subprocess import Popen, PIPE, CREATE_NO_WINDOW
from tkinter import BooleanVar, DoubleVar, IntVar
from json import load as JSload, dump as JSdump
from threading import Thread, Timer as TD_Timer
from datetime import datetime, date, timedelta
from tkinter.filedialog import askdirectory
from webbrowser import open as WBopen
from zipfile import ZipFile
from copy import deepcopy
from shutil import copy2
from time import sleep
import sys

try:
    from customtkinter import (
        CTk,
        CTkToplevel,
        CTkFrame, 
        CTkScrollableFrame, 
        CTkLabel, 
        CTkButton, 
        CTkImage, 
        CTkEntry, 
        CTkSwitch, 
        CTkOptionMenu, 
        CTkProgressBar, 
        CTkTextbox, 
        CTkSlider, 
        set_appearance_mode
    )
    from PIL.Image import open as PILopen, fromarray as PILfromarray
    from winshell import desktop, CreateShortcut, startup
    from watchdog.events import FileSystemEventHandler
    from pytube import YouTube as PY_Youtube
    from requests.exceptions import Timeout
    from watchdog.observers import Observer
    from pygame import mixer as pygmixer
    from pyttsx3 import init as ttsinit
    from numpy import array as nparray
    from plyer import notification
    from requests import get
    import openai
except ImportError as importError:
    ModuleNotFound = str(importError).split("'")[1]
    showerror(title="Import error", message=f"An error occurred while importing '{ModuleNotFound}'")
    sys.exit()

# Minimizes console window that launches with .py files if you want to use this app as a .py instead of a .pyw file
# ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 6)

# Sets the appearance mode of the window to dark 
# (in simpler terms, sets the window to dark mode).
# Don't want to burn them eyes now do we?
set_appearance_mode("dark") 

CurrentAppVersion = "4.2.3"
UpdateLink = "https://github.com/HyperNylium/Management_Panel"
DataTXTFileUrl = "http://www.hypernylium.com/projects/ManagementPanel/assets/data.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

SETTINGSFILE = "settings.json"
model_prompt = "Hello, how can I help you today?"
UserDesktopDir = desktop()
UserStartupDir = startup() # shell:startup
devices_per_row = 2  # Maximum number of devices per ro
DeviceFrames = []  # List to store references to DeviceFrame frames
devices = {} # dict to store device info (battey persetage, type)
after_events = {} # dict to store after events
all_buttons: list[CTkButton] = [] # list to store all buttons in the navigation bar
all_buttons_text: list[str] = [] # list to store all buttons text in the navigation bar
all_frames = ["Home", "Games", "Social Media", "YT Downloader", "Assistant", "Music", "Devices", "System", "Settings"] # list to store all frames
prev_x = 0 # variable to store previous x coordinate of the window
prev_y = 0 # variable to store previous y coordinate of the window
AppsLaucherGUISetup_max_buttons_per_row = 3 # Maximum number of buttons per row in the "Games" and "Social Media" frames
AppsLaucherGUISetup_row_num = 0 # Current row number in the "Games" and "Social Media" frames
AppsLaucherGUISetup_col_num = 0 # Current column number in the "Games" and "Social Media" frames

class SettingsFileEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.modified_event_pending = False

    def on_modified(self, event):
        if event.src_path.endswith(SETTINGSFILE) and not self.modified_event_pending:
            self.modified_event_pending = True
            TD_Timer(1, self.reload_settings).start()

    def reload_settings(self):
        if exists(SETTINGSFILE):
            global settings
            try:
                with open(SETTINGSFILE, 'r') as settings_file:
                    new_settings = JSload(settings_file)
                if new_settings != settings:
                    if exists(new_settings["MusicSettings"]["MusicDir"]) or new_settings["MusicSettings"]["MusicDir"] == "":
                        settings = deepcopy(new_settings)
                        music_manager.musicmanager("update")
                del new_settings
            except Exception as e:
                print("Error reloading settings:", e)
        self.modified_event_pending = False
class TitleUpdater:
    def __init__(self, label: CTkLabel = None):
        if label is not None:
            self.label = label
        else:
            raise ValueError("label cannot be None")

    def start(self):
        """starts the time and date thread for infinite loop"""
        Thread(target=self.loop, daemon=True, name="TitleUpdater").start()

    def loop(self):
        while True:
            self.update()
            sleep(1)

    def update(self):
        """"Updates the title of the window to the current time and date"""
        if self.label is not None:
            if settings["AppSettings"]["NavigationState"] == "close":
                current_time = datetime.now().strftime('%I:%M %p')
                current_date = date.today().strftime('%d/%m/%Y')
            else:
                current_time = datetime.now().strftime('%I:%M:%S %p')
                current_date = date.today().strftime('%a, %b %d, %Y')
            self.label.configure(text=f"{current_date}\n{current_time}")
class MusicManager:
    def __init__(self):
        self.song_info = {}  # Dictionary to store song info: {"song_name": {"duration": duration_in_seconds}}
        self.current_song_index = 0
        self.current_song_paused = False
        self.has_started_before = False
        self.updating = False
        pygmixer.init()
        pygmixer.music.set_volume(float(int(settings["MusicSettings"]["Volume"]) / 100))

    def cleanup(self):
        try:
            pygmixer.music.stop()
            pygmixer.quit()
        except: pass
        return

    def main_event_loop(self):
        while True:
            if pygmixer.music.get_busy() and not self.current_song_paused:
                current_pos_secs = pygmixer.music.get_pos() / 1000  # Get current position in seconds
                total_duration = self.song_info[self.song_list[self.current_song_index]]["duration"]
                remaining_time = total_duration - current_pos_secs

                formatted_remaining_time = str(timedelta(seconds=remaining_time)).split(".")[0]
                formatted_total_duration = str(timedelta(seconds=total_duration)).split(".")[0]

                time_left_label.configure(text=formatted_remaining_time)
                song_progressbar.set((current_pos_secs / total_duration))
                total_time_label.configure(text=formatted_total_duration)
            if pygmixer.music.get_pos() == -1 and self.current_song_paused is False and self.has_started_before is True:
                if settings["MusicSettings"]["LoopState"] == "all":
                    # This is where the infinite loop around all the music in your music dir happens.
                    # Almost like replaying a playlist infinitely.
                    # But the playlist is your music folder.
                    # So, after the last song is done playing in your music dir, 
                    # it will come back to the first song and play that. 
                    # It will do this infinitely.
                    self.musicmanager("next")
                elif settings["MusicSettings"]["LoopState"] == "one":
                    # This is where the infinite loop around the currently playing song happens.
                    # After the current song is done playing, it will start playing it again after it finishes.
                    # You can still change the song by clicking the next or previous button.
                    # And that new song will be the new song to be played infinitely.
                    pygmixer.music.stop()
                    self.musicmanager("play")
                elif settings["MusicSettings"]["LoopState"] == "off":
                    # When the song finishes playing, it will stop playing music
                    # until either you click the Play button or the Next button.
                    pygmixer.music.stop()
                    pre_song_btn.configure(state="disabled")
                    next_song_btn.configure(state="disabled")
                    play_pause_song_btn.configure(image=playimage, command=lambda: music_manager.musicmanager("play"))
                    if self.updating is False:
                        SaveSettingsToJson("CurrentlyPlaying", "False")
            sleep(1)

    def start_event_loops(self):
        Thread(target=self.main_event_loop, daemon=True, name="MusicManager_main_event_loop").start()

    def update(self):
        MusicDir_exists = exists(settings["MusicSettings"]["MusicDir"])
        if MusicDir_exists:
            self.song_list = [f for f in listdir(settings["MusicSettings"]["MusicDir"]) if f.endswith((".mp3", ".m4a"))]
            for song_name in self.song_list:
                self.song_info[song_name] = {"duration": pygmixer.Sound(join(settings["MusicSettings"]["MusicDir"], song_name)).get_length()}
        else:
            self.song_list = []
        for widget in all_music_frame.winfo_children():
            widget.destroy()
        for index, song_name in enumerate(self.song_list):
            CTkLabel(all_music_frame, text=f"{index+1}. {song_name}", font=("sans-serif", 20)).grid(row=self.song_list.index(song_name), column=1, padx=(20, 0), pady=5, sticky="w")
        update_music_list.configure(state="normal")
        change_music_dir.configure(state="normal")
        play_pause_song_btn.configure(state="normal")
        volume_slider.configure(state="normal")
        currently_playing_label.configure(text=f"Currently Playing: {self.song_list[self.current_song_index] if self.has_started_before is True and MusicDir_exists is True > 0 else 'None'}")
        music_dir_label.configure(text=f"Music Directory: {shorten_path(settings['MusicSettings']['MusicDir'], 25)}" if settings['MusicSettings']['MusicDir'] != "" else "Music Directory: None")
        del MusicDir_exists
        if settings["MusicSettings"]["CurrentlyPlaying"] == "True":
            self.musicmanager("play")
        self.updating = False

    def musicmanager(self, action: str):
        if action == "play" and len(self.song_list) > 0:
            if self.current_song_paused is True:
                pygmixer.music.unpause()
                self.current_song_paused = False
            else:
                pygmixer.music.load(join(settings["MusicSettings"]["MusicDir"], self.song_list[self.current_song_index]))
                pygmixer.music.play()
                currently_playing_label.configure(text=f"Currently Playing: {self.song_list[self.current_song_index]}")
                self.has_started_before = True
                self.current_song_paused = False
            pre_song_btn.configure(state="normal")
            next_song_btn.configure(state="normal")
            play_pause_song_btn.configure(image=pauseimage, command=lambda: music_manager.musicmanager("pause"))
            SaveSettingsToJson("CurrentlyPlaying", "True")
        elif action == "pause":
            if self.current_song_paused is False:
                pygmixer.music.pause()
                self.current_song_paused = True
            else:
                self.current_song_paused = False
                self.musicmanager("play")
            pre_song_btn.configure(state="disabled")
            next_song_btn.configure(state="disabled")
            play_pause_song_btn.configure(image=playimage, command=lambda: music_manager.musicmanager("play"))
            if self.updating is False:
                SaveSettingsToJson("CurrentlyPlaying", "False")
        elif action == "next":
            if len(self.song_list) > 0:
                pygmixer.music.stop()
                self.current_song_index = (self.current_song_index + 1) % len(self.song_list)
                self.musicmanager("play")
        elif action == "previous":
           if len(self.song_list) > 0:
                pygmixer.music.stop()
                self.current_song_index = (self.current_song_index - 1) % len(self.song_list)
                self.musicmanager("play")
        elif action == "volume":
            def savevolume():
                SaveSettingsToJson("Volume", musicVolumeVar.get())
            pygmixer.music.set_volume(float(musicVolumeVar.get() / 100))
            volume_label.configure(text=f"{musicVolumeVar.get()}%")
            schedule_cancel(window, savevolume)
            schedule_create(window, 420, savevolume)

        elif action == "loop":
            self.loopstate = settings["MusicSettings"]["LoopState"]
            if self.loopstate == "all":
                loop_playlist_btn.configure(image=CTkImage(change_image_clr(PILopen('assets/MusicPlayer/loop-1.png'), "#00ff00"), size=(25, 25)))
                SaveSettingsToJson("LoopState", "one")
            elif self.loopstate == "one":
                loop_playlist_btn.configure(image=CTkImage(change_image_clr(PILopen('assets/MusicPlayer/loop.png'), "#ff0000"), size=(25, 25)))
                SaveSettingsToJson("LoopState", "off")
            elif self.loopstate == "off":
                loop_playlist_btn.configure(image=CTkImage(change_image_clr(PILopen('assets/MusicPlayer/loop.png'), "#00ff00"), size=(25, 25)))
                SaveSettingsToJson("LoopState", "all")
            del self.loopstate

        elif action == "changedir":
            if settings["MusicSettings"]["MusicDir"] != "" and exists(settings["MusicSettings"]["MusicDir"]):
                tmp_music_dir = askdirectory(title="Select Your Music Directory", initialdir=settings["MusicSettings"]["MusicDir"])
            else:
                tmp_music_dir = askdirectory(title="Select Your Music Directory", initialdir=expanduser("~"))
            if tmp_music_dir != "":
                SaveSettingsToJson("MusicDir", tmp_music_dir)
                self.musicmanager("update")
        elif action == "update":
            self.updating = True
            update_music_list.configure(state="disabled")
            change_music_dir.configure(state="disabled")
            pre_song_btn.configure(state="disabled")
            play_pause_song_btn.configure(state="disabled")
            next_song_btn.configure(state="disabled")
            volume_slider.configure(state="disabled")
            currently_playing_label.configure(text="Status: Scanning files...")
            song_progressbar.set(0.0)
            time_left_label.configure(text="0:00")
            total_time_label.configure(text="0:00")
            if pygmixer.music.get_busy() and not self.current_song_paused:
                self.musicmanager("pause")
            Thread(target=self.update, daemon=True, name="MusicManager_update").start()
        else:
            pass

def StartUp():
    """Reads settings.json and loads all the variables into the settings variable.\n
    If the file isn't found, it creates one within the same directory and loads it with default values.\n
    settings[Property][Key] => value\n
    settings['AppSettings']['AlwaysOnTop'] => True | False"""

    try:
        window.iconbitmap("assets/AppIcon/Management_Panel_Icon.ico")
    except Exception as e:
        showerror(title="Error loading window icon", message=f"An error occurred while loading the window icon\n{e}")
        sys.exit()

    settings_loaded = False

    def load_settings():
        nonlocal settings_loaded
        global observer, settings
        default_settings = {
            "URLs": {
                "HyperNylium.com": "http://hypernylium.com/",
                "Github": "https://github.com/HyperNylium",
                "Discord": "https://discord.gg/4FHTjAgw95",
                "Instagram": "https://www.instagram.com/",
                "Youtube": "https://www.youtube.com/",
                "TikTok": "https://www.tiktok.com/",
                "Facebook": "https://www.facebook.com/",
                "Twitter": "https://twitter.com/"
            },
            "GameShortcutURLs": {
                "Game 1": "",
                "Game 2": "",
                "Game 3": "",
                "Game 4": "",
                "Game 5": "",
                "Game 6": "",
                "Game 7": "",
                "Game 8": "",
                "Game 9": ""
            },
            "OpenAISettings": {
                "VoiceType": 0,
                "OpenAI_API_Key": "",
                "OpenAI_model_engine": "text-davinci-003",
                "OpenAI_Max_Tokens": 1024,
                "OpenAI_Temperature": 0.5
            },
            "MusicSettings": {
                "MusicDir": "",
                "Volume": 0,
                "CurrentlyPlaying": "False",
                "LoopState": "all"
            },
            "AppSettings": {
                "PreviouslyUpdated": "False",
                "AlwaysOnTop": "False",
                "LaunchAtLogin": "False",
                "SpeakResponce": "False",
                "CheckForUpdatesOnLaunch": "True",
                "NavigationState": "open",
                "DownloadsFolderName": "YT_Downloads",
                "DefaultFrame": "Home",
                "Alpha": 1.0,
                "Window_State": "normal",
                "Window_Width": "",
                "Window_Height": "",
                "Window_X": "",
                "Window_Y": ""
            },
            "Devices": []
        }
        event_handler = SettingsFileEventHandler()
        observer = Observer()
        observer.schedule(event_handler, path='.', recursive=False)
        observer.start()
        try:
            with open(SETTINGSFILE, 'r') as settings_file:
                settings = JSload(settings_file)

            if settings["AppSettings"]["PreviouslyUpdated"] == "True":
                for Property in default_settings:
                    if Property not in settings:
                        settings[Property] = default_settings[Property]
                    else:
                        for key in default_settings[Property]:
                            if key not in settings[Property]:
                                settings[Property][key] = default_settings[Property][key]
                settings["AppSettings"]["PreviouslyUpdated"] = "False"
                with open(SETTINGSFILE, 'w') as settings_file:
                    JSdump(settings, settings_file, indent=2)
                restart(pass_args=False)

        except FileNotFoundError:
            with open(SETTINGSFILE, 'w') as settings_file:
                JSdump(default_settings, settings_file, indent=2)
            settings = default_settings
        settings_loaded = True
        observer.join()

    Thread(target=load_settings, name="settings_thread", daemon=True).start()

    global UserPowerPlans, settingsSpeakResponceVar, settingsAlwayOnTopVar, settingslaunchwithwindowsvar, settingsCheckForUpdates, settingsAlphavar, musicVolumeVar, music_manager
    settingsSpeakResponceVar = BooleanVar()
    settingsAlwayOnTopVar = BooleanVar()
    settingslaunchwithwindowsvar = BooleanVar()
    settingsCheckForUpdates = BooleanVar()
    settingsAlphavar = DoubleVar()
    musicVolumeVar = IntVar()

    UserPowerPlans = GetPowerPlans()

    while not settings_loaded:
        sleep(0.3)

    if settings["AppSettings"]["AlwaysOnTop"] == "True":
        window.attributes('-topmost', True)
        settingsAlwayOnTopVar.set(True)

    if settings["AppSettings"]["LaunchAtLogin"] == "True":
        settingslaunchwithwindowsvar.set(True)
    elif exists(join(UserStartupDir, "Management_Panel.lnk")):
        usr_res = askyesno(title="Management_Panel: Startup shortcut found", message="Even though the 'LaunchAtLogin' setting is turned off\nwe have found a shortcut that launches this app when you login in your startup folder.\nWould you like the app to still lauch on login?")
        if usr_res is True:
            SaveSettingsToJson("LaunchAtLogin", "True")
            settingslaunchwithwindowsvar.set(True)
        else:
            try:
                remove(join(UserStartupDir, "Management_Panel.lnk"))
            except FileNotFoundError:
                pass

    if settings["AppSettings"]["SpeakResponce"] == "True":
        settingsSpeakResponceVar.set(True)

    if isinstance(settings["MusicSettings"]["Volume"], int):
        musicVolumeVar.set(settings["MusicSettings"]["Volume"])
    elif isinstance(settings["MusicSettings"]["Volume"], float):
        musicVolumeVar.set(int(settings["MusicSettings"]["Volume"]))

    CheckForUpdatesOnLaunch = str(settings["AppSettings"]["CheckForUpdatesOnLaunch"])
    check_for_updates(CheckForUpdatesOnLaunch)
    settingsCheckForUpdates.set(CheckForUpdatesOnLaunch)
    del CheckForUpdatesOnLaunch

    music_manager = MusicManager()
def check_for_updates(option: str):
    global LiveAppVersion, Developer, LastEditDate, ShowUserInfo
    if option == "True":
        try:
            response = get(DataTXTFileUrl, timeout=3, headers=headers)
            lines = response.text.split('\n')
            delimiter = "="

            for line in lines:
                key_value = line.split(delimiter, 1)
                if len(key_value) == 2:
                    key = key_value[0].strip()
                    value = key_value[1].strip().replace(" ", "")
                    if key == "Version":
                        LiveAppVersion = value
                    elif key == "DevName":
                        Developer = value
                    elif key == "LastEditDate":
                        LastEditDate = value
            if LiveAppVersion < CurrentAppVersion:
                    Developer = "Unknown"
                    LastEditDate = "Unknown"
                    ShowUserInfo = "- Unauthentic"
            elif LiveAppVersion != CurrentAppVersion or LiveAppVersion > CurrentAppVersion:
                    ShowUserInfo = f"- Update available (v{LiveAppVersion})"
            else:
                ShowUserInfo = "- Latest version"
        except Timeout:
            showerror(title='Request timed out', message=f"Main data file request timed out\nThis can happen because:\n> You are offline\n> The webserver is not hosting the file at the moment\n> Your internet connection is slow\n\nThe app will now start in offline mode.")
            LiveAppVersion = "N/A"
            Developer = "N/A"
            LastEditDate = "N/A"
            ShowUserInfo = "- timed out"
        except Exception as e:
            showerror(title='Launching in offline mode', message=f"There was an error while retrieving the main data file\nThis can happen because:\n> You are offline\n> The webserver is not hosting the file at the moment\n\nThe app will now start in offline mode.")
            LiveAppVersion = "N/A"
            Developer = "N/A"
            LastEditDate = "N/A"
            ShowUserInfo = "- offline mode"
    elif option == "in-app":
        check_for_updates_button.configure(text="Checking for updates...", state="disabled")
        try:
            response = get(DataTXTFileUrl, timeout=3, headers=headers)
            lines = response.text.split('\n')
            delimiter = "="

            for line in lines:
                key_value = line.split(delimiter, 1)
                if len(key_value) == 2:
                    key = key_value[0].strip()
                    value = key_value[1].strip().replace(" ", "")
                    if key == "Version":
                        LiveAppVersion = value
                    elif key == "DevName":
                        Developer = value
                    elif key == "LastEditDate":
                        LastEditDate = value
            if LiveAppVersion < CurrentAppVersion:
                    Developer = "Unknown"
                    LastEditDate = "Unknown"
                    ShowUserInfo = "- Unauthentic"
            elif LiveAppVersion != CurrentAppVersion or LiveAppVersion > CurrentAppVersion:
                    ShowUserInfo = f"- Update available (v{LiveAppVersion})"
            else:
                ShowUserInfo = "- Latest version"
        except Timeout:
            LiveAppVersion = "N/A"
            Developer = "N/A"
            LastEditDate = "N/A"
            ShowUserInfo = "- timed out"
        except Exception as e:
            LiveAppVersion = "N/A"
            Developer = "N/A"
            LastEditDate = "N/A"
            ShowUserInfo = "- offline mode"
        home_frame_label_1.configure(text=f"Version: {CurrentAppVersion} {ShowUserInfo}")
        home_frame_label_2.configure(text=f"Creator/developer: {Developer}")
        home_frame_label_3.configure(text=f"Last updated: {LastEditDate}")
        check_for_updates_button.configure(text="Check complete", state="disabled")
        schedule_create(window, 3500, lambda: check_for_updates_button.configure(text="Check for updates", state="normal"), True)
    else:
        LiveAppVersion = "N/A"
        Developer = "N/A"
        LastEditDate = "N/A"
        ShowUserInfo = "- Check disabled"
def restart(pass_args=True):
    """Restarts app"""
    python = sys.executable
    print(python)
    print(sys.argv)
    sleep(3)
    if pass_args is True:
        execl(python, python, *sys.argv)
    else:
        execl(python, python, sys.argv[0])
def on_closing():
    """App termination function"""
    SaveSettingsToJson("CurrentlyPlaying", "False")
    try: 
        observer.stop()
    except: pass
    music_manager.cleanup()
    window.destroy()
    sys.exit()
def schedule_create(widget, ms, func, cancel_after_finished=False, *args, **kwargs):
    """Schedules a function to run after a given time in milliseconds and saves the event id in a dictionary with the function name as the key"""
    event_id = widget.after(ms, lambda: func(*args, **kwargs))
    after_events[func.__name__] = event_id
    if cancel_after_finished:
        widget.after(ms, lambda: schedule_cancel(widget, func))
def schedule_cancel(widget, func):
    """Cancels a scheduled function and deletes the event id from the dictionary using the function name as the parameter instead of the event id"""
    try:
        event_id = after_events.get(func.__name__)
        if event_id is not None:
            widget.after_cancel(event_id)
            del after_events[func.__name__]
    except: 
        pass
def NavbarAction(option: str):
    """Opens or closes the navigation bar and saves the state to settings.json"""
    SaveSettingsToJson("NavigationState", str(option))
    if option == "close":
        for button in all_buttons:
            button.configure(text="", anchor="center")
        navigation_frame_label.pack_configure(padx=7)
        navigation_frame_label.configure(font=("sans-serif", 15, "bold"))
        close_open_nav_button.configure(image=openimage, command=lambda: NavbarAction("open"))
        window.minsize(550, 420)
    elif option == "open":
        for button in all_buttons:
            button.configure(text=all_buttons_text[all_buttons.index(button)], anchor="w")
        navigation_frame_label.pack_configure(padx=20)
        navigation_frame_label.configure(font=("sans-serif", 18, "bold"))
        close_open_nav_button.configure(image=closeimage, command=lambda: NavbarAction("close"))
        window.minsize(650, 420)
    title_bar.update()

def on_drag_end(event):
    global prev_x, prev_y

    # Check if x and y values have changed
    if prev_x != event.x or prev_y != event.y:
        # Update the x and y values
        prev_x = event.x
        prev_y = event.y

        # The main point about the upcoming code is that when you start to
        # drag the window, it first cancels any existing function call to on_drag_stopped()
        # but then creates a new one right after that. This means that instead of the on_drag_stopped()
        # function being called every single pixel you move the window, it will
        # be called only after the window has stopped moving for 420ms.
        # this happens because the on_drag_end() gets called probably hundreds of times
        # you move the window. But with this code, it will only call the on_drag_stopped()
        # function once after you stop moving the window for 420ms because it keeps cancelling
        # the function call before it can even start. Cool, right? This is a more modefied version
        # so it works with this project (i am sure it would work with any project though)
        # you can find the full version that was built with tkinter and uses the .after() method
        # intead of my custom schedule_create() and schedule_cancel() functions here: https://github.com/HyperNylium/tkinter-window-drag-detection

        # Cancel any existing threshold check
        schedule_cancel(window, on_drag_stopped)

        # Schedule a new threshold check after 420ms
        schedule_create(window, 420, on_drag_stopped)
    return
def on_drag_stopped():
    if window.state() == "zoomed":
        SaveSettingsToJson("Window_State", "maximized")
    elif window.state() == "normal":
        SaveSettingsToJson("Window_State", "normal")
        SaveSettingsToJson("Window_Width", window.winfo_width())
        SaveSettingsToJson("Window_Height", window.winfo_height())
        SaveSettingsToJson("Window_X", window.winfo_x())
        SaveSettingsToJson("Window_Y", window.winfo_y())
    return

def systemsettings(setting: str):
    """Launches different settings within windows 10 and 11 (only tested on windows 11)"""
    if setting == "power":
        Popen(
            "cmd.exe /c control powercfg.cpl",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "display":
        Popen(
            "cmd.exe /c control desk.cpl",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "network":
        Popen(
            "cmd.exe /c %systemroot%\system32\control.exe /name Microsoft.NetworkAndSharingCenter",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "sound":
        Popen(
            "cmd.exe /c control mmsys.cpl sounds",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "apps":
        Popen(
            "cmd.exe /c start ms-settings:appsfeatures",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )  # Put "appwiz.cpl" for control center version
    elif setting == "storage":
        Popen(
            "cmd.exe /c start ms-settings:storagesense",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "windowsupdate":
        Popen(
            "cmd.exe /c %systemroot%\system32\control.exe /name Microsoft.WindowsUpdate",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "taskmanager":
        Popen(
            "cmd.exe /c taskmgr",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "vpn":
        Popen(
            "cmd.exe /c start ms-settings:network-vpn",
            stdout=PIPE,
            stderr=PIPE,
            stdin=PIPE,
            creationflags=CREATE_NO_WINDOW,
        )
    elif setting == "netdrive":
        system("cmd.exe /c netdrive --reset")
        showinfo(
            title="Network drives reset", message="All network drives have been reset"
        )
    else:
        pass
def LaunchGame(GameVar: str):
    """Launches selected game"""
    if GameVar == None or GameVar == "":
        showerror(
            title="No game link found",
            message="Make sure you have configured a game shortcut link in you're settings and try restarting the app",
        )
    else:
        WBopen(GameVar)
        notification.notify(
            "Management Panel", "Your game is now launching.", timeout=6
        )
def SocialMediaLoader(MediaVar: str):
    """Launches a website URL (either http or https)"""
    WBopen(MediaVar)

def CenterWindowToDisplay(Screen: CTk, width: int, height: int, scale_factor: float = 1.0):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int(((screen_width/2) - (width/2)) * scale_factor)
    y = int(((screen_height/2) - (height/1.5)) * scale_factor)
    return f"{width}x{height}+{x}+{y}"
def CenterWindowToMain(Screen: CTkToplevel, width: int, height: int):
    """Centers the window to the main tkinter window"""
    main_screen_width = Screen.winfo_width()
    main_screen_height = Screen.winfo_height()
    main_screen_X = Screen.winfo_x()
    main_screen_Y = Screen.winfo_y()
    x = main_screen_X + (main_screen_width - width) // 2
    y = main_screen_Y + (main_screen_height - height) // 2
    return f"{width}x{height}+{int(x)}+{int(y)}"
def ResetWindowPos():
    """Resets window positions in settings.json"""
    SaveSettingsToJson("Window_State", "normal")
    SaveSettingsToJson("Window_Width", "")
    SaveSettingsToJson("Window_Height", "")
    SaveSettingsToJson("Window_X", "")
    SaveSettingsToJson("Window_Y", "")
    settingsresetwindowbtn.configure(state="disabled", text="Window position reset")
    restart()

def AppsLaucherGUISetup(frame: str):
    global AppsLaucherGUISetup_row_num, AppsLaucherGUISetup_col_num

    if frame == "games_frame":
        frame = games_frame
        key = "GameShortcutURLs"
        cmd = LaunchGame
    elif frame == "socialmedia_frame":
        frame = socialmedia_frame
        key = "URLs"
        cmd = SocialMediaLoader
    else:
        return

    for url_name, url in settings[key].items():
        CTkButton(frame, width=200, text=url_name, compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: cmd(url)).grid(row=AppsLaucherGUISetup_row_num, column=AppsLaucherGUISetup_col_num, padx=5, pady=10)
        AppsLaucherGUISetup_col_num += 1
        if AppsLaucherGUISetup_col_num >= AppsLaucherGUISetup_max_buttons_per_row:
            AppsLaucherGUISetup_col_num = 0
            AppsLaucherGUISetup_row_num += 1

    AppsLaucherGUISetup_row_num = 0
    AppsLaucherGUISetup_col_num = 0
    del frame, key, cmd

def AlwaysOnTopTrueFalse():
    """Sets the window to always be on top or not and saves the state to settings.json"""
    value = settingsAlwayOnTopVar.get()
    window.attributes('-topmost', value)
    SaveSettingsToJson("AlwaysOnTop", str(value))
    del value
    return
def LaunchOnStartupTrueFalse():
    value = settingslaunchwithwindowsvar.get()
    if value is True:
        if getattr(sys, 'frozen', False):
            target = sys.executable
        else:
            target = __file__
        CreateShortcut(
            Path=join(UserStartupDir, "Management_Panel.lnk"),
            Target=target,
            StartIn=getcwd(),
            Description="Shortcut for launching 'Management_Panel.pyw'",
            Icon=(join(getcwd(), "assets", "AppIcon", "Management_Panel_Icon.ico"), 0),
        )
    else:
        try:
            remove(join(UserStartupDir, "Management_Panel.lnk"))
        except FileNotFoundError:
            pass

    SaveSettingsToJson("LaunchAtLogin", str(value))
    del value
    return
def set_alpha(alpha_var: float):
    """Sets the window transparency and saves the state to settings.json"""
    def save_alpha_settings():
        SaveSettingsToJson("Alpha", alpha_var)
    window.attributes('-alpha', alpha_var)
    schedule_cancel(window, save_alpha_settings)
    schedule_create(window, 420, save_alpha_settings)
    del save_alpha_settings

def YTVideoDownloaderContentType(vidtype: str):
    """Updates the video content type to either .mp4 or .mp3 according to whatever was selected in the dropdown"""
    global YTVideoContentType
    YTVideoContentType = vidtype
def YTVideoDownloader(ContentType: str):
    """Downloads youtube videos and shows progress on GUI"""
    def DefaultStates(**kwargs):
        option = kwargs.get("option")
        if option == "YTReset":
            ytdownloader_progressbarpercentage.configure(text="0%")
            ytdownloader_progressbar.configure(progress_color="#1f6aa5")
            ytdownloader_progressbar.set(0)
            ytdownloader_progressbarpercentage.grid_forget()
            ytdownloader_progressbar.grid_forget()
            ytdownloader_OptionMenu.grid_configure(row=2, column=0, columnspan=2, padx=0, pady=0)
            ytdownloader_frame_button_1.grid_configure(row=3, rowspan=2, column=0, columnspan=2, padx=10, pady=20, sticky="ews")
            ytdownloader_entry.configure(state="normal")
            ytdownloader_OptionMenu.configure(state="normal")
            ytdownloader_frame_button_1.configure(text="Download", state="normal")
        elif option == "ErrorReset":
            ytdownloader_error_label.grid_forget()
            ytdownloader_OptionMenu.grid_configure(row=2, column=0, columnspan=2, padx=0, pady=0)
            ytdownloader_frame_button_1.grid_configure(row=3, rowspan=2, column=0, columnspan=2, padx=10, pady=20, sticky="ews")
            ytdownloader_entry.configure(state="normal")
            ytdownloader_OptionMenu.configure(state="normal")
            ytdownloader_frame_button_1.configure(text="Download", state="normal")
            window.update()
    def on_download_progress(stream, chunk, bytes_remaining):
        TotalSize = stream.filesize
        BytesDownloaded = TotalSize - bytes_remaining
        RawPersentage = BytesDownloaded / TotalSize * 100
        ConvertedPersentage = str(int(RawPersentage))
        ytdownloader_progressbarpercentage.configure(text=f"{ConvertedPersentage}%")
        ytdownloader_progressbar.set(float(ConvertedPersentage) / 100)
        ytdownloader_progressbarpercentage.update()
        ytdownloader_progressbar.update()
        ytdownloader_frame.update()
        if ConvertedPersentage == "100":
            ytdownloader_progressbar.configure(progress_color="green")
            ytdownloader_progressbar.update()
            schedule_create(window, 3500, DefaultStates, True, **{"option": "YTReset"})
    def YTDownloadThread():
        try:
            videourl = ytdownloader_entry.get().strip()
            if (videourl != "") and (videourl != None):
                ytdownloader_entry.configure(state="disabled")
                ytdownloader_OptionMenu.configure(state="disabled")
                ytdownloader_frame_button_1.configure(text="Downloading...", state="disabled")
                YTObject = PY_Youtube(videourl)
                CreatePath = join(UserDesktopDir, settings["AppSettings"]["DownloadsFolderName"])
                if not exists(CreatePath):
                    try:
                        mkdir(CreatePath)
                        mkdir(f"{CreatePath}\\Video")
                        mkdir(f"{CreatePath}\\Audio")
                    except OSError as error:
                        showerror(title="An error occurred", message=f"An error occurred while creating the downloads folder\nMore detailed error: {error}")
                        return
                if ContentType == "Video (.mp4)":
                    Video = YTObject.streams.get_by_resolution("720p")
                    VideoFilename = f"{CreatePath}\\Video\\{Video.default_filename}"
                    ytdownloader_OptionMenu.grid_configure(row=3, column=0, columnspan=2, padx=0, pady=0)
                    ytdownloader_frame_button_1.grid_configure(row=4, rowspan=2, column=0, columnspan=2, padx=10, pady=20, sticky="ews")
                    if exists(VideoFilename):
                        ytdownloader_error_label.configure(text=f"The video already exists", text_color="red")
                        ytdownloader_error_label.grid(row=2, column=0, columnspan=2, padx=0, pady=0)
                        schedule_create(window, 4000, DefaultStates, True, **{"option": "ErrorReset"})
                    else:
                        ytdownloader_progressbar.grid(row=2, column=0, columnspan=2, padx=20, pady=0, sticky="ew")
                        ytdownloader_progressbarpercentage.grid(row=2, column=0, columnspan=2, padx=0, pady=0)
                        DownloadThread = Thread(name="VidDownloadThread", daemon=True, target=lambda: Video.download(output_path=f"{CreatePath}\\Video"))
                        CallbackThread = Thread(name="VidCallbackThread", daemon=True, target=lambda: YTObject.register_on_progress_callback(on_download_progress))
                        DownloadThread.start()
                        CallbackThread.start()
                    ytdownloader_frame.update()
                elif ContentType == "Audio (.mp3)":
                    Audio = YTObject.streams.filter(only_audio=True).first()
                    BaseFilename, BaseFileext = splitext(Audio.default_filename)
                    YTVideoName = f"{CreatePath}\\Audio\\{Audio.default_filename}"
                    MP3Filename = f"{CreatePath}\\Audio\\{BaseFilename +'.mp3'}"
                    ytdownloader_OptionMenu.grid_configure(row=3, column=0, columnspan=2, padx=0, pady=0)
                    ytdownloader_frame_button_1.grid_configure(row=4, rowspan=2, column=0, columnspan=2, padx=10, pady=20, sticky="ews")
                    if (exists(YTVideoName)) or (exists(MP3Filename)):
                        ytdownloader_error_label.configure(text=f"The audio (.mp3/.mp4) already exists", text_color="red")
                        ytdownloader_error_label.grid(row=2, column=0, columnspan=2, padx=0, pady=0)
                        schedule_create(window, 4000, DefaultStates, True, **{"option": "ErrorReset"})
                    else:
                        def on_complete(stream, file_handle):
                            rename(file_handle, MP3Filename)
                        ytdownloader_progressbar.grid(row=2, column=0, columnspan=2, padx=20, pady=0, sticky="ew")
                        ytdownloader_progressbarpercentage.grid(row=2, column=0, columnspan=2, padx=0, pady=0)
                        CallbackThread = Thread(name="AudioCallbackThread", daemon=True, target=lambda: YTObject.register_on_progress_callback(on_download_progress))
                        DownloadThread = Thread(name="AudioDownloadThread", daemon=True, target=lambda: Audio.download(output_path=f"{CreatePath}\\Audio"))
                        CompleteCallbackThread = Thread(name="AudioCompleteCallbackThread", daemon=True, target=lambda: YTObject.register_on_complete_callback(on_complete))
                        CallbackThread.start()
                        DownloadThread.start()
                        CompleteCallbackThread.start()
                    ytdownloader_frame.update()
                else:
                    showerror(title="Unknown format", message=f"Format invalid. Only\nVideo: Video (.mp4)\nAudio = Audio (.mp3)")
                    return
        except Exception as viderror:
            viderror = str(viderror)
            if (viderror == "'streamingData'"):
                YTVideoDownloader(ContentType)
            elif (viderror == "regex_search: could not find match for (?:v=|\/)([0-9A-Za-z_-]{11}).*"):
                # showerror(title="URL error", message="The URL that you have inputed does not seem to be a vaild URL.\nPlease make sure you are inputing an actual URL from youtube")
                ytdownloader_OptionMenu.grid_configure(row=3, column=0, columnspan=2, padx=0, pady=0)
                ytdownloader_frame_button_1.grid_configure(row=4, rowspan=2, column=0, columnspan=2, padx=10, pady=20, sticky="ews")
                ytdownloader_error_label.configure(text=f"The link that you inputed is not a valid link", text_color="red")
                ytdownloader_error_label.grid(row=2, column=0, columnspan=2, padx=0, pady=0)
            else:
                showerror(title="Unknown error occurred", message=f"An unknown error occurred. Heres the log:\n{viderror}")
            schedule_create(window, 4000, DefaultStates, True, **{"option": "ErrorReset"})
    YTThread = Thread(name="YTDownloadThread", daemon=True, target=YTDownloadThread)
    YTThread.start()

def speak(audio):
    """Speaks any string that you give it. It runs on its own thread so it doesn't block the main thread by default.\n
    speak('hello world')
    """
    def engineSpeak(audio):
        engine = ttsinit('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[settings["OpenAISettings"]["VoiceType"]].id)
        engine.say(audio)
        engine.runAndWait()
        del engine
    SpeechThread = Thread(name="SpeechThread", daemon=True, target=lambda: engineSpeak(audio))
    SpeechThread.start()
def ChatGPT():
    """Sends requests to ChatGPT and puts Response in text box"""
    UserText = assistant_responce_box_1.get("0.0", "end").strip("\n")
    if UserText != "" and UserText != None:
        def generate_response(prompt):
            try:
                openai.api_key = settings["OpenAISettings"]["OpenAI_API_Key"]
                response = openai.Completion.create(
                    engine=settings["OpenAISettings"]["OpenAI_model_engine"],
                    prompt=prompt,
                    max_tokens=settings["OpenAISettings"]["OpenAI_Max_Tokens"],
                    temperature=settings["OpenAISettings"]["OpenAI_Temperature"]
                )
                message = response.choices[0].text.strip()
                assistant_responce_box_2.delete("0.0", "end")
                assistant_responce_box_2.insert("end", message)
                if settingsSpeakResponceVar.get():
                    speak(message)
            except Exception as e:
                if (settings["OpenAISettings"]["OpenAI_API_Key"] == "") or (settings["OpenAISettings"]["OpenAI_API_Key"] == None):
                    showerror(title="OpenAI API Key Error", message=f"In settings.xml make sure 'OpenAI_API_Key' has a vaild OpenAI API key. Heres the full error:\n{e}")
                else:
                    showerror(title="OpenAI Error", message=e)
                assistant_responce_box_2.delete("0.0", "end")
        assistant_responce_box_2.delete("0.0", "end")
        assistant_responce_box_2.insert("end", "Thinking...")
        prompt = f"User: {UserText}"
        AIThread = Thread(name="AIThread", daemon=True, target=lambda: generate_response(model_prompt + "\n" + prompt))
        AIThread.start()

def GetPowerPlans():
    """Gets all power plans that are listed at:\n
    control panel > hardware and sound > power options"""

    # Run a command to list the power plans without showing a window. I do nothing with the error output because this command does not return an error
    output, error = Popen(["powercfg", "/list"], stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW).communicate()
    output_text = output.decode("utf-8")

    # Extract power plan information from the output
    power_plans = {}
    for line in output_text.splitlines():
        if "GUID" in line:
            guid = line.split("(")[1].split(")")[0]
            name = line.split(":")[1].split("(")[0].strip()
            power_plans[guid] = name

    # Find the active power plan
    active_plan = None
    for line in output_text.splitlines():
        if "*" in line and "GUID" in line:
            active_plan = line.split("(")[1].split(")")[0]
            break

    # Store the active power plan in the dictionary
    power_plans["active"] = active_plan

    return power_plans
def ChangePowerPlan(PlanName: str):
    """Changes the selected power plan"""
    if PlanName not in UserPowerPlans:
        showerror(title="Power plan error", message=f"The power plan that you selected\n> {PlanName}\ndoesn't seem to exist.")
        return
    PowerPlanGUID = UserPowerPlans[PlanName]
    Popen(["powercfg", "/setactive", PowerPlanGUID], stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)

def GetDeviceInfo(device_name: str = None, connectivity_type: str = "Bluetooth", device_battery_data: str = "{104EA319-6EE2-4701-BD47-8DDBF425BBE5} 2", device_type_data: str = "DEVPKEY_DeviceContainer_Category"):
    """Gets Bluetooth device information based on the provided parameters"""
    if device_name is None:
        raise ValueError("device_name must be provided")

    try:
        powershell_script = f"""
            $devices = Get-PnpDevice -Class '{connectivity_type}' | Where-Object {{$_.FriendlyName -eq '{device_name}'}}
            $deviceProperties = $devices | Get-PnpDeviceProperty | Where-Object {{$_.KeyName -eq '{device_battery_data}' -or $_.KeyName -eq '{device_type_data}'}}
            $batteryData = $deviceProperties | Where-Object {{$_.KeyName -eq '{device_battery_data}'}}
            $typeData = $deviceProperties | Where-Object {{$_.KeyName -eq '{device_type_data}'}}
            $batteryData.Data, $typeData.Data
        """
        result = Popen(["powershell.exe", "-WindowStyle", "Hidden", "-Command", powershell_script], stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
        output, error = result.communicate()
        output = output.decode("utf-8")
        script_output = output.strip().splitlines()
        if len(script_output) == 2:
            battery_percentage, device_type = script_output
            return int(battery_percentage), str(device_type)
        else:
            return None
    except:
        return None
def AllDeviceDetails():
    """Gets all device details and puts the bluetooth devices on the GUI in different frames and uses different icons for each device type (mouse, keyboard, headphones)"""
    def UpdateDevices():
        devices_refresh_btn.grid_forget()
        refreshinglabel = CTkLabel(devices_frame, text="Refreshing...", font=("Arial", 25))
        refreshinglabel.place(relx=0.5, rely=0.4, anchor="center")

        for frame in DeviceFrames:
            frame.destroy()
        DeviceFrames.clear()
        devices.clear()

        for device in settings["Devices"]:
            DeviceDetails = GetDeviceInfo(device)
            devices[device] = DeviceDetails

        for index, (device_name, device_data) in enumerate(devices.items()):
            row = (index // devices_per_row) + 1  # Calculate the row number based on the index and skip the first row
            column = index % devices_per_row  # Calculate the column number based on the index

            deviceFrame = CTkFrame(devices_frame, bg_color="#242424")
            deviceFrame.grid(row=row, column=column, pady=10, padx=10, sticky="nesw")
            DeviceFrames.append(deviceFrame)  # Add the frame to the list

            if len(device_name) > 17:
                    device_name = device_name[:17] + "..."

            if device_data is not None:
                percentage, device_type = device_data

                # Set the header image based on the device type
                if device_type == 'Input.Mouse':
                    header_image = CTkImage(PILopen("assets/ExtraIcons/mouse.png"), size=(50, 50))
                elif device_type == 'Input.Keyboard': # Experimental value
                    header_image = CTkImage(PILopen("assets/ExtraIcons/keyboard.png"), size=(50, 50))
                elif (device_type == 'Audio.Headphone') or (device_type == 'Audio.Headset') or (device_type == 'Audio.Speaker') or (device_type == 'Communication.Headset.Bluetooth'):
                    header_image = CTkImage(PILopen("assets/ExtraIcons/headphones.png"), size=(50, 50))
                else:
                    header_image = CTkImage(PILopen("assets/ExtraIcons/unknown_device.png"), size=(50, 50))

                header_label = CTkLabel(deviceFrame, image=header_image, text="")
                header_label.grid(row=0, column=0, rowspan=2, padx=10)

                # Display the device name and percentage
                name_label = CTkLabel(deviceFrame, text=device_name, font=("Arial", 20, "bold"))
                name_label.grid(row=0, column=1, columnspan=2, sticky="w", padx=(0, 20), pady=(10, 0))

                percentage_label = CTkLabel(deviceFrame, text=f"Percentage: {str(percentage)}%", font=("Arial", 17))
                percentage_label.grid(row=1, column=1, columnspan=2, sticky="w", padx=(0, 20), pady=(0, 10))
            else:
                header_image = CTkImage(PILopen("assets/ExtraIcons/unknown_device.png"), size=(50, 50))
                header_label = CTkLabel(deviceFrame, image=header_image, text="")
                header_label.grid(row=0, column=0, rowspan=2, padx=10)

                name_label = CTkLabel(deviceFrame, text=device_name, font=("Arial", 20, "bold"))
                name_label.grid(row=0, column=1, sticky="w", padx=(0, 20), pady=(10, 0))

                percentage_label = CTkLabel(deviceFrame, text="No data", font=("Arial", 17))
                percentage_label.grid(row=1, column=1, sticky="w", padx=(0, 20), pady=(0, 10))
            try: 
                refreshinglabel.destroy()
            except: 
                pass
        devices_refresh_btn.configure(text="Refresh")
        devices_refresh_btn.grid(row=row + 1, column=0, columnspan=2, padx=10, pady=20, sticky="ew")
    if settings["Devices"] is None or len(settings["Devices"]) == 0 or settings["Devices"] == "":
        def defaultstates():
            refreshinglabel.destroy()
            devices_refresh_btn.configure(text="Load devices")
            devices_refresh_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="ew")
        devices_refresh_btn.grid_forget()
        refreshinglabel = CTkLabel(devices_frame, text="No devices found", font=("Arial", 25))
        refreshinglabel.place(relx=0.5, rely=0.4, anchor="center")
        schedule_create(window, 4000, defaultstates, True)
    else:
        Thread(name="DeviceUpdateThread", daemon=True, target=lambda: UpdateDevices()).start()

def select_frame_by_name(name: str):
    """Changes selected frame"""
    # set button color for selected button
    home_button.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")
    games_button.configure(fg_color=("gray75", "gray25") if name == "Games" else "transparent")
    socialmedia_button.configure(fg_color=("gray75", "gray25") if name == "Social Media" else "transparent")
    ytdownloader_button.configure(fg_color=("gray75", "gray25") if name == "YT Downloader" else "transparent")
    assistant_button.configure(fg_color=("gray75", "gray25") if name == "Assistant" else "transparent")
    music_button.configure(fg_color=("gray75", "gray25") if name == "Music" else "transparent")
    devices_button.configure(fg_color=("gray75", "gray25") if name == "Devices" else "transparent")
    system_button.configure(fg_color=("gray75", "gray25") if name == "System" else "transparent")
    settings_button.configure(fg_color=("gray75", "gray25") if name == "Settings" else "transparent")

    # show selected frame
    if name == "Home":
        home_frame.pack(fill="both", expand=True)
    else:
        home_frame.pack_forget()
    if name == "Games":
        games_frame.pack(anchor="center", fill="both", expand=True)
    else:
        games_frame.pack_forget()
    if name == "Social Media":
        socialmedia_frame.pack(anchor="center", fill="both", expand=True)
    else:
        socialmedia_frame.pack_forget()
    if name == "YT Downloader":
        ytdownloader_frame.pack(fill="both", expand=True, anchor="center")
        ytdownloader_entry.bind("<Return>", lambda event: YTVideoDownloader(YTVideoContentType))
    else:
        ytdownloader_frame.pack_forget()
        ytdownloader_entry.unbind("<Return>")
    if name == "Assistant":
        assistant_frame.pack(fill="both", expand=True)
        assistant_responce_box_1.bind("<Shift-Return>", lambda event: ChatGPT())
    else:
        assistant_frame.pack_forget()
        assistant_responce_box_1.unbind("<Shift-Return>")
    if name == "Music":
        music_frame.pack(fill="both", expand=True)
    else:
        music_frame.pack_forget()
    if name == "Devices":
        devices_frame.pack(fill="both", expand=True)
        window.bind('<Control-r>', lambda event: AllDeviceDetails())
    else:
        devices_frame.pack_forget()
        window.unbind('<Control-r>')
    if name == "System":
        system_frame.pack(anchor="center", pady=(0, 20), fill="x", expand=True)
    else:
        system_frame.pack_forget()
    if name == "Settings":
        settings_frame.pack(anchor="center", fill="both", expand=True)
    else:
        settings_frame.pack_forget()
def SaveSettingsToJson(ValueToChange: str, Value: str):
    """Saves data to settings.json file"""
    for Property in ['URLs', 'GameShortcutURLs', 'OpenAISettings', 'MusicSettings', 'AppSettings']:
        if Property in settings and ValueToChange in settings[Property]:
            settings[Property][ValueToChange] = Value
            break
    else:
        showerror(title="settings error", message="There was an error when writing to the settings file")
        return

    with open(SETTINGSFILE, 'w') as SettingsToWrite:
        JSdump(settings, SettingsToWrite, indent=2)
def responsive_grid(frame: CTkFrame, rows: int, columns: int):
    """Makes a grid responsive for a frame"""
    for row in range(rows+1):
        frame.grid_rowconfigure(row, weight=1)
    for column in range(columns+1):
        frame.grid_columnconfigure(column, weight=1)
def check_window_properties():
    """Checks if the window properties are set"""
    if (
        "AppSettings" in settings and
        all(key in settings["AppSettings"] for key in ["Window_Width", "Window_Height", "Window_X", "Window_Y", "Window_State"]) and
        all(settings["AppSettings"][key] != "" for key in ["Window_Width", "Window_Height", "Window_X", "Window_Y", "Window_State"])
    ):
        return True
    return False
def update_widget(widget, update=False, update_idletasks=False):
    """Updates a widget"""
    if update:
        widget.update()
    if update_idletasks:
        widget.update_idletasks()
def hextorgb(new_color_hex: str):
    new_color_hex = new_color_hex.lower().lstrip('#')
    new_color_rgb = tuple(int(new_color_hex[i:i+2], 16) for i in (0, 2, 4))
    return new_color_rgb
def change_image_clr(image, hex_color: str):
    target_rgb = hextorgb(hex_color)
    image = image.convert('RGBA')
    data = nparray(image)

    # red, green, blue, alpha = data[..., 0], data[..., 1], data[..., 2], data[..., 3]
    alpha = data[..., 3]

    # Find areas with non-transparent pixels
    non_transparent_areas = alpha > 0

    # Replace the RGB values of non-transparent areas with the target RGB color
    data[..., 0][non_transparent_areas] = target_rgb[0]
    data[..., 1][non_transparent_areas] = target_rgb[1]
    data[..., 2][non_transparent_areas] = target_rgb[2]

    image_with_color = PILfromarray(data)
    return image_with_color
def shorten_path(text, max_length, replacement: str = "..."):
    if len(text) > max_length:
        return text[:max_length - 3] + replacement  # Replace the last three characters with "..."
    return text
def LaunchUpdater():
    check_for_updates("in-app")
    cwd = getcwd()
    if getattr(sys, 'frozen', False):
        downurl = f"https://github.com/HyperNylium/Management_Panel/releases/download/v{LiveAppVersion}/Management_Panel-{LiveAppVersion}-windows.zip"
        local_path_zip = f"Management_Panel-{LiveAppVersion}-windows.zip"
        local_path = f"{cwd}\\Management_Panel"
    else:
        downurl = f"https://github.com/HyperNylium/Management_Panel/archive/refs/tags/v{LiveAppVersion}.zip"
        local_path_zip = f"Management_Panel-{LiveAppVersion}.zip"
        local_path = f"{cwd}\\Management_Panel-{LiveAppVersion}"

    if LiveAppVersion < CurrentAppVersion:
        showerror(title="Invalid version!", message=f"You have an invalid copy/version of this software.\n\nLive/Public version: {LiveAppVersion}\nYour version: {CurrentAppVersion}\n\nPlease go to:\nhttps://github.com/HyperNylium/Management_Panel\nto get the latest/authentic version of this app.")
        return

    elif LiveAppVersion != CurrentAppVersion or LiveAppVersion > CurrentAppVersion:
        usr_choice = askyesno(title='New Version!', message=f'New Version is v{LiveAppVersion}\nYour Version is v{CurrentAppVersion}\n\nNew Version of the app is now available to download/install\nClick "Yes" to update and "No" to cancel')
        if usr_choice is True:
            def updatewindow_on_closing():
                update_now_button.configure(state="normal")
                updatewindow.destroy()
            def launchupdater():
                def launch():
                    system(f"update.exe {LiveAppVersion} {SETTINGSFILE}")
                    sys.exit()
                Thread(name="LaunchUpdaterThread", daemon=True, target=launch).start()
                on_closing()
            def download_update():
                try:
                    updatewindow_label.configure(text=f"Downloading update v{LiveAppVersion}...")
                    downloadedoutof = CTkLabel(updatewindow, text=f"0 / 0 (0.0%)", font=("Arial", 20))
                    downloadedoutof.pack(fill="x", expand=True, padx=20, pady=0)
                    downloadprogress = CTkProgressBar(updatewindow, mode="determinate", height=15)
                    downloadprogress.set(0)
                    downloadprogress.pack(fill="x", expand=True, padx=20, pady=0)
                    response = get(downurl, stream=False, timeout=60, headers=headers, allow_redirects=True)
                    total_size_in_bytes = int(response.headers.get('content-length', 0))
                    bytes_downloaded = 0
                    block_size = 1024
                    with open(local_path_zip, 'wb') as updatefile:
                        for data in response.iter_content(block_size):
                            updatefile.write(data)
                            bytes_downloaded += len(data)
                            if total_size_in_bytes > 0:
                                progress = bytes_downloaded / total_size_in_bytes
                                progress_percent = (progress * 100)
                                downloadedoutof.configure(text=f"{bytes_downloaded} out of {total_size_in_bytes} bytes downloaded\n({progress_percent:.2f}%)")
                                downloadprogress.set(progress)
                                downloadedoutof.update()
                                downloadprogress.update()
                    downloadedoutof.destroy()
                    downloadprogress.destroy()

                    updatewindow_label.configure(text=f"Extracting update files...")
                    with ZipFile(local_path_zip, 'r') as zipObj:
                        zipObj.extractall()

                    remove(local_path_zip)

                    for root, dirs, files in walk(local_path):
                        relative_path = relpath(root, local_path)
                        dest_root = join(cwd, relative_path)

                        makedirs(dest_root, exist_ok=True)

                        for file in files:
                            if file.lower() == "update.exe":
                                src_file = join(root, file)
                                dest_file = join(dest_root, file)
                                copy2(src_file, dest_file)
                                break

                    updatewindow_label.configure(text=f"Launching update.exe to finish installing update...")
                    launchupdater()
                    return
                except Exception as e:
                    showerror(title="Update error", message=f"An error occurred while updating. Heres the full error:\n{e}")
                    update_now_button.configure(state="normal")
                    updatewindow.destroy()
                return

            updatewindow = CTkToplevel()
            updatewindow.title("Updater")
            updatewindow.attributes('-topmost', True)
            updatewindow.geometry(CenterWindowToMain(window, 500, 250))
            updatewindow.resizable(False, False)
            updatewindow.protocol("WM_DELETE_WINDOW", updatewindow_on_closing)
            update_now_button.configure(state="disabled")
            updatewindow_label = CTkLabel(updatewindow, text="Initializing...", font=("Arial", 20))
            updatewindow_label.pack(fill="x", expand=True, padx=20, pady=0)
            Thread(name="UpdateDownloadThread", daemon=True, target=download_update).start()
    else:
        showinfo(title="Update", message="You are on the latest version")
        return

    return

window = CTk()
window.title("Management Panel")
window.protocol("WM_DELETE_WINDOW", on_closing)
screen_scale = window._get_window_scaling()
StartUp()

if check_window_properties():
    WINDOW_STATE = str(settings["AppSettings"]["Window_State"])
    WIDTH = int(settings["AppSettings"]["Window_Width"] / screen_scale)
    HEIGHT = int(settings["AppSettings"]["Window_Height"] / screen_scale)
    X = int(settings["AppSettings"]["Window_X"])
    Y = int(settings["AppSettings"]["Window_Y"])

    window.geometry(f"{WIDTH}x{HEIGHT}+{X}+{Y}")

    if WINDOW_STATE == "maximized":
        # Thank you Akascape for helping me out (https://github.com/TomSchimansky/CustomTkinter/discussions/1819)
        schedule_create(window, 50,  lambda: window.state('zoomed'), True)

    del WIDTH, HEIGHT, X, Y, WINDOW_STATE
else:
    window.geometry(CenterWindowToDisplay(window, 900, 420, screen_scale))

del screen_scale

# Bind keys Ctrl + Shift + Del to reset the windows positional values in settings.json
window.bind('<Control-Shift-Delete>', lambda event: ResetWindowPos())
window.bind('<Configure>', on_drag_end)

# Set alpha value of window from settings.json
window.attributes("-alpha", settings["AppSettings"]["Alpha"])

# Importing all icons and assigning them to there own variables to use later
try:
    homeimage = CTkImage(PILopen("assets/MenuIcons/about.png"), size=(25, 25))
    devicesimage = CTkImage(PILopen("assets/MenuIcons/devices.png"), size=(25, 25))
    gamesimage = CTkImage(PILopen("assets/MenuIcons/games.png"), size=(25, 25))
    ytdownloaderimage = CTkImage(PILopen("assets/MenuIcons/ytdownloader.png"), size=(25, 25))
    socialmediaimage = CTkImage(PILopen("assets/MenuIcons/socialmedia.png"), size=(25, 25))
    assistantimage = CTkImage(PILopen("assets/MenuIcons/assistant.png"), size=(25, 25))
    musicimage = CTkImage(PILopen("assets/MenuIcons/music.png"), size=(25, 25))
    systemimage = CTkImage(PILopen("assets/MenuIcons/system.png"), size=(25, 25))
    settingsimage = CTkImage(PILopen("assets/MenuIcons/settings.png"), size=(25, 25))
    closeimage = CTkImage(PILopen("assets/MenuIcons/close.png"), size=(20, 20))
    openimage = CTkImage(PILopen("assets/MenuIcons/open.png"), size=(25, 25))
    previousimage = CTkImage(change_image_clr(PILopen('assets/MusicPlayer/previous.png'), "#ffffff"), size=(25, 25))
    pauseimage = CTkImage(change_image_clr(PILopen("assets/MusicPlayer/pause.png"), "#ffffff"), size=(25, 25))
    playimage = CTkImage(change_image_clr(PILopen('assets/MusicPlayer/play.png'), "#ffffff"), size=(25, 25))
    nextimage = CTkImage(change_image_clr(PILopen('assets/MusicPlayer/next.png'), "#ffffff"), size=(25, 25))
    if settings["MusicSettings"]["LoopState"] == "all":
        loopimage = CTkImage(change_image_clr(PILopen('assets/MusicPlayer/loop.png'), "#00ff00"), size=(25, 25))
    elif settings["MusicSettings"]["LoopState"] == "one":
        loopimage = CTkImage(change_image_clr(PILopen('assets/MusicPlayer/loop-1.png'), "#00ff00"), size=(25, 25))
    elif settings["MusicSettings"]["LoopState"] == "off":
        loopimage = CTkImage(change_image_clr(PILopen('assets/MusicPlayer/loop.png'), "#ff0000"), size=(25, 25))
    else:
        loopimage = CTkImage(change_image_clr(PILopen('assets/MusicPlayer/loop.png'), "#00ff00"), size=(25, 25))
        SaveSettingsToJson("LoopState", "all")
except Exception as e:
    showerror(title="Icon import error", message=f"Couldn't import an icon.\nDetails: {e}")
    on_closing()

# create navigation frame
navigation_frame = CTkFrame(window, corner_radius=0)
navigation_buttons_frame = CTkFrame(navigation_frame, corner_radius=0, fg_color="transparent")
navigation_frame.pack(side="left", fill="y")

# X button and time&date label
close_open_nav_button = CTkButton(window, width=25, height=25, text="", fg_color="transparent", image=closeimage, anchor="w", hover_color=("gray70", "gray30"), command=lambda: NavbarAction("close"))
close_open_nav_button.pack(side="top", anchor="nw", padx=0, pady=5)
navigation_frame_label = CTkLabel(navigation_frame, text="Loading...", font=("sans-serif", 18, "bold"))
navigation_frame_label.pack(side="top", padx=20, pady=20)

# navigation_buttons_frame pack. We need to pack it here so its under the navigation_frame_label (under the time and date)
navigation_buttons_frame.pack(fill="x", expand=True, anchor="center")

# menu btns
home_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=10, height=40, text="Home", fg_color="transparent", image=homeimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Home"))
home_button.grid(sticky="ew", pady=1)
games_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="Games", fg_color="transparent", image=gamesimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Games"))
games_button.grid(sticky="ew", pady=1)
socialmedia_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="Social Media", fg_color="transparent", image=socialmediaimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Social Media"))
socialmedia_button.grid(sticky="ew", pady=1)
ytdownloader_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="YT Downloader", fg_color="transparent", image=ytdownloaderimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("YT Downloader"))
ytdownloader_button.grid(sticky="ew", pady=1)
assistant_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="Assistant", fg_color="transparent", image=assistantimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Assistant"))
assistant_button.grid(sticky="ew", pady=1)
music_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="Music", fg_color="transparent", image=musicimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Music"))
music_button.grid(sticky="ew", pady=1)
devices_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="Devices", fg_color="transparent", image=devicesimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Devices"))
devices_button.grid(sticky="ew", pady=1)
system_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="System", fg_color="transparent", image=systemimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("System"))
system_button.grid(sticky="ew", pady=1)
settings_button = CTkButton(navigation_buttons_frame, corner_radius=10, width=0, height=40, text="Settings", fg_color="transparent", image=settingsimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Settings"))
settings_button.grid(sticky="ew", pady=1)

del homeimage, devicesimage, gamesimage, ytdownloaderimage, socialmediaimage, assistantimage, musicimage, systemimage, settingsimage


# main frames
home_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
games_frame = CTkScrollableFrame(window, corner_radius=0, fg_color="transparent", border_width=3, border_color="#242424")
socialmedia_frame = CTkScrollableFrame(window, corner_radius=0, fg_color="transparent", border_width=3, border_color="#242424")
ytdownloader_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
assistant_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
music_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
devices_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
system_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
settings_frame = CTkScrollableFrame(window, corner_radius=0, fg_color="transparent", border_width=3, border_color="#242424")


# Create elements/widgets for frames
home_frame_label_1 = CTkLabel(home_frame, text=f"Version: {CurrentAppVersion} {ShowUserInfo}", font=("sans-serif", 28))
home_frame_label_1.pack(anchor="center", pady=(100, 0))
home_frame_label_2 = CTkLabel(home_frame, text=f"Creator/developer: {Developer}", font=("sans-serif", 28))
home_frame_label_2.pack(anchor="center", pady=10)
home_frame_label_3 = CTkLabel(home_frame, text=f"Last updated: {LastEditDate}", font=("sans-serif", 28))
home_frame_label_3.pack(anchor="center")
chkforupdatesframe = CTkFrame(home_frame, corner_radius=0, fg_color="transparent")
chkforupdatesframe.pack(anchor="s", fill="x", expand=True)
check_for_updates_button = CTkButton(chkforupdatesframe, text="Check for updates", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: check_for_updates(option="in-app"))
update_now_button = CTkButton(chkforupdatesframe, text="Update now", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=LaunchUpdater)
check_for_updates_button.grid(row=1, column=0, columnspan=2, padx=5, pady=10, sticky="ew")
update_now_button.grid(row=1, column=2, columnspan=2, padx=5, pady=10, sticky="ew")


YTVideoContentType = "Video (.mp4)"
ytdownloader_entry = CTkEntry(ytdownloader_frame, placeholder_text="Enter your video URL here", width=600, height=40, border_width=0, corner_radius=10, font=("sans-serif", 22), justify="center")
ytdownloader_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=0)
ytdownloader_error_label = CTkLabel(ytdownloader_frame, text="", font=("sans-serif", 18))
ytdownloader_OptionMenu = CTkOptionMenu(ytdownloader_frame, values=["Video (.mp4)", "Audio (.mp3)"], command=lambda vidtype: YTVideoDownloaderContentType(vidtype), fg_color="#343638", button_color="#4d4d4d", button_hover_color="#444", font=("sans-serif", 17), dropdown_font=("sans-serif", 15), width=200, height=30, anchor="center")
ytdownloader_OptionMenu.grid(row=2, column=0, columnspan=2, padx=10, pady=0)
ytdownloader_OptionMenu.set("Video (.mp4)")
ytdownloader_frame_button_1 = CTkButton(ytdownloader_frame, text="Download", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: YTVideoDownloader(YTVideoContentType))
ytdownloader_frame_button_1.grid(row=3, rowspan=2, column=0, columnspan=2, padx=10, pady=20, sticky="ews")
ytdownloader_progressbar= CTkProgressBar(ytdownloader_frame, mode="determinate", height=15)
ytdownloader_progressbar.set(0)
ytdownloader_progressbarpercentage= CTkLabel(ytdownloader_frame, text="0%", font=("sans-serif Bold", 18))


assistant_responce_box_frame = CTkFrame(assistant_frame, corner_radius=0, fg_color="transparent")
assistant_responce_box_frame.pack(fill="x", expand=True, anchor="center")
assistant_responce_box_1 = CTkTextbox(assistant_responce_box_frame, width=680, height=150, border_width=0, corner_radius=10, font=("sans-serif", 22), activate_scrollbars=True, border_color="#242424")
assistant_responce_box_1.grid(row=0, column=0, padx=10, pady=10)
assistant_responce_box_2 = CTkTextbox(assistant_responce_box_frame, width=680, height=150, border_width=0, corner_radius=10, font=("sans-serif", 22), activate_scrollbars=True, border_color="#242424")
assistant_responce_box_2.grid(row=1, column=0, padx=10, pady=10)
assistant_frame_button_1 = CTkButton(assistant_frame, text="Submit question", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: ChatGPT())
assistant_frame_button_1.pack(fill="x", expand=True, anchor="center", padx=10, pady=5)


music_frame_container = CTkFrame(music_frame, corner_radius=0, fg_color="transparent")
all_music_frame = CTkScrollableFrame(music_frame, height=150, corner_radius=0, fg_color="transparent", border_width=3, border_color="#333")
music_info_frame = CTkFrame(music_frame, corner_radius=0, fg_color="transparent")
music_controls_frame = CTkFrame(music_frame_container, corner_radius=0, fg_color="transparent")
music_volume_frame = CTkFrame(music_frame_container, corner_radius=0, fg_color="transparent")
music_progress_frame = CTkFrame(music_frame_container, corner_radius=0, fg_color="transparent")
all_music_frame.pack(fill="x", expand=True, anchor="s", pady=0)
music_info_frame.pack(fill="x", expand=True, anchor="s", pady=0)
music_frame_container.pack(fill="x", expand=True, anchor="s", pady=0)
music_controls_frame.pack(fill="x", expand=True, anchor="s", pady=0)
music_volume_frame.pack(fill="x", expand=True, anchor="s", pady=0)
music_progress_frame.pack(fill="x", expand=True, anchor="s", pady=0)
currently_playing_label = CTkLabel(music_info_frame, text="Status: Scanning files...", font=("sans-serif", 18))
music_dir_label = CTkLabel(music_info_frame, text=f"Music Directory: {shorten_path(settings['MusicSettings']['MusicDir'], 45)}" if settings['MusicSettings']['MusicDir'] != "" else "Music Directory: None", font=("sans-serif", 18))
update_music_list = CTkButton(music_info_frame, width=80, text="Update", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 18), corner_radius=10, command=lambda: music_manager.musicmanager("update"))
change_music_dir = CTkButton(music_info_frame, width=80, text="Change", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 18), corner_radius=10, command=lambda: music_manager.musicmanager("changedir"))
currently_playing_label.grid(row=1, column=1, padx=10, pady=5, sticky="w")
music_dir_label.grid(row=2, column=1, padx=10, pady=5, sticky="w")
update_music_list.grid(row=2, column=2, padx=5, pady=5, sticky="e")
change_music_dir.grid(row=2, column=3, padx=5, pady=5, sticky="w")
music_info_frame.grid_columnconfigure([0, 3], weight=1)
pre_song_btn = CTkButton(music_controls_frame, width=40, height=40, text="", fg_color="transparent", image=previousimage, anchor="w", hover_color=("gray70", "gray30"), command=lambda: music_manager.musicmanager("previous"))
play_pause_song_btn = CTkButton(music_controls_frame, width=40, height=40, text="", fg_color="transparent", image=playimage, anchor="w", hover_color=("gray70", "gray30"), command=lambda: music_manager.musicmanager("play"))
next_song_btn = CTkButton(music_controls_frame, width=40, height=40, text="", fg_color="transparent", image=nextimage, anchor="w", hover_color=("gray70", "gray30"), command=lambda: music_manager.musicmanager("next"))
loop_playlist_btn = CTkButton(music_controls_frame, width=40, height=40, text="", fg_color="transparent", image=loopimage, anchor="w", hover_color=("gray70", "gray30"), command=lambda: music_manager.musicmanager("loop"))
pre_song_btn.grid(row=1, column=1, padx=10, pady=0, sticky="e")
play_pause_song_btn.grid(row=1, column=2, padx=10, pady=0, sticky="e")
next_song_btn.grid(row=1, column=3, padx=10, pady=0, sticky="e")
loop_playlist_btn.grid(row=1, column=4, padx=10, pady=0, sticky="w")
volume_slider = CTkSlider(music_volume_frame, width=250, from_=0, to=100, command=lambda volume: music_manager.musicmanager("volume"), variable=musicVolumeVar, button_color="#fff", button_hover_color="#ccc")
volume_label = CTkLabel(music_volume_frame, text=f"{musicVolumeVar.get()}%", font=("sans-serif", 18, "bold"), fg_color="transparent")
volume_label.grid(row=1, column=1, padx=0, pady=0, sticky="w")
volume_slider.grid(row=1, column=1, padx=40, pady=0, sticky="e")
music_volume_frame.grid_columnconfigure([0, 2], weight=1)
time_left_label = CTkLabel(music_progress_frame, text="0:00", font=("sans-serif", 18, "bold"), fg_color="transparent")
song_progressbar = CTkProgressBar(music_progress_frame, mode="determinate", height=15)
song_progressbar.set(0.0)
total_time_label = CTkLabel(music_progress_frame, text="0:00", font=("sans-serif", 18, "bold"), fg_color="transparent")
time_left_label.grid(row=1, column=0, padx=10, pady=0, sticky="w")
song_progressbar.grid(row=1, column=1, padx=10, pady=0, sticky="ew")
total_time_label.grid(row=1, column=2, padx=10, pady=0, sticky="e")
music_progress_frame.grid_columnconfigure(1, weight=1)


devices_spacing_label_1 = CTkLabel(devices_frame, width=340, height=0, text="").grid(row=0, column=0, padx=0, pady=0)
devices_spacing_label_2 = CTkLabel(devices_frame, width=340, height=0, text="").grid(row=0, column=1, padx=0, pady=0)
devices_refresh_btn = CTkButton(devices_frame, text="Load devices", compound="bottom", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=AllDeviceDetails)
devices_refresh_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="ew")


system_frame_button_1 = CTkButton(system_frame, text="VPN settings", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("vpn"))
system_frame_button_1.grid(row=0, column=1, padx=5, pady=10)
system_frame_button_2 = CTkButton(system_frame, text="Netdrive", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("netdrive"))
system_frame_button_2.grid(row=0, column=2, padx=5, pady=10)
system_frame_button_3 = CTkButton(system_frame, text="Installed apps", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("apps"))
system_frame_button_3.grid(row=0, column=3, padx=5, pady=10)
system_frame_button_4 = CTkButton(system_frame, text="Sound settings", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("sound"))
system_frame_button_4.grid(row=1, column=1, padx=5, pady=10)
system_frame_button_5 = CTkButton(system_frame, text="Display settings", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("display"))
system_frame_button_5.grid(row=1, column=2, padx=5, pady=10)
system_frame_button_6 = CTkButton(system_frame, text="Power settings", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("power"))
system_frame_button_6.grid(row=1, column=3, padx=5, pady=10)
system_frame_button_7 = CTkButton(system_frame, text="Storage settings", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("storage"))
system_frame_button_7.grid(row=2, column=1, padx=5, pady=10)
system_frame_button_8 = CTkButton(system_frame, text="Network setings", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("network"))
system_frame_button_8.grid(row=2, column=2, padx=5, pady=10)
system_frame_button_9 = CTkButton(system_frame, text="Windows update", compound="top", width=200, fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("windowsupdate"))
system_frame_button_9.grid(row=2, column=3, padx=5, pady=10)
system_frame_power_optionmenu = CTkOptionMenu(system_frame, values=list(UserPowerPlans.keys())[:-1], command=lambda PlanName: ChangePowerPlan(PlanName), fg_color="#343638", button_color="#4d4d4d", button_hover_color="#444", font=("sans-serif", 17), dropdown_font=("sans-serif", 15), width=200, height=30, anchor="center")
system_frame_power_optionmenu.grid(row=4, column=2, padx=5, pady=10)
system_frame_power_optionmenu.set(UserPowerPlans['active'])


settingsgrid = CTkFrame(settings_frame, corner_radius=0, fg_color="transparent")
settingsgrid.pack(fill="x", expand=True, anchor="center")
settingsAlwayOnTopswitch = CTkSwitch(settingsgrid, text="", variable=settingsAlwayOnTopVar, onvalue=True, offvalue=False, font=("sans-serif", 22), command=AlwaysOnTopTrueFalse)
settingsAlwayOnToplabel = CTkLabel(settingsgrid, text="Always on top", font=("sans-serif", 22))
settingsAlwayOnTopswitch.grid(row=1, column=1, pady=5, sticky="e")
settingsAlwayOnToplabel.grid(row=1, column=2, pady=5, sticky="w")
settingslaunchwithwindowsswitch = CTkSwitch(settingsgrid, text="", variable=settingslaunchwithwindowsvar, onvalue=True, offvalue=False, font=("sans-serif", 22), command=LaunchOnStartupTrueFalse)
settingslaunchwithwindowslabel = CTkLabel(settingsgrid, text="Launch at login", font=("sans-serif", 22))
settingslaunchwithwindowsswitch.grid(row=2, column=1, pady=5, sticky="e")
settingslaunchwithwindowslabel.grid(row=2, column=2, pady=5, sticky="w")
settingsSpeakResponceswitch = CTkSwitch(settingsgrid, text="", variable=settingsSpeakResponceVar, onvalue=True, offvalue=False, font=("sans-serif", 22), command=lambda: SaveSettingsToJson("SpeakResponce", str(settingsSpeakResponceVar.get())))
settingsSpeakResponcelabel = CTkLabel(settingsgrid, text="Speak response from AI", font=("sans-serif", 22))
settingsSpeakResponceswitch.grid(row=3, column=1, pady=5, sticky="e")
settingsSpeakResponcelabel.grid(row=3, column=2, pady=5, sticky="w")
settingscheckupdatesswitch = CTkSwitch(settingsgrid, text="", variable=settingsCheckForUpdates, onvalue=True, offvalue=False, font=("sans-serif", 22), command=lambda: SaveSettingsToJson("CheckForUpdatesOnLaunch", str(settingsCheckForUpdates.get())))
settingscheckupdateslabel = CTkLabel(settingsgrid, text="Check for updates on launch", font=("sans-serif", 22))
settingscheckupdatesswitch.grid(row=4, column=1, pady=5, sticky="e")
settingscheckupdateslabel.grid(row=4, column=2, pady=5, sticky="w")
settingsresetwindowbtn = CTkButton(settings_frame, width=300, text="Reset window position", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 20), corner_radius=10, command=lambda: ResetWindowPos())
settingsresetwindowbtn.pack(anchor="center", padx=10, pady=10)
settingsopensettingsbtn = CTkButton(settings_frame, width=300, text="Open settings.json", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 20), corner_radius=10, command=lambda: startfile(SETTINGSFILE))
settingsopensettingsbtn.pack(anchor="center", padx=10, pady=10)
alpha_slider = CTkSlider(settings_frame, width=300, from_=0.5, to=1.0, command=set_alpha, variable=settingsAlphavar) # I set the _from param to 0.5 because anything lower than that is too transparent and you can't see the window let alone interact with it.
alpha_slider.pack(anchor="center", padx=10, pady=10)
settings_default_frame_optionmenu = CTkOptionMenu(settings_frame, values=all_frames, command=lambda frame: SaveSettingsToJson("DefaultFrame", frame), fg_color="#343638", button_color="#4d4d4d", button_hover_color="#444", font=("sans-serif", 20), dropdown_font=("sans-serif", 17), width=250, height=30, anchor="center")
settings_default_frame_optionmenu.set(settings["AppSettings"]["DefaultFrame"])
settings_default_frame_optionmenu.pack(anchor="center", padx=10, pady=10)
settingsAlphavar.set(settings["AppSettings"]["Alpha"])


# select default frame in settings.json (can be changed in GUI from "settings_default_frame_optionmenu")
select_frame_by_name(settings["AppSettings"]["DefaultFrame"])

# Make frames .grid responsive
responsive_grid(navigation_buttons_frame, 10, 0) # 10 rows, 0 columns responsive
responsive_grid(games_frame, 2, 2) # 2 rows, 2 columns responsive
responsive_grid(socialmedia_frame, 2, 2) # 2 rows, 2 columns responsive
responsive_grid(ytdownloader_frame, 4, 1) # 4 rows, 1 column responsive
responsive_grid(assistant_frame, 0, 0) # 0 rows, 0 columns responsive
responsive_grid(assistant_responce_box_frame, 1, 0) # 1 rows, 0 columns responsive
responsive_grid(devices_frame, 3, 1) # 3 rows, 1 column responsive
responsive_grid(system_frame, 2, 3) # 2 rows, 3 columns responsive
responsive_grid(settings_frame, 2, 2) # 2 rows, 2 columns responsive
chkforupdatesframe.grid_columnconfigure([0, 3], weight=1)
music_controls_frame.grid_columnconfigure([0, 4], weight=1)
settingsgrid.grid_columnconfigure([0, 3], weight=1)

# add all buttons and their text to a list for later use
for widget in navigation_buttons_frame.winfo_children():
    if isinstance(widget, CTkButton):
        all_buttons.append(widget)
        all_buttons_text.append(widget.cget('text'))

# initialize and start the MusicManager
music_manager.musicmanager("update")
music_manager.start_event_loops()

# initialize and start the TitleUpdater
title_bar = TitleUpdater(navigation_frame_label)
title_bar.start()

# set the navigation state to the last known state in settings.json
if settings["AppSettings"]["NavigationState"] == "close":
    NavbarAction("close")
else:
    NavbarAction("open")

AppsLaucherGUISetup("games_frame") # create the games_frame content
AppsLaucherGUISetup("socialmedia_frame") # create the socialmedia_frame content

# if my personel netdrive script does not exist on the system, disable the button to launch it
if not exists(f"{UserDesktopDir}/Stuff/GitHub/Environment_Scripts/netdrive.bat"):
    system_frame_button_2.configure(state="disabled")

window.mainloop()