


<h1 align="center">Management_Panel</h1>

## App Information

<h4>
Version: v3.7.0<br>
Project status: Ready for update/download<br>
Last updated Github Repo: 12/1/2022<br>
The beta program (closed): https://github.com/HyperNylium/Management_Panel_BETA
</h4>

## Usage/Setup

1. Make sure to have the latest version of [python](https://www.python.org/downloads/). Python 3.9.0 is recommended

2. Download the [Management_Panel source code](https://github.com/HyperNylium/Management_Panel/archive/refs/heads/main.zip) from Github

3. Un-zip the `Management_Panel-main.zip` file wherever you want

4. Launch the `Updater.exe` file and wait for it to install all of the libraries for you (Assuming you have python installed. If you don't this step will not work)
5. Launch `Management_Panel.py` and have fun ;)


## New with this update
- Minor bugs and mistakes fixed<br><br>

- Customtkinter update issue fixed<br><br>

- New command for `Jarvis`. Saying "jarvis lock my computer" will lock your computer (just like clicking `windows + L` keys but now included with jarvis)<br><br>

- New error catching method on importing critical libraries<br><br>

- You can now run/execute the app in whatever directory you want.<br><br>

- Optimized `Management_Panel` and `MP_MINI` (some of you were saying that the program was launching in 3 seconds. Well, now it should launch anywere between 400ms - 1.5s)<br><br>

- Full re-design of `MP_MINI` (Some text was to small and sometimes hard to read. So, i made things a bit bigger and easier to navigate)<br><br>

- Added "help" command to `Jarvis` (Whenever you say "jarvis help", jarvis will show you all of his commands for 5 seconds then go back to taking commands)<br><br>

- Modified `Updater.exe` to only install required libraries when launched<br><br>

- The `Updater.exe` now launches it self in [administrator mode](https://www.digitalcitizen.life/run-as-admin-windows-11/#ftoc-heading-5) so it can install the Libraries on your systems [PATH](https://www.maketecheasier.com/what-is-the-windows-path#incontent-ad1)<br><br>

- Updated the "Jarvis play music" function. Should now scan for .mp3 (more format support coming soon) files in your music dir (C:\Users\[user]\Music) and list them one by one.<br><br>
  For example:<br>
    [1] Musicfile1.mp3<br>
    [2] Musicfile2.mp3<br>
    [3] Musicfile3.mp3<br><br>
    All you need to do is type the number infront of the file name in the given input and wait for your song to launch. If `Jarvis` has any problems, he will let you know and return to taking commands shortly after that.<br><br>

## Things to keep in mind
- The program will automatically detect your computers desktop location (used for `YT_Downloader.py`)<br> For example: `C:\Users\[user]\Desktop)`

- The `Updater.exe` is only for installing the required libraries.

- The `Updater.exe` file requests [administrator](https://www.digitalcitizen.life/run-as-admin-windows-11/#ftoc-heading-5) privileges to run. If you click "No" when prompted, the updater will terminate itself and not run. The reason for that is, if you are going to download/install the required python libraries they need to be installed onto your computers PATH. Or else the program will have errors such as, crashing, not even launching, not able to find required files and more.<br><br>

> You can change whatever you want but this is the most stable i have been able to make it.<br>But, if you do make a more better looking/stable version please send me a link to your work [Here](http://www.hypernylium.com/en-en/customer-support/) ;)

> if you have any problems or questions please [send me a message](http://www.hypernylium.com/en-en/customer-support/)
