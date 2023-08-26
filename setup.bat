@echo off

echo Installing required libraries...

pip cache remove *
pip install customtkinter==5.2.0
pip install plyer==2.1.0
pip install requests==2.31.0
pip install winshell==0.6
pip install Pillow==10.0.0
pip install openai==0.27.8
pip install pytube==15.0.0
pip install pyttsx3==2.90
pip install watchdog==3.0.0
pip install pygame==2.5.0
pip install numpy==1.25.2

echo Installation complete.
pause
start Management_Panel.pyw