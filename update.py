
# pyinstaller --onefile --icon=assets/AppIcon/Management_Panel_Icon.ico update.py

from os import system, getcwd, walk, makedirs, remove, startfile
from colorama import init as colorinit, Fore
from os.path import exists, join, relpath
from sys import exit, platform, argv
from shutil import copy2, rmtree
from winshell import desktop
from zipfile import ZipFile
from requests import get
from time import sleep
from tqdm import tqdm

colorinit()

RED = Fore.RED
GREEN = Fore.GREEN
YELLOW = Fore.YELLOW
BLUE = Fore.CYAN
RESET = Fore.RESET

clear_command = "cls" if platform == "win32" else "clear"

def on_closing():
    print(RESET)
    sleep(2.5)
    exit()

if len(argv) != 3:
    print(f"{RED}Error{RESET}: Invalid arguments")
    on_closing()

CurrentAppVersion = argv[1]
DataTXTFileUrl = argv[2]
UserDesktopDir = desktop()
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
}
error_count = 0
cwd = getcwd()

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
except Exception as e:
    print(f"{RED}Error{RESET}: Unable to get data from server:\n   {e}")
    on_closing()


if exists(f"{cwd}\\Management_Panel.exe"):
    downurl = f"https://github.com/HyperNylium/Management_Panel/releases/download/v{LiveAppVersion}/Management_Panel-{LiveAppVersion}-windows.zip"
    local_path_zip = f"Management_Panel-{LiveAppVersion}-windows.zip"
    local_path = f"{cwd}\\Management_Panel"
    expected_path = f"Management_Panel.exe"
elif exists(f"{cwd}\\Management_Panel.py") or exists(f"{cwd}\\Management_Panel.pyw"):
    downurl = f"https://github.com/HyperNylium/Management_Panel/archive/refs/tags/v{LiveAppVersion}.zip"
    local_path_zip = f"Management_Panel-{LiveAppVersion}.zip"
    local_path = f"{cwd}\\Management_Panel-{LiveAppVersion}"
    expected_path = f"Management_Panel.pyw"
else:
    print(f"{RED}Error{RESET}: Unable to determine which version to download. Please make sure you have either the executable or source code version of the Management Panel in the same directory as the updater")
    on_closing()


if LiveAppVersion < CurrentAppVersion:
    print(f"{RED}Error{RESET}: Live version is older than current version")
    on_closing()

elif LiveAppVersion != CurrentAppVersion or LiveAppVersion > CurrentAppVersion:
    print(f"{YELLOW}Update available!\n{BLUE}{CurrentAppVersion} -> {LiveAppVersion}\n\n{YELLOW}Would you like to update?{RESET} ({GREEN}y{RESET}/{RED}n{RESET})")
    choice = input("> ").lower()
    if choice == "y":
        system(clear_command)

        print(f"\n{YELLOW}Downloading update...{RESET}")
        try:
            response = get(downurl, stream=True, timeout=3, headers=headers)
            total_size_in_bytes= int(response.headers.get('content-length', 0))
            block_size = 1024 # 1 Kibibyte
            progress_bar = tqdm(total=total_size_in_bytes, unit='KiB', unit_scale=True)
            with open(local_path_zip, 'wb') as file:
                for data in response.iter_content(block_size):
                    progress_bar.update(len(data))
                    file.write(data)
            progress_bar.close()
            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print(f"{RED}Error{RESET}: Something went wrong while downloading update file")
                on_closing()
            print(f"{GREEN}Downloaded update successfully{RESET}")

            sleep(1)

            print(f"\n{YELLOW}Extracting update...{RESET}")
            try:
                with ZipFile(local_path_zip, 'r') as zipObj:
                    zipObj.extractall()
                print(f"{GREEN}Update extracted successfully{RESET}")
            except Exception as e:
                print(f"{RED}Error{RESET}: Unable to extract update:\n   {e}")
                error_count += 1

            sleep(1)

            print(f"\n{YELLOW}Installing update...{RESET}")
            try:
                for root, dirs, files in walk(local_path):
                    relative_path = relpath(root, local_path)
                    dest_root = join(cwd, relative_path)

                    makedirs(dest_root, exist_ok=True)

                    for file in files:
                        src_file = join(root, file)
                        dest_file = join(dest_root, file)
                        copy2(src_file, dest_file)
                print(f"{GREEN}Update installed successfully{RESET}")
            except Exception as e:
                print(f"{RED}Error{RESET}: Unable to install update:\n   {e}")
                error_count += 1

            sleep(1)

            try:
                print(f"\n{YELLOW}Cleaning up...{RESET}")
                remove(local_path_zip)
                rmtree(local_path)
                print(f"{GREEN}Update cleaned up successfully{RESET}")
            except Exception as e:
                print(f"{RED}Error{RESET}: Unable to clean up update files:\n   {e}")

            if error_count == 0:
                print(f"\n{GREEN}Update complete{RESET}")

            sleep(1.5)

            print(f"\n{YELLOW}Restarting Management_Panel...{RESET}")
            startfile(join(cwd, expected_path))

        except Exception as e:
            print(f"{RED}Error{RESET}: Unable to download update:\n   {e}")
            on_closing()
    else:
        print(f"{RED}Update cancelled{RESET}")
        sleep(1.5)
        startfile(join(cwd, expected_path))
        on_closing()
else:
    print(f"{GREEN}You are on the latest version{RESET}")
    sleep(1.5)
    startfile(join(cwd, expected_path))

on_closing()