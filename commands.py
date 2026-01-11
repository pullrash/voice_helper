import os, pyttsx3, datetime as d

#voice setings
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


#all comands
def say_time():
    engine.say(str(d.datetime.now().hour) + "hour" + str(d.datetime.now().minute) + "minute")




engine.runAndWait()