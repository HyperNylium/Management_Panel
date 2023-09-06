
# pyinstaller --onefile --icon=assets/AppIcon/Management_Panel_Icon.ico update.py

from os import system, getcwd, walk, makedirs, startfile
from json import load as JSload, dump as JSdump
from colorama import init as colorinit, Fore
from os.path import exists, join, relpath
from sys import exit, platform, argv
from shutil import copy2, rmtree
from time import sleep

colorinit()

RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.CYAN
RESET = Fore.RESET

clear_command = "cls" if platform == "win32" else "clear"

def on_closing():
    print(RESET)
    sleep(1.5)
    exit()

if len(argv) != 3:
    print(f"{RED}Error{RESET}: Invalid arguments count {len(argv)}. Expected argument count 4. Passed arguments:\n")
    for arg in argv:
        print(f" -> {arg}")
    on_closing()

LiveAppVersion = argv[1]
SETTINGSFILE = argv[2]
error_count = 0
cwd = getcwd()

if exists(f"{cwd}\\Management_Panel.exe"):
    downurl = f"https://github.com/HyperNylium/Management_Panel/releases/download/v{LiveAppVersion}/Management_Panel-{LiveAppVersion}-windows.zip"
    local_path = f"{cwd}\\Management_Panel"
    expected_file_name = "Management_Panel.exe"
elif exists(f"{cwd}\\Management_Panel.py") or exists(f"{cwd}\\Management_Panel.pyw"):
    downurl = f"https://github.com/HyperNylium/Management_Panel/archive/refs/tags/v{LiveAppVersion}.zip"
    local_path = f"{cwd}\\Management_Panel-{LiveAppVersion}"
    expected_file_name = "Management_Panel.pyw"
else:
    print(f"{RED}Error{RESET}: Unable to determine which version to download. Please make sure you have either the executable or source code version of the Management_Panel in the same directory as this updater")
    on_closing()

system(clear_command)

print(f"\n{YELLOW}Installing v{LiveAppVersion} update...{RESET}")
try:
    disregard = ["update.exe", "VCRUNTIME140.dll", "VCRUNTIME140_1.dll", "python3.dll"]

    for root, dirs, files in walk(local_path):
        relative_path = relpath(root, local_path)
        dest_root = join(cwd, relative_path)

        makedirs(dest_root, exist_ok=True)

        for file in files:
            src_file = join(root, file)
            dest_file = join(dest_root, file)
            if not file.lower() in disregard:
                copy2(src_file, dest_file)

    rmtree(local_path)

    if exists(SETTINGSFILE):
        with open(SETTINGSFILE, 'r') as json_file:
            settings = JSload(json_file)

        if "AppSettings" in settings and "PreviouslyUpdated" in settings["AppSettings"]:
            settings["AppSettings"]["PreviouslyUpdated"] = "True"

        with open(SETTINGSFILE, 'w') as json_file:
            JSdump(settings, json_file, indent=4)

    print(f"{GREEN}Update installed successfully{RESET}")
except Exception as e:
    print(f"{RED}Error{RESET}: Encountered an error while installing the update:\n   {e}")
    error_count += 1

if error_count != 0:
    print(f"\n{YELLOW}Warning{RESET}: {error_count} errors occured during update. The update may have been installed incorrectly. Please try again later")

sleep(0.5)

try:
    print(f"\n{YELLOW}Restarting Management_Panel to finish install...{RESET}")
    startfile(join(cwd, expected_file_name))
except Exception as e:
    print(f"{RED}Error{RESET}: Unable to restart Management_Panel:\n   {e}")

on_closing()