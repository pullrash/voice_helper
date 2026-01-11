import group, os, webbrowser, subprocess, pyttsx3,time, pyautogui, datetime as d

#voice setings
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#all comands
def say_time(command):
    if "time" in command: 
        now = d.datetime.now()
        hour_12 = now.hour % 12
        hour_12 = 12 if hour_12 == 0 else hour_12  # щоб 0 → 12
        minute = now.minute
        am_pm = "AM" if now.hour < 12 else "PM"
        engine.say(f"The time is{hour_12} hour {minute} minute {am_pm}")

def what_opened(command):
    if "open" in command:
        command = command.split(" ")
        opened = command[command.index("open")+1]
        if opened == "browser":
            pyautogui.hotkey("win","1")
        elif opened == "code":
            pyautogui.hotkey("win","2")
        elif opened == "calculator":
            os.startfile("calc.exe")
        elif opened == "factorio":
            subprocess.Popen([r"C:\Program Files (x86)\Steam\Steam.exe", "-applaunch", "427520"])
        elif opened == "group":
            if command[command.index("open")+2] == "java":
                for url in group.group[f"{command[command.index("open")+2]}{command[command.index("open")+3]}"]:
                    webbrowser.open(url)
            for url in group.group[f"{command[command.index("open")+2]}"]:
                webbrowser.open(url)
        elif opened == "github" or opened == "any_sites":
            for url in group.group[f"{command[command.index("open")+1]}"]:
                webbrowser.open(url)
engine.runAndWait()