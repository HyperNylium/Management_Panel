
import platform
import datetime
import webbrowser
import os
import time
from Management_Panel import App_Version, Website, GithubURL, DiscordURL, instagramURL, YoutubeURL, TikTokURL, FacebookURL, TwitterURL

try:
	import speech_recognition as sr
except:
	os.system("python -m pip install SpeechRecognition")
import speech_recognition as sr

try:
	import wikipedia
except:
	os.system("python -m pip install wikipedia")
import wikipedia

try:
	import pyjokes
except:
	os.system("python -m pip install pyjokes")
import pyjokes

try:
	import pyttsx3
except:
	os.system("python -m pip install pyttsx3")
import pyttsx3

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

# Text Colors
CLR_RED = "\033[31m"
CLR_GREEN = "\033[32m"
CLR_YELLOW = "\033[33m"
CLR_BLUE = "\033[34m"
CLR_CYAN = "\033[36m"
CLR_WHİTE = "\033[37m"
RESET_ALL = "\033[0m"

spacers = 20
date = datetime.date.today().strftime("%A, %B %d, %Y")
date2 = datetime.date.today().strftime("%d, %m, %Y")
strTime = datetime.datetime.now().strftime("%I:%M %p")

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
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print(CLR_YELLOW+ "  Recognizing..." + RESET_ALL)
        query = r.recognize_google(audio, language="en")
        print(f"\n  command: {query}\n")
        time.sleep(0.5)

    except Exception as e:
        print("    Say that again please...")
        time.sleep(0.5)
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
                print(CLR_CYAN + "\n  VERSION: " + App_Version + RESET_ALL)
                print(CLR_CYAN + "  CREATOR: HyperNylium" + RESET_ALL)
                speak("my version is" + App_Version + "and i was created by hypernylium")

            elif "jarvis play music" in query:
                music_dir = "C:/Users/david/Music"
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))

            elif 'jarvis tell me a joke' in query:
                speak(pyjokes.get_joke())

            elif "jarvis what's the time" in query:
                speak(f"    Current time is {strTime}")

            elif "jarvis open commands" in query:
                os.system(clear_command)
                print(CLR_GREEN + "\n\n     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                print(CLR_GREEN + "     |                  COMMANDS                      |                   OUTPUT                   |" + RESET_ALL)
                print(CLR_GREEN + "     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    Open commands                             " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Brings up this table of commands" + RESET_ALL + CLR_GREEN + "         | " + RESET_ALL)
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
                print(CLR_GREEN + "     | " + RESET_ALL + CLR_CYAN + "    open pc panel                             " + RESET_ALL + CLR_GREEN + " |   " + RESET_ALL + CLR_YELLOW + "Closes Jarvis and opens management panel" + RESET_ALL + CLR_GREEN + " | " + RESET_ALL)
                print(CLR_GREEN + "     +------------------------------------------------+--------------------------------------------+" + RESET_ALL)
                speak("these are my commands. when you say either of these, i will respond to you with an answer")
                time.sleep(5)

            elif "jarvis update software" in query:
                speak("Attempting to update software")
                time.sleep(0.6)
                speak("Opening software update tool")
                os.startfile("Updater.exe")
                exit()

            elif "jarvis open management panel" in query:
                speak(f"Attempting to open management panel project version {App_Version}")
                print(CLR_YELLOW, f"Attempting to open Management Panel project version {App_Version}", RESET_ALL)
                time.sleep(1.5)
                print(CLR_YELLOW, "Attempting to Grant access to files", RESET_ALL)
                time.sleep(1.5)
                print(CLR_GREEN, "File access granted", RESET_ALL)
                time.sleep(0.6)
                speak("Proceeding to launch Management Panel project")
                time.sleep(0.3)
                os.startfile("Management_Panel.py")
                exit()

            elif "jarvis shutdown" in query:
                hour = int(datetime.datetime.now().hour)
                if hour>=0 and hour<12:
                    print(CLR_RED , "\n  Shuting Down. Have a good Morning sir", RESET_ALL)
                    speak("Shut ing Down. Have a good Morning sir")
                    time.sleep(1)
                    exit()

                elif hour>=12 and hour<18:
                    print(CLR_RED, "\n  Shuting Down. have a good afternoon sir", RESET_ALL)
                    speak("Shut ing Down. have a good afternoon sir")
                    time.sleep(1)
                    exit()

                else:
                    print(CLR_RED , "\n  Shuting Down. have a good evening sir", RESET_ALL)
                    speak("Shut ing Down. have a good evening sir")
                    time.sleep(1)
                    exit()


if __name__ == "__main__":
    JARVIS()