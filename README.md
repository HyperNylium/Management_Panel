

# Management_Panel

## App Information

**Version:** v4.1.0\
**Project status:** Ready for update/download\
**Last updated Github Repo:** 5/2/2023

## Setup

1. Make sure to have the latest version of [Python](https://www.python.org/downloads/). Python 3.9.0 or above is recommended.

2. Download the [Management_Panel source code](https://github.com/HyperNylium/Management_Panel/archive/refs/heads/main.zip) from GitHub.

3. Unzip the `Management_Panel-main.zip` file wherever you want.

4. Install the required libraries in `requirements.txt`.

5. Launch `Management_Panel.pyw` and have fun! 😄

## New with this update

- Before, the app was only working with customtkinter version `4.1.2`, but now it works with `5.1.2` and above.

- Implemented settings file called `settings.json`. When the app first launches, it creates the settings file using the default settings in the current working directory. Then, once created, it gets all settings by reading that file. You can open the file by going to `settings > Open settings.json`.\
Default values for **settings.json**:
```json
{
  "URLs": {
    "WEBSITE": "http://hypernylium.com/",
    "GITHUBURL": "https://github.com/HyperNylium",
    "DISCORDURL": "https://discord.gg/4FHTjAgw95",
    "INSTAGRAMURL": "https://www.instagram.com/hypernylium/",
    "YOUTUBEURL": "https://www.youtube.com/channel/UCpJ4F4dMn_DIhtrCJwDUK2A",
    "TIKTOKURL": "https://www.tiktok.com/foryou?lang=en",
    "FACEBOOK": "https://www.facebook.com/HyperNylium/",
    "TWITTERURL": "https://twitter.com/HyperNylium"
  },
  "GameShortcutURLs": {
    "GAME_1": "",
    "GAME_2": "",
    "GAME_3": "",
    "GAME_4": "",
    "GAME_5": "",
    "GAME_6": "",
    "GAME_7": "",
    "GAME_8": ""
  },
  "OpenAISettings": {
    "VoiceType": 0,
    "OpenAI_API_Key": "",
    "OpenAI_model_engine": "text-davinci-003",
    "OpenAI_Max_Tokens": 128,
    "OpenAI_Temperature": 0.5
  },
  "AppSettings": {
    "AlwaysOnTop": "False",
    "SpeakResponce": "False",
    "Window_X": 318,
    "Window_Y": 232,
    "DownloadsFolderName": "YT_Downloads",
    "DefaultFrame": "About"
  },
  "Devices": []
}
```

- UI update.

- Integrated YouTube downloader.

- Integrated ChatGPT/OpenAI (you can change all of its settings in the `settings.json` file).

- New devices tab. When you have a Bluetooth mouse, keyboard, or headset, simply go to the `settings.json` file (you don't even need to close the app) and from the device manager in Windows under Bluetooth, find your device's name and put it in the `Devices` section like this:

```json
"Devices": [
  "YOUR DEVICE NAME",
  "BSK V3 PRO" // putting my own mouse name as an example.
] 
```

- You can directly change your power mode from the **System tab**. The dropdown will show you all available power modes, and the title of the dropdown will show you the active one (the mode that shows even when you didn't click the dropdown).

- Even if you are either downloading a file from YouTube or waiting for a response from ChatGPT, you can still switch through different tabs in the app. I wouldn't suggest this, but you can even change some settings from **settings.json**, and the thing would occasionally run (As I said, not recommended, but possible).

## Tested devices for "Devices" tab

- Razor Basilisk V3 Pro


## Things to keep in mind
- The program will automatically detect your computers desktop location (used for `YT_Downloader.py`)<br> For example: `C:\Users\[user]\Desktop)`

- The `Updater.exe` is only for installing the required libraries.

> if you have any problems or questions please [send me a message](http://www.hypernylium.com/en-en/customer-support/)
