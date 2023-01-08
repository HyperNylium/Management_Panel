
from Management_Panel import App_Version, CurrentAppVersion, clear_command, GetUserDesktopLocation, Developer, Developer_Lowercase
from Management_Panel import Website, GithubURL, DiscordURL, instagramURL, YoutubeURL, TikTokURL, FacebookURL, TwitterURL, exit
from Management_Panel import CLR_RED, CLR_GREEN, CLR_YELLOW, CLR_BLUE, CLR_CYAN, CLR_WHITE, CLR_BLACK, CLR_MAGENTA, RESET_ALL
from time import sleep
import webbrowser
import platform
import datetime
import os

try:
	import speech_recognition as sr
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: speech_recognition\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install speech_recognition ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()

try:
	import wikipedia
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: wikipedia\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install wikipedia ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
	import pyjokes
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: pyjokes\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install pyjokes ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
	import pyttsx3
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: pyttsx3\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install pyttsx3 ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
	import pyaudio
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: pyaudio\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install pyaudio ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


try:
	import plyer
except:
    print("\033[31m" + "\nIt looks like you don't have a critical the python library: plyer\nPlease open the"  +  "\033[36m" + " 'Updater.exe' " + "\033[31m" + "to install all the libraries correctly or open your terminal in administrator mode and type" +  "\033[36m" + ' python -m pip install plyer ' + "\033[31m" + "to install correctly")
    sleep(8)
    exit()


###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
###
### Author/Creator: HyperNylium
###
### Command: pyinstaller --onefile jarvis.py
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

spacers = 20
date = datetime.date.today().strftime("%A, %B %d, %Y")
date2 = datetime.date.today().strftime("%d, %m, %Y")
strTime = datetime.datetime.now().strftime("%I:%M %p")
UserMusicDirectory = os.path.expanduser('~\\Music\\')

clear_command = "cls" if platform.system() == "Windows" else "clear"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Beginning():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        print("\n  Good Morning sir")
        speak("Good Morning sir")

    elif hour>=12 and hour<18:
        print("\n  Good Afternoon sir")
        speak("Good Afternoon sir")

    else:
        print("\n  Good Evening sir")
        speak("Good Evening sir")

    speak("What can i help you with today")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        os.system(clear_command)
        print(CLR_GREEN + "\n  Listening..." + RESET_ALL)
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print(CLR_YELLOW + "  Recognizing..." + RESET_ALL)
        query = r.recognize_google(audio, language="en")
        print(f"\n  command: {query}\n")
        sleep(0.5)

    except Exception as e:
        print("    Say that again please...")
        sleep(0.5)
        return "None"
    return query

def JARVIS():
    Beginning()
    while True:
            query = takeCommand().lower()

            if "jarvis tell me about" in query:
                speak(CLR_YELLOW + "    Searching Wikipedia..." + RESET_ALL)
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print("  " + results)
                speak(results)

            elif "jarvis say hi" in query:
                speak("hello there sir. how are you today?")

            elif "jarvis what's today" in query:
                speak(f"    Today is {date}. or. {date2}")

            elif "jarvis what's the date" in query:
                speak(f"    Today is {date}. or. {date2}")

            elif "jarvis open youtube" in query:
                webbrowser.open(YoutubeURL)
                speak("opened youtube")

            elif "jarvis open my website" in query:
                webbrowser.open(Website)
                speak("opened your website")

            elif "jarvis open github" in query:
                webbrowser.open(GithubURL)
                speak("opened github")

            elif "jarvis open instagram" in query:
                webbrowser.open(instagramURL)
                speak("opened instagram")

            elif "jarvis open tik-tok" in query:
                webbrowser.open(TikTokURL)
                speak("opened tik-tok")

            elif "jarvis open facebook" in query:
                webbrowser.open(FacebookURL)
                speak("opened facebook")
                
            elif "jarvis open discord" in query:
                webbrowser.open(DiscordURL)
                speak("opened discord")
            
            elif "jarvis open twitter" in query:
                webbrowser.open(TwitterURL)
                speak("opened twitter")
            
            elif "jarvis open gmail" in query:
                webbrowser.open("https://mail.google.com/")
                speak("opened gmail")

            elif "jarvis display info" in query:
                print(CLR_CYAN + f"\n  VERSION: {App_Version}"+ RESET_ALL)
                print(CLR_CYAN + f"  CREATOR: {Developer}" + RESET_ALL)
                speak(f"my version is {App_Version} and i was created by {Developer_Lowercase}")

            elif "jarvis play music" in query:
                speak("Checking your personal music directory")
                sleep(1)
                ListMusicDir = os.listdir(UserMusicDirectory)
                speak("Detected music directory")
                os.system(clear_command)
                print(CLR_CYAN + f"\n  Your music directory is: {UserMusicDirectory}" + RESET_ALL)
                speak("Fetching all file that end with a dot mp3 format")
                ListOfUserMP3 = []
                ListOfUserMP3FileOnly = []
                SongListNumber = 0
                for MusicFiles in ListMusicDir:
                    if MusicFiles.endswith(".mp3"):
                        ListOfUserMP3.append(f"  [{int(SongListNumber)}] " + MusicFiles + "\n")
                        ListOfUserMP3FileOnly.append(MusicFiles)
                        SongListNumber += 1
                    else:
                        pass
                NumberOfSongs = len(ListOfUserMP3)
                tostr = ''.join(ListOfUserMP3)
                speak("Fetching all music files complete. Returning all files found")
                def MusicDirFunc():
                    os.system(clear_command)
                    print( CLR_YELLOW + "\n  Avalible songs are:\n\n" + RESET_ALL + CLR_CYAN + tostr + RESET_ALL)
                    print(CLR_YELLOW + f"  Total number of songs are: {NumberOfSongs}" + RESET_ALL)
                    speak("Please pick what music file you want to listen to by typing the number in front of the file name below")
                    UserInput = input("\n  Which song do you want to play: ")
                    if UserInput == "q":
                        os.system(clear_command)
                        speak("Going back to main funtion.")
                        JARVIS()
                    else: pass
                    try:
                        UserInput = int(UserInput)
                        print(CLR_GREEN + f"\n  Now playing:{ListOfUserMP3FileOnly[UserInput]}" + RESET_ALL)
                        speak(f"Playing{ListOfUserMP3FileOnly[UserInput]}.")
                        os.startfile(UserMusicDirectory + ListOfUserMP3FileOnly[UserInput])
                    except:
                        os.system(clear_command)
                        print(CLR_RED + "\n  That file doesn't exist in your directory. please try again" + RESET_ALL)
                        speak("That file doesn't exist in your directory. please try again")
                        sleep(1)
                        MusicDirFunc()
                MusicDirFunc()

            elif 'jarvis tell me a joke' in query:
                speak(pyjokes.get_joke())

            elif "jarvis what's the time" in query:
                speak(f"    Current time is {strTime}")

            elif "jarvis open commands" in query:
                os.system(clear_command)
                print(CLR_GREEN + "\n\n     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                print(CLR_GREEN + "     |                  COMMANDS                      |                   OUTPUT                   |" + RESET_ALL)
                print(CLR_GREEN + "     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Open commands/help                        " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Brings up this table of commands" + RESET_ALL + CLR_GREEN + "         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    display system info                       " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Application info" + RESET_ALL + CLR_GREEN + "                         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Open [youtube, github, facebook, etc]     " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Opens websites" + RESET_ALL + CLR_GREEN + "                           | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Play music                                " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Playes music in wanted directory" + RESET_ALL + CLR_GREEN + "         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Tell me about [NAME]                      " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Searches Wikipedia for any given name" + RESET_ALL + CLR_GREEN + "    | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    What's the time                           " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Tells you the time" + RESET_ALL + CLR_GREEN + "                       | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    What's the date (or what's today)         " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Tells you the date" + RESET_ALL + CLR_GREEN + "                       | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Tell me a joke                            " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Tells you a joke" + RESET_ALL + CLR_GREEN + "                         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    shutdown                                  " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Closes J.A.R.V.I.S" + RESET_ALL + CLR_GREEN + "                       | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Update software                           " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Opens Updater.exe" + RESET_ALL + CLR_GREEN + "                        | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Say hi                                    " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Says Hi" + RESET_ALL + CLR_GREEN + "                                  | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Lock my computer                          " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Locks your pc" + RESET_ALL + CLR_GREEN + "                            | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    open management panel                     " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Closes Jarvis and opens management panel" + RESET_ALL + CLR_GREEN + " | " + RESET_ALL)
                print(CLR_GREEN + "     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                speak("these are my commands. when you say either of these, i will respond to you with an answer")
                sleep(5)

            elif "jarvis help" in query:
                os.system(clear_command)
                print(CLR_GREEN + "\n\n     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                print(CLR_GREEN + "     |                  COMMANDS                      |                   OUTPUT                   |" + RESET_ALL)
                print(CLR_GREEN + "     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Open commands/help                        " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Brings up this table of commands" + RESET_ALL + CLR_GREEN + "         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    display system info                       " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Application info" + RESET_ALL + CLR_GREEN + "                         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Open [youtube, github, facebook, etc]     " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Opens websites" + RESET_ALL + CLR_GREEN + "                           | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Play music                                " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Playes music in wanted directory" + RESET_ALL + CLR_GREEN + "         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Tell me about [NAME]                      " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Searches Wikipedia for any given name" + RESET_ALL + CLR_GREEN + "    | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    What's the time                           " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Tells you the time" + RESET_ALL + CLR_GREEN + "                       | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    What's the date (or what's today)         " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Tells you the date" + RESET_ALL + CLR_GREEN + "                       | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Tell me a joke                            " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Tells you a joke" + RESET_ALL + CLR_GREEN + "                         | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    shutdown                                  " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Closes J.A.R.V.I.S" + RESET_ALL + CLR_GREEN + "                       | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Update software                           " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Opens Updater.exe" + RESET_ALL + CLR_GREEN + "                        | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Say hi                                    " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Says Hi" + RESET_ALL + CLR_GREEN + "                                  | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Lock my computer                          " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Locks your pc" + RESET_ALL + CLR_GREEN + "                            | " + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    open management panel                     " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Closes Jarvis and opens management panel" + RESET_ALL + CLR_GREEN + " | " + RESET_ALL)
                print(CLR_GREEN + "     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                speak("these are my commands. when you say either of these, i will respond to you with an answer")
                sleep(5)

            elif "jarvis update software" in query:
                speak("Attempting to update software")
                sleep(0.6)
                speak("Opening software update tool")
                os.startfile("Updater.exe")
                exit()

            elif "jarvis open management panel" in query:
                print(CLR_YELLOW, f"Attempting to open Management Panel project version {App_Version}", RESET_ALL)
                speak(f"Attempting to open management panel project version {App_Version}")
                os.startfile("Management_Panel.py")
                exit()

            elif "jarvis shutdown" in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    print(CLR_RED , "\n  Shuting Down. Have a good Morning sir", RESET_ALL)
                    speak("Shut ing Down. Have a good Morning sir")
                    sleep(1)
                    exit()

                elif hour>=12 and hour<18:
                    print(CLR_RED, "\n  Shuting Down. have a good afternoon sir", RESET_ALL)
                    speak("Shut ing Down. have a good afternoon sir")
                    sleep(1)
                    exit()

                else:
                    print(CLR_RED , "\n  Shuting Down. have a good evening sir", RESET_ALL)
                    speak("Shut ing Down. have a good evening sir")
                    sleep(1)
                    exit()

            elif "jarvis lock workstation" in query:
                print(CLR_YELLOW + "\n  Locking your workstation sir. Have a wonderful day" + RESET_ALL)
                speak("Locking your workstation sir. Have a wonderful day")
                sleep(1)
                os.system('cmd /c "rundll32.exe user32.dll,LockWorkStation"')
                sleep(1)
                plyer.notification.notify("Jarvis", "Your workstation has been locked.\nUntill next time sir", timeout=5)
                sleep(1)
                exit()


if __name__ == "__main__":
    JARVIS()