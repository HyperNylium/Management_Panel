@echo off

echo Installing required libraries...

pip cache remove *
pip install -r requirements.txt

echo Installation complete.

start Management_Panel.pyw