


<h1 align="center">App Information</h1>

<h3>
Version: v3.2.0<br><br>
Last updated Github Repo: 10/28/2022<br><br>
Description:<br>Computer control panel that has J.A.R.V.I.S, a Youtube video\audio downloader
</h3>

## Usage/Setup

1. Make sure to have the latest version of [python](https://www.python.org/downloads/). Python 3.7.0+ is compatible

2. Download the [Management_Panel source code](https://github.com/HyperNylium/Management_Panel/archive/refs/heads/main.zip) from Github

3. Un-zip the `Management_Panel-main.zip` file on your desktop (Read [Things to keep in mind](https://github.com/HyperNylium/Management_Panel#things-to-keep-in-mind) to learn why)

4. And launch the `Updater.exe` file in [administrator](https://www.digitalcitizen.life/run-as-admin-windows-11/#ftoc-heading-5) mode in order for everything to install correctly

## Things to keep in mind
- The program will automatically detect your home directorys desktop location. For example:<br>`C:\Users\[user]\Desktop)`

- The program will only work if its on your desktop directory (the whole folder). But you can change this behavior by opening `Management_Panel.py` in your preferred text editor then change the<br>`GetUserDesktopLocation = winshell.desktop()`<br> variable to:<br>`GetUserDesktopLocation = "[your preferred directory]"`<br>For example: <br>`GetUserDesktopLocation = "C:\Users\[user]\Downloads)"`

- You can download/un-zip this project where ever you want. But for now, it can only be run/executed from your desktop directory. You can make the folder a hidden folder and have a shortcut of the `Management_Panel.py` script to run it from whatever directory you want.

- Please keep in mind that the `Updater.exe` is only for installing the required libraries and small updates. The updater gets updates to lol. So, if it crashes once you try to launch it or click the "Check for updates" button, its because the links that it was using before are now not in use anymore or broken. Now since you know that be sure to check Github for updates all the time (or when the Updater.exe crashes) for updates until v4.5.0 at least

- If you do not open the `Updater.exe` file in [administrator](https://www.digitalcitizen.life/run-as-admin-windows-11/#ftoc-heading-5) mode then you'll need to uninstall the version of python that you installed as well as delete the Pacific folders that the python installer created. You could also do the `pip list -V` to view all of the libraries that are installed on your pc and the `pip uninstall [library name]` command to uninstall the libraries individually. But because there are 15 libraries to uninstall i highly suggest theleading all files corresponding to python and re-installing python should do the trick

> You can change whatever you want but this is the most stable i have been able to make it.<br>But, if you do make a more better looking/stable version please send me a link to your work [Here](http://www.hypernylium.com/en-en/customer-support/) ;)

> if you have any problems or questions please [send me a message](http://www.hypernylium.com/en-en/customer-support/)
