import pyttsx3
import speech_recognition as sr
import pywhatkit
import datetime
import wikipedia
import os

# Initialize speech engine
engine = pyttsx3.init()

# Speak function
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Listen function
def take_command():
    listener = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"User said: {command}")
    except:
        command = ""
    return command

# Open apps function (change paths according to your PC)
def open_apps(command):
    if "notepad" in command:
        os.startfile("C:\\Windows\\System32\\notepad.exe")
        talk("Opening Notepad")
    elif "calculator" in command:
        os.startfile("C:\\Windows\\System32\\calc.exe")
        talk("Opening Calculator")
    elif "chrome" in command:
        os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
        talk("Opening Chrome")
    else:
        talk("App not found")

# Run JARVIS
def run_jarvis():
    command = take_command()

    if "play" in command:
        song = command.replace("play", "")
        talk(f"Playing {song}")
        pywhatkit.playonyt(song)

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        talk(f"Current time is {time}")

    elif "who is" in command:
        person = command.replace("who is", "")
        info = wikipedia.summary(person, sentences=2)
        talk(info)

    elif "open" in command:
        open_apps(command)

    elif "exit" in command or "stop" in command:
        talk("Goodbye!")
        exit()
 
    else:
        talk("I did not understand. Can you repeat?")

# Keep JARVIS running
talk("Hello, I am your assistant JARVIS. How can I help you?")
while True:
    run_jarvis()
