
from py_compile import compile
from tkinter.filedialog import askopenfilename
from os.path import dirname, abspath
main_path = dirname(abspath(__file__))
file_path = askopenfilename(initialdir=main_path)
compile(file_path)