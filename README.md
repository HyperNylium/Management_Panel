


<h1 align="center">App Information</h1>

<h3>
Version: v3.2.0<br><br>
Last updated Github Repo: 10/28/2022<br><br>
Description:<br>Computer control panel that has J.A.R.V.I.S, a Youtube video\audio downloader
</h3>

## Usage/Setup

1. Make sure to have the latest version of [python](https://www.python.org/downloads/). Python 3.7.0+ is compatible

2. Download the [Management_Panel source code](https://github.com/HyperNylium/Management_Panel/archive/refs/heads/main.zip) from Github

3. Un-Zip the `Management_Panel-main.zip` file in your desktop (Read (Things to keep in mind)[https://github.com/HyperNylium/Management_Panel#notes-to-keep-in-mind] to find why)

4. And launch the `Updater.exe` file in [administrator](https://www.digitalcitizen.life/run-as-admin-windows-11/#ftoc-heading-5) mode in order for everything to install correctly

## Things to keep in mind
- The program will automatically detect your home directorys desktop location. For example:<br>`C:\Users\[user]\Desktop)`

- The program will only work if its on your desktop directory(the whole folder). But you can change this behavior by opening `Management_Panel.py` in your preferred text editor then change the<br>`GetUserDesktopLocation = winshell.desktop()`<br> variable to:<br>`GetUserDesktopLocation = "[your preferred directory]"`<br>For example: <br>`GetUserDesktopLocation = "C:\Users\[user]\Downloads)"`

- If you do not open the `Updater.exe` file in [administrator](https://www.digitalcitizen.life/run-as-admin-windows-11/#ftoc-heading-5) mode then you'll need to uninstall the version of python that you installed as well as delete the Pacific folders that the python installer created. You could also do the `pip list -V` to view all of the libraries that are installed on your pc and the `pip uninstall [library name]` command to uninstall the libraries individually. But because there are 15 libraries to uninstall i highly suggest theleading all files corresponding to python and re-installing python should do the trick

> You can change whatever you want but this is the most stable i have been able to make it.<br>But, if you do make a more better looking/stable version please send me a link to your work [Here](http://www.hypernylium.com/en-en/customer-support/) ;)

> if you have any problems or questions please [send me a message](http://www.hypernylium.com/en-en/customer-support/)
