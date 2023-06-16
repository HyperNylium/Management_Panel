
# pyinstaller --noconfirm --onedir --windowed --add-data "C:/Users/david/AppData/Local/Programs/Python/Python311/Lib/site-packages/customtkinter;customtkinter/"  "C:/Users/david/Desktop/Stuff/GitHub/Repos/Management_Panel/Management_Panel.pyw"

# TODO: make a check for updates function that checks for updates once clicked by a button instead of on launch
# TODO: make a dropdown menu in the settings tab for changing the default open tab on launch
# TODO: finish making the app responsive. 4/8 done so far
# TODO: when closing also save the width and height of the window for next launch in the settings.json

from sys import exit, executable as SYSexecutable, argv as SYSargv
from tkinter.messagebox import showerror, askyesno, showinfo
from os import system, startfile, execl, mkdir, rename
from subprocess import Popen, PIPE, CREATE_NO_WINDOW
from json import load as JSload, dump as JSdump
from threading import Thread, Timer as TD_Timer
from os.path import exists, join, splitext
from webbrowser import open as WBopen
from datetime import datetime, date
from tkinter import BooleanVar

try:
    from customtkinter import CTk, CTkFrame, CTkLabel, CTkButton, CTkImage, CTkEntry, CTkSwitch, CTkOptionMenu, CTkProgressBar, CTkTextbox, set_appearance_mode
except:
    showerror(title="Import error", message="There was an error while importing 'customtkinter'.\nTry running 'pip install customtkinter'\nin a elevated/admin terminal")
    exit()
try:
    from plyer import notification
except:
    showerror(title="Import error", message="There was an error while importing 'plyer'.\nTry running 'pip install plyer'\nin a elevated/admin terminal")
    exit()
try:
    from requests import get
    from requests.exceptions import Timeout
except:
    showerror(title="Import error", message="There was an error while importing 'requests'.\nTry running 'pip install requests'\nin a elevated/admin terminal")
    exit()
try:
    from winshell import desktop
except:
    showerror(title="Import error", message="There was an error while importing 'winshell'.\nTry running 'pip install winshell'\nin a elevated/admin terminal")
    exit()
try:
    from PIL.Image import open as PILopen
except:
    showerror(title="Import error", message="There was an error while importing 'Pillow-PIL'.\nTry running 'pip install Pillow'\nin a elevated/admin terminal")
    exit()
try:
    import openai
except:
    showerror(title="Import error", message="There was an error while importing 'OpenAI'.\nTry running 'pip install openai'\nin a elevated/admin terminal")
    exit()
try:
    from pytube import YouTube as PY_Youtube
except:
    showerror(title="Import error", message="There was an error while importing 'pytube'.\nTry running 'pip install pytube'\nin a elevated/admin terminal")
    exit()
try:
    from pyttsx3 import init as ttsinit
except:
    showerror(title="Import error", message="There was an error while importing 'pyttsx3'.\nTry running 'pip install pyttsx3'\nin a elevated/admin terminal")
    exit()
try:
    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler
except:
    showerror(title="Import error", message="There was an error while importing 'watchdog'.\nTry running 'pip install watchdog'\nin a elevated/admin terminal")
    exit()

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
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

# ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6) # Minimizes console window that launches with .py files

set_appearance_mode("dark")

CurrentAppVersion = "4.1.2"
UpdateLink = "https://github.com/HyperNylium/Management_Panel"
DataTXTFileUrl = "http://www.hypernylium.com/projects/ManagementPanel/assets/data.txt"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}

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
            elif key == "Developer_Lowercase":
                Developer_Lowercase = value
            elif key == "LastEditDate":
                LastEditDate = value

    if LiveAppVersion < CurrentAppVersion:
            output = askyesno(title='Invalid version!', message=f'You have an invalid copy/version of this software.\n\nLive/Public version: {LiveAppVersion}\nYour version: {CurrentAppVersion}\n\nPlease go to:\nhttps://github.com/HyperNylium/Management_Panel\nto get the latest/authentic version of this app.\n\nDo you want to contine anyways?')
            if (output):
                pass
            else:
                exit()
            Developer = "Unknown"
            Developer_Lowercase = "Unknown"
            LastEditDate = "Unknown"
            LiveAppVersion = CurrentAppVersion
            ShowUserInfo = "- Unauthentic"
            pass
    elif LiveAppVersion != CurrentAppVersion or LiveAppVersion > CurrentAppVersion:
            output = askyesno(title='New Version!', message=f'New Version is v{LiveAppVersion}\nYour Version is v{CurrentAppVersion}\n\nNew Version of the app is now available to download/install\nClick "Yes" to update and "No" to cancel')
            if (output):
                WBopen(UpdateLink)
                exit()
            else:
                ShowUserInfo = f"- Update available (v{LiveAppVersion})"
                LiveAppVersion = CurrentAppVersion
                pass
    else:
        ShowUserInfo = "- Latest version"
        pass
except Timeout:
    showerror(title='Request timed out', message=f"Main data file request timed out\nThis can happen because:\n> You are offline\n> The webserver is not hosting the file at the moment\n> Your internet connection is slow\n\nThe app will now start in offline mode.")
    LiveAppVersion = "N/A"
    Developer = "N/A"
    Developer_Lowercase = "N/A"
    LastEditDate = "N/A"
    ShowUserInfo = ""
except Exception as e:
    showerror(title='Launching in offline mode', message=f"There was an error while retrieving the main data file\nThis can happen because:\n> You are offline\n> The webserver is not hosting the file at the moment\n\nThe app will now start in offline mode.")
    LiveAppVersion = "N/A"
    Developer = "N/A"
    Developer_Lowercase = "N/A"
    LastEditDate = "N/A"
    ShowUserInfo = ""

model_prompt = "Hello, how can I help you today?"
UserDesktopDir = desktop()
SETTINGSFILE = "settings.json"
devices_per_row = 2  # Maximum number of devices per row
DeviceFrames = []  # List to store references to deviceFrame frames
devices = {} # dict to store device info (battey persetage, type)
after_events = {} # dict to store after events
all_buttons: list[CTkButton] = [] # list to store all buttons in the navigation bar
all_buttons_text: list[str] = [] # list to store all buttons text in the navigation bar

class SettingsFileEventHandler(FileSystemEventHandler):
    def __init__(self):
        self.modified_event_pending = False

    def on_modified(self, event):
        if event.src_path.endswith(SETTINGSFILE) and not self.modified_event_pending:
            self.modified_event_pending = True
            TD_Timer(1, self.reload_settings).start()

    def reload_settings(self):
        global settings
        if exists(SETTINGSFILE):
            try:
                with open(SETTINGSFILE, 'r') as settings_file:
                    settings = JSload(settings_file)
            except:
                pass
        self.modified_event_pending = False

def StartUp():
    """Reads settings.json and loads all the variables into the settings variable.\n
    If the file isn't found, it creates one within the same directory and loads it with default values.\n
    settings[Property][Key] => value\n
    settings['AppSettings']['AlwaysOnTop'] => True | False"""

    def load_settings():
        global observer, settings
        default_settings = {
            "URLs": {
                "WEBSITE": "http://hypernylium.com/",
                "GITHUBURL": "https://github.com/HyperNylium",
                "DISCORDURL": "https://discord.gg/4FHTjAgw95",
                "INSTAGRAMURL": "https://www.instagram.com/hypernylium/",
                "YOUTUBEURL": "https://www.youtube.com/channel/UCpJ4F4dMn_DIhtrCJwDUK2A",
                "TIKTOKURL": "https://www.tiktok.com/foryou?lang=en",
                "FACEBOOK": "https://www.facebook.com/HyperNylium/",
                "TWITTERURL": "https://twitter.com/HyperNylium"
            },
            "GameShortcutURLs": {
                "GAME_1": "",
                "GAME_2": "",
                "GAME_3": "",
                "GAME_4": "",
                "GAME_5": "",
                "GAME_6": "",
                "GAME_7": "",
                "GAME_8": "",
                "GAME_9": ""
            },
            "OpenAISettings": {
                "VoiceType": 0,
                "OpenAI_API_Key": "",
                "OpenAI_model_engine": "text-davinci-003",
                "OpenAI_Max_Tokens": 128,
                "OpenAI_Temperature": 0.5
            },
            "AppSettings": {
                "AlwaysOnTop": "False",
                "SpeakResponce": "False",
                "ResponsiveMode": "False",
                "NavigationState": "open",
                "DownloadsFolderName": "YT_Downloads",
                "DefaultFrame": "Home",
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
        except FileNotFoundError:
            with open(SETTINGSFILE, 'w') as settings_file:
                JSdump(default_settings, settings_file, indent=2)
            settings = default_settings
        observer.join()

    settings_thread = Thread(target=load_settings, name="settings_thread", daemon=True)
    settings_thread.start()

    global UserPowerPlans, settingsSpeakResponceVar, settingsAlwayOnTopVar, settingsResponsiveModeVar
    settingsSpeakResponceVar = BooleanVar()
    settingsAlwayOnTopVar = BooleanVar()
    settingsResponsiveModeVar = BooleanVar()

    UserPowerPlans = GetPowerPlans()

    if settings["AppSettings"]["AlwaysOnTop"] == "True":
        window.attributes('-topmost', True)
        settingsAlwayOnTopVar.set(True)
    else:
        window.attributes('-topmost', False)
        settingsAlwayOnTopVar.set(False)

    if settings["AppSettings"]["SpeakResponce"] == "True":
        settingsSpeakResponceVar.set(True)
    else:
        settingsSpeakResponceVar.set(False)

    if settings["AppSettings"]["ResponsiveMode"] == "True": # responsive mode is still in beta so it's disabled by default in settings.json
        window.resizable(True, True)
        settingsResponsiveModeVar.set(True)
    else:
        window.resizable(False, False)
        settingsResponsiveModeVar.set(False)
def restart():
    """Restarts app"""
    python = SYSexecutable
    execl(python, python, *SYSargv)
def on_closing():
    """App termination function"""
    Current_X = window.winfo_x()
    Current_Y = window.winfo_y()
    SaveSettingsToJson("Window_X", Current_X)
    SaveSettingsToJson("Window_Y", Current_Y)
    try: 
        observer.stop()
    except: pass
    window.destroy()
    exit()
def schedule_create(widget, ms, func, *args):
    """Schedules a function to run after a given time in milliseconds and saves the event id in a dictionary with the function name as the key"""
    event_id = widget.after(ms, func, *args)
    after_events[func.__name__] = event_id
def schedule_cancel(widget, func):
    """Cancels a scheduled function and deletes the event id from the dictionary using the function name as the parameter instead of the event id"""
    try:
        event_id = after_events.get(func.__name__)
        if event_id is not None:
            widget.after_cancel(event_id)
            del after_events[func.__name__]
    except: 
        pass
def UpdateTitleInfo():
    """Updates the title bar with the current time and date every second. If the navigation bar is closed, it shows the data in a different format"""
    schedule_cancel(navigation_frame_label, UpdateTitleInfo)
    if settings["AppSettings"]["NavigationState"] == "close":
        current_time = datetime.now().strftime('%I:%M %p')
        current_date = date.today().strftime('%d/%m/%Y')
    else:
        current_time = datetime.now().strftime('%I:%M:%S %p')
        current_date = date.today().strftime('%A, %B %d, %Y')
    navigation_frame_label.configure(text=f"{current_date}\n{current_time}")
    schedule_create(navigation_frame_label, 1000, UpdateTitleInfo)
def NavbarAction(option: str):
    """Opens or closes the navigation bar and saves the state to settings.json"""
    SaveSettingsToJson("NavigationState", str(option))
    if option == "close":
        for button in all_buttons:
            button.configure(text="", anchor="center")
        navigation_frame_label.pack_configure(padx=7)
        navigation_frame_label.configure(font=("sans-serif", 15, "bold"))
        close_open_nav_button.configure(image=openimage, command=lambda: NavbarAction("open"))
        window.minsize(550, 400)
    elif option == "open":
        for button in all_buttons:
            button.configure(text=all_buttons_text[all_buttons.index(button)], anchor="w")
        navigation_frame_label.pack_configure(padx=20)
        navigation_frame_label.configure(font=("sans-serif", 18, "bold"))
        close_open_nav_button.configure(image=closeimage, command=lambda: NavbarAction("close"))
        window.minsize(650, 400)
    UpdateTitleInfo()

def systemsettings(setting: str):
    """Launches different settings within windows 10 and 11 (only tested on windows 11)"""
    if setting == "power":
        Popen('cmd.exe /c control powercfg.cpl', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "display":
        Popen('cmd.exe /c control desk.cpl', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "network":
        Popen('cmd.exe /c %systemroot%\system32\control.exe /name Microsoft.NetworkAndSharingCenter', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "sound":
        Popen('cmd.exe /c control mmsys.cpl sounds', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "apps":
        Popen('cmd.exe /c start ms-settings:appsfeatures', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW) # Put "appwiz.cpl" for control center version
    elif setting == "storage":
        Popen('cmd.exe /c start ms-settings:storagesense', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "windowsupdate":
        Popen('cmd.exe /c %systemroot%\system32\control.exe /name Microsoft.WindowsUpdate', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "taskmanager":
        Popen('cmd.exe /c taskmgr', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "vpn":
        Popen('cmd.exe /c start ms-settings:network-vpn', stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)
    elif setting == "netdrive":
        system('cmd.exe /c netdrive --reset')
        showinfo(title="Network drives reset", message="All network drives have been reset")
    else:
        pass
def LaunchGame(GameVar: str):
    """Launches selected game"""
    if (GameVar == None) or (GameVar == ""):
        showerror(title="No game link found", message="Make sure you have configured a game shortcut link in you're settings and try restarting the app")
    else:
        WBopen(GameVar)
        notification.notify("Management Panel", "Your game is now launching.", timeout=6)
def SocialMediaLoader(MediaVar: str):
    """Launches a website URL (either http or https)"""
    WBopen(MediaVar)

def CenterWindowToDisplay(Screen, width: int, height: int, x: int = None, y: int = None):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    if (x == None) and (y == None):
        x = (screen_width/2) - (width/2)
        y = (screen_height/2) - (height/2)
    return f"{width}x{height}+{int(x)}+{int(y)}"
def ResetWindowPos(x: bool = False, y: bool = False):
    """Resets window positions both x and y in settings.json"""
    if x:
        SaveSettingsToJson("Window_X", "")
    if y:
        SaveSettingsToJson("Window_Y", "")
    restart()
def AlwaysOnTopTrueFalse(value: bool):
    """Sets the window to always be on top or not and saves the state to settings.json"""
    window.attributes('-topmost', value)
    SaveSettingsToJson("AlwaysOnTop", str(value))
def ResponsiveModeTrueFalse(value: bool):
    """Sets the window to be resizable or not and saves the state to settings.json. Also sets the window size to 900x400 (this will be changed in the future)"""
    window.geometry("900x400")
    window.resizable(value, value)
    SaveSettingsToJson("ResponsiveMode", str(value))

def YTVideoDownloaderContentType(vidtype: str):
    """Updates the video content type to either .mp4 or .mp3 according to whatever was selected in the dropdown"""
    global YTVideoContentType
    YTVideoContentType = vidtype
def YTVideoDownloader(ContentType: str):
    """Downloads youtube videos and shows progress on GUI"""
    def DefaultStates(option: str):
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
            window.after(3500, lambda: DefaultStates(option="YTReset"))
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
                        window.after(4000, lambda: DefaultStates(option="ErrorReset"))
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
                        window.after(4000, lambda: DefaultStates(option="ErrorReset"))
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
                window.after(4000, lambda: DefaultStates(option="ErrorReset"))
            else:
                showerror(title="Unknown error occurred", message=f"An unknown error occurred. Heres the log: {viderror}")
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
    SpeechThread = Thread(name="SpeechThread", daemon=True, target=lambda: engineSpeak(audio))
    SpeechThread.start()
def ChatGPT():
    """Sends requests to ChatGPT and puts Response in text box"""
    UserText = assistant_responce_box_1.get("0.0", "end").strip("\n")
    if (UserText != "") and (UserText != None):
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
    # Execute the command without creating a window
    result = Popen(["powercfg", "/list"], stdout=PIPE, stderr=PIPE, stdin=PIPE, creationflags=CREATE_NO_WINDOW)

    # Wait for the command to complete and get the output
    output, error = result.communicate()

    # Decode the output
    output = output.decode("utf-8")
    error = error.decode("utf-8")

    # Process the output to extract power plan information
    PowerPlans = {line.split("(")[1].split(")")[0]: line.split(":")[1].split("(")[0].strip() for line in output.splitlines() if "GUID" in line}

    # Find the active power plan
    active = next(name for line in output.splitlines() if "*" in line for name in [line.split("(")[1].split(")")[0]] if "GUID" in line)

    # Assign the active power plan to the PowerPlans dictionary with the key "active"
    PowerPlans["active"] = active

    return PowerPlans
def ChangePowerPlan(PlanName: str):
    """Changes the selected power plan"""
    PowerPlanGUID = UserPowerPlans[PlanName]
    if PlanName not in UserPowerPlans:
        showerror(title="Power plan error", message=f"The power plan that you selected\n> {PlanName}\ndoesn't seem to exist.\nHeres the GUID: {PowerPlanGUID}")
        return
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

                percentage_label = CTkLabel(deviceFrame, text=f"Battery percentage: {str(percentage)}%", font=("Arial", 17))
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
    if (settings["Devices"] is None) or (len(settings["Devices"]) == 0) or (settings["Devices"] == ""):
        def defaultstates():
            refreshinglabel.destroy()
            devices_refresh_btn.configure(text="Load devices")
            devices_refresh_btn.grid(row=3, column=0, columnspan=2, padx=10, pady=20, sticky="ew")
        devices_refresh_btn.grid_forget()
        refreshinglabel = CTkLabel(devices_frame, text="No devices found", font=("Arial", 25))
        refreshinglabel.place(relx=0.5, rely=0.4, anchor="center")
        window.after(4000, defaultstates)
    else:
        Thread(name="DeviceUpdateThread", daemon=True, target=lambda: UpdateDevices()).start()

def select_frame_by_name(name: str):
    """Changes selected frame"""
    # set button color for selected button
    home_button.configure(fg_color=("gray75", "gray25") if name == "Home" else "transparent")
    games_button.configure(fg_color=("gray75", "gray25") if name == "Games" else "transparent")
    ytdownloader_button.configure(fg_color=("gray75", "gray25") if name == "YT Downloader" else "transparent")
    assistant_button.configure(fg_color=("gray75", "gray25") if name == "Assistant" else "transparent")
    socialmedia_button.configure(fg_color=("gray75", "gray25") if name == "Social Media" else "transparent")
    devices_button.configure(fg_color=("gray75", "gray25") if name == "Devices" else "transparent")
    system_button.configure(fg_color=("gray75", "gray25") if name == "System" else "transparent")
    settings_button.configure(fg_color=("gray75", "gray25") if name == "Settings" else "transparent")

    # show selected frame
    if name == "Home":
        home_frame.pack(fill="both", expand=True)
    else:
        home_frame.pack_forget()
    if name == "Games":
        games_frame.pack(anchor="center", pady=(0, 20), fill="x", expand=True)
    else:
        games_frame.pack_forget()
    if name == "Social Media":
        socialmedia_frame.pack(anchor="center", pady=(0, 20), fill="x", expand=True)
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
    if name == "Devices":
        devices_frame.pack(fill="both", expand=True)
        window.bind('<Control-r>', lambda event: AllDeviceDetails())
    else:
        devices_frame.pack_forget()
        window.unbind('<Control-r>')
    if name == "System":
        system_frame.pack(fill="both", expand=True)
    else:
        system_frame.pack_forget()
    if name == "Settings":
        settings_frame.pack(fill="both", expand=True)
    else:
        settings_frame.pack_forget()
def SaveSettingsToJson(ValueToChange: str, Value: str):
    """Saves data to settings.json file"""
    for Property in ['URLs', 'GameShortcutURLs', 'AppSettings', 'OpenAISettings']:
        if Property in settings and ValueToChange in settings[Property]:
            settings[Property][ValueToChange] = Value
            break
    else:
        showerror(title="settings error", message="There was an error when writing to the settings file")

    with open(SETTINGSFILE, 'w') as SettingsToWrite:
        JSdump(settings, SettingsToWrite, indent=2)
def responsive_grid(frame: CTkFrame, rows: int, columns: int):
    """Makes a grid responsive for a frame"""
    for row in range(rows+1):
        frame.grid_rowconfigure(row, weight=1)
    for column in range(columns+1):
        frame.grid_columnconfigure(column, weight=1)

window = CTk()
window.title("Management Panel")
window.protocol("WM_DELETE_WINDOW", on_closing)
StartUp()
if (settings["AppSettings"]["Window_X"] != "") and (settings["AppSettings"]["Window_Y"] != ""):
    window.geometry(CenterWindowToDisplay(window, 900, 400, settings["AppSettings"]["Window_X"], settings["AppSettings"]["Window_Y"]))
else:
    window.geometry(CenterWindowToDisplay(window, 900, 400))

# Bind keys Ctrl + Shift + Del to reset the windows positional values in the setting.json file then restart the app
window.bind('<Control-Shift-Delete>', lambda event: ResetWindowPos(True, True))

# Importing all icons and assigning them to there own variables to use later
try:
    homeimage = CTkImage(PILopen("assets/MenuIcons/about.png"), size=(25, 25))
    devicesimage = CTkImage(PILopen("assets/MenuIcons/devices.png"), size=(25, 25))
    gamesimage = CTkImage(PILopen("assets/MenuIcons/games.png"), size=(25, 25))
    ytdownloaderimage = CTkImage(PILopen("assets/MenuIcons/ytdownloader.png"), size=(25, 25))
    socialmediaimage = CTkImage(PILopen("assets/MenuIcons/socialmedia.png"), size=(25, 25))
    assistantimage = CTkImage(PILopen("assets/MenuIcons/assistant.png"), size=(25, 25))
    systemimage = CTkImage(PILopen("assets/MenuIcons/system.png"), size=(25, 25))
    settingsimage = CTkImage(PILopen("assets/MenuIcons/settings.png"), size=(25, 25))
    closeimage = CTkImage(PILopen("assets/MenuIcons/close.png"), size=(30, 30))
    openimage = CTkImage(PILopen("assets/MenuIcons/open.png"), size=(30, 30))
except Exception as e:
    showerror(title="Icon import error", message=f"Couldn't import an icon.\nDetails: {e}")
    exit()

# create navigation frame
navigation_frame = CTkFrame(window, corner_radius=0)
navigation_frame.pack(side="left", fill="y")

# menu buttons
close_open_nav_button = CTkButton(window, corner_radius=10, width=30, height=30, text="", fg_color="transparent", image=closeimage, anchor="w", hover_color=("gray70", "gray30"), command=lambda: NavbarAction("close"))
close_open_nav_button.pack(side="top", anchor="nw", padx=0, pady=5)
navigation_frame_label = CTkLabel(navigation_frame, text="", compound="left", font=("sans-serif", 18, "bold"))
navigation_frame_label.pack(side="top", padx=20, pady=20, anchor="w")
home_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="Home", fg_color="transparent", image=homeimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Home"))
home_button.pack(side="top", fill="x", padx=0, pady=0)
games_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="Games", fg_color="transparent", image=gamesimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Games"))
games_button.pack(side="top", fill="x", padx=0, pady=0)
socialmedia_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="Social Media", fg_color="transparent", image=socialmediaimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Social Media"))
socialmedia_button.pack(side="top", fill="x", padx=0, pady=0)
ytdownloader_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="YT Downloader", fg_color="transparent", image=ytdownloaderimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("YT Downloader"))
ytdownloader_button.pack(side="top", fill="x", padx=0, pady=0)
assistant_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="Assistant", fg_color="transparent", image=assistantimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Assistant"))
assistant_button.pack(side="top", fill="x", padx=0, pady=0)
devices_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="Devices", fg_color="transparent", image=devicesimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Devices"))
devices_button.pack(side="top", fill="x", padx=0, pady=0)
system_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="System", fg_color="transparent", image=systemimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("System"))
system_button.pack(side="top", fill="x", padx=0, pady=0)
settings_button = CTkButton(navigation_frame, corner_radius=10, width=0, height=40, text="Settings", fg_color="transparent", image=settingsimage, anchor="w", text_color=("gray10", "gray90"), font=("Arial", 22), hover_color=("gray70", "gray30"), command=lambda: select_frame_by_name("Settings"))
settings_button.pack(side="top", fill="x", padx=0, pady=0)

# main frames
# starting to work on responsive design for all frames/widgets.
home_frame = CTkFrame(window, corner_radius=0, fg_color="transparent") # responsive
games_frame = CTkFrame(window, corner_radius=0, fg_color="transparent") # responsive
socialmedia_frame = CTkFrame(window, corner_radius=0, fg_color="transparent") # responsive
ytdownloader_frame = CTkFrame(window, corner_radius=0, fg_color="transparent") # responsive
assistant_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
devices_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
system_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")
settings_frame = CTkFrame(window, corner_radius=0, fg_color="transparent")

# Create elements/widgets for frames
home_frame_button_1 = CTkLabel(home_frame, text=f"Version: {LiveAppVersion} {ShowUserInfo}", font=("sans-serif", 28))
home_frame_button_1.pack(anchor="center", pady=(100, 0))
home_frame_button_2 = CTkLabel(home_frame, text=f"Creator/developer: {Developer}", font=("sans-serif", 28))
home_frame_button_2.pack(anchor="center", pady=10)
home_frame_button_3 = CTkLabel(home_frame, text=f"Last updated: {LastEditDate}", font=("sans-serif", 28))
home_frame_button_3.pack(anchor="center")

games_frame_button_1 = CTkButton(games_frame, width=200, text="Game 1", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_1"]))
games_frame_button_1.grid(row=0, column=1, padx=5, pady=20)
games_frame_button_2 = CTkButton(games_frame, width=200, text="Game 2", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_2"]))
games_frame_button_2.grid(row=0, column=2, padx=5, pady=20)
games_frame_button_3 = CTkButton(games_frame, width=200, text="Game 3", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_3"]))
games_frame_button_3.grid(row=0, column=3, padx=5, pady=20)
games_frame_button_4 = CTkButton(games_frame, width=200, text="Game 4", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_4"]))
games_frame_button_4.grid(row=1, column=1, padx=5, pady=20)
games_frame_button_5 = CTkButton(games_frame, width=200, text="Game 5", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_5"]))
games_frame_button_5.grid(row=1, column=2, padx=5, pady=20)
games_frame_button_6 = CTkButton(games_frame, width=200, text="Game 6", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_6"]))
games_frame_button_6.grid(row=1, column=3, padx=5, pady=20)
games_frame_button_7 = CTkButton(games_frame, width=200, text="Game 7", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_7"]))
games_frame_button_7.grid(row=2, column=1, padx=5, pady=20)
games_frame_button_8 = CTkButton(games_frame, width=200, text="Game 8", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_8"]))
games_frame_button_8.grid(row=2, column=2, padx=5, pady=20)
games_frame_button_9 = CTkButton(games_frame, width=200, text="Game 8", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: LaunchGame(settings["GameShortcutURLs"]["GAME_8"]))
games_frame_button_9.grid(row=2, column=3, padx=5, pady=20)

socialmedia_frame_button_1 = CTkButton(socialmedia_frame, width=200, text="Github", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["GITHUBURL"]))
socialmedia_frame_button_1.grid(row=0, column=1, padx=5, pady=20)
socialmedia_frame_button_2 = CTkButton(socialmedia_frame, width=200, text="Discord", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["DISCORDURL"]))
socialmedia_frame_button_2.grid(row=0, column=2, padx=5, pady=20)
socialmedia_frame_button_3 = CTkButton(socialmedia_frame, width=200, text="Youtube", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["YOUTUBEURL"]))
socialmedia_frame_button_3.grid(row=0, column=3, padx=5, pady=20)
socialmedia_frame_button_4 = CTkButton(socialmedia_frame, width=200, text="Instagram", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["INSTAGRAMURL"]))
socialmedia_frame_button_4.grid(row=1, column=1, padx=5, pady=20)
socialmedia_frame_button_5 = CTkButton(socialmedia_frame, width=200, text="TikTok", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["TIKTOKURL"]))
socialmedia_frame_button_5.grid(row=1, column=2, padx=5, pady=20)
socialmedia_frame_button_6 = CTkButton(socialmedia_frame, width=200, text="Twitter", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["TWITTERURL"]))
socialmedia_frame_button_6.grid(row=1, column=3, padx=5, pady=20)
socialmedia_frame_button_7 = CTkButton(socialmedia_frame, width=200, text="HyperNylium.com", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["WEBSITE"]))
socialmedia_frame_button_7.grid(row=2, column=1, padx=5, pady=20)
socialmedia_frame_button_8 = CTkButton(socialmedia_frame, width=200, text="Facebook", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: SocialMediaLoader(settings["URLs"]["FACEBOOK"]))
socialmedia_frame_button_8.grid(row=2, column=2, padx=5, pady=20)

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

assistant_responce_box_1 = CTkTextbox(assistant_frame, width=680, height=150, border_width=5, corner_radius=10, font=("sans-serif", 22), activate_scrollbars=True, border_color="#242424")
assistant_responce_box_1.grid(row=1, column=1, padx=0, pady=10)
assistant_responce_box_2 = CTkTextbox(assistant_frame, width=680, height=150, border_width=5, corner_radius=10, font=("sans-serif", 22), activate_scrollbars=True, border_color="#242424")
assistant_responce_box_2.grid(row=2, column=1, padx=0, pady=0)
assistant_frame_button_1 = CTkButton(assistant_frame, text="Submit question", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: ChatGPT())
assistant_frame_button_1.grid(row=3, column=1, padx=10, pady=20, sticky="ew")

devices_spacing_frame_1 = CTkLabel(devices_frame, width=340, height=0, text="").grid(row=0, column=0, padx=0, pady=0)
devices_spacing_frame_2 = CTkLabel(devices_frame, width=340, height=0, text="").grid(row=0, column=1, padx=0, pady=0)
devices_refresh_btn = CTkButton(devices_frame, text="Load devices", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: AllDeviceDetails())
devices_refresh_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=20, sticky="ew")

systemspacer = CTkLabel(system_frame, text="")
systemspacer.grid(row=0, column=0, padx=20, pady=10)
system_frame_button_1 = CTkButton(system_frame, text="VPN settings", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("vpn"))
system_frame_button_1.grid(row=1, column=1, padx=10, pady=10)
system_frame_button_2 = CTkButton(system_frame, text="Netdrive", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("netdrive"))
system_frame_button_2.grid(row=1, column=2, padx=10, pady=10)
system_frame_button_3 = CTkButton(system_frame, text="Installed apps", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("apps"))
system_frame_button_3.grid(row=1, column=3, padx=10, pady=10)
system_frame_button_4 = CTkButton(system_frame, text="Sound settings", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("sound"))
system_frame_button_4.grid(row=2, column=1, padx=10, pady=10)
system_frame_button_5 = CTkButton(system_frame, text="Display settings", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("display"))
system_frame_button_5.grid(row=2, column=2, padx=10, pady=10)
system_frame_button_6 = CTkButton(system_frame, text="Power settings", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("power"))
system_frame_button_6.grid(row=2, column=3, padx=10, pady=10)
system_frame_button_7 = CTkButton(system_frame, text="Storage settings", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("storage"))
system_frame_button_7.grid(row=3, column=1, padx=10, pady=10)
system_frame_button_8 = CTkButton(system_frame, text="Network setings", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("network"))
system_frame_button_8.grid(row=3, column=2, padx=10, pady=10)
system_frame_button_9 = CTkButton(system_frame, text="Windows update", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: systemsettings("windowsupdate"))
system_frame_button_9.grid(row=3, column=3, padx=10, pady=10)
system_frame_power_optionmenu = CTkOptionMenu(system_frame, values=list(UserPowerPlans.keys())[:-1], command=lambda PlanName: ChangePowerPlan(PlanName), fg_color="#343638", button_color="#4d4d4d", button_hover_color="#444", font=("sans-serif", 17), dropdown_font=("sans-serif", 15), width=200, height=30, anchor="center")
system_frame_power_optionmenu.grid(row=4, column=2, padx=0, pady=10)
system_frame_power_optionmenu.set(UserPowerPlans['active'])

settingsspacer = CTkLabel(settings_frame, text="")
settingsspacer.grid(row=0, column=0, padx=100, pady=30)
settingsAlwayOnTopswitch = CTkSwitch(settings_frame, text="Always on top", variable=settingsAlwayOnTopVar, onvalue=True, offvalue=False, font=("sans-serif", 22), command=lambda: AlwaysOnTopTrueFalse(settingsAlwayOnTopVar.get()))
settingsAlwayOnTopswitch.grid(row=1, column=1, padx=20, pady=10)
settingsResponsiveModeswitch = CTkSwitch(settings_frame, text="Responsive mode (beta)", variable=settingsResponsiveModeVar, onvalue=True, offvalue=False, font=("sans-serif", 22), command=lambda: ResponsiveModeTrueFalse(settingsResponsiveModeVar.get()))
settingsResponsiveModeswitch.grid(row=3, column=1, padx=20, pady=10)
settingsSpeakResponceswitch = CTkSwitch(settings_frame, text="Speak response from AI", variable=settingsSpeakResponceVar, onvalue=True, offvalue=False, font=("sans-serif", 22), command=lambda: SaveSettingsToJson("SpeakResponce", str(settingsSpeakResponceVar.get())))
settingsSpeakResponceswitch.grid(row=2, column=1, padx=20, pady=10)
settings_frame_button_1 = CTkButton(settings_frame, text="Reset window position", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: ResetWindowPos(True, True))
settings_frame_button_1.grid(row=4, column=1, padx=20, pady=10)
settings_frame_button_2 = CTkButton(settings_frame, text="Open settings.json", compound="top", fg_color=("gray75", "gray30"), font=("sans-serif", 22), corner_radius=10, command=lambda: startfile(SETTINGSFILE))
settings_frame_button_2.grid(row=5, column=1, padx=20, pady=10)


for widget in navigation_frame.winfo_children(): # add all buttons and their text to a list for later use
    if isinstance(widget, CTkButton):
        all_buttons.append(widget)
        all_buttons_text.append(widget.cget('text'))

select_frame_by_name(settings["AppSettings"]["DefaultFrame"]) # select default frame

UpdateTitleInfo() # start timer for title info that includes time and date info

# Make frames .grid responsive
responsive_grid(games_frame, 3, 3)
responsive_grid(socialmedia_frame, 3, 3)
responsive_grid(ytdownloader_frame, 4, 1)

if settings["AppSettings"]["NavigationState"] == "close": # get navigation state from settings.json
    NavbarAction("close")
else:
    NavbarAction("open")

if not exists(f"{UserDesktopDir}/Stuff/GitHub/Environment_Scripts/netdrive.bat"): # if my personel netdrive script is not available on the system, disable the button
    system_frame_button_2.configure(state="disabled")

window.mainloop()