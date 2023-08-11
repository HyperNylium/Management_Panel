
# Compile into bytecode (.pyc, requires python to run) file
#############################################
# from py_compile import compile
# from tkinter.filedialog import askopenfilename
# from os.path import dirname, abspath
# main_path = dirname(abspath(__file__))
# file_path = askopenfilename(initialdir=main_path)
# compile(file_path)
#############################################



# Compile into executable (.exe, doesn't require python to run)
#############################################
from os import system, listdir, getcwd
from os.path import expanduser
from time import sleep
from sys import exit
from shutil import copytree
user = expanduser('~').replace('\\', '/')
current_dir = getcwd().replace('\\', '/')
cmd_line = f'pyinstaller --noconfirm --onedir --windowed --add-data "{user}/AppData/Local/Programs/Python/Python311/Lib/site-packages/customtkinter;customtkinter/" Management_Panel.pyw'
system(cmd_line)
src_dir = f"{current_dir}/assets/"
dest_dir = f"{current_dir}/dist/Management_Panel/assets/"
files = listdir(src_dir)
copytree(src_dir, dest_dir)
sleep(3)
exit()
#############################################