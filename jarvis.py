import pyttsx3
import speech_recognition as sr
import pywhatkit as kit
import wikipedia
import datetime
import os
import time

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to audio input from the user
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
        return query.lower()
    except Exception as e:
        print("Sorry, I didn't understand that.")
        return None

# Function to greet the user based on time
def greet():
    hour = int(datetime.datetime.now().hour)
    if 6 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis, your assistant. How can I help you today?")

# Function to perform actions based on user query
def perform_task(query):
    if "play" in query and "music" in query:
        song = query.replace("play", "").replace("music", "")
        speak(f"Playing {song}")
        kit.playonyt(song)

    elif "time" in query:
        time_now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {time_now}")

    elif "search" in query:
        query = query.replace("search", "")
        speak(f"Searching for {query} on Wikipedia")
        results = wikipedia.summary(query, sentences=2)
        speak(results)

    elif "tell me about" in query:
        query = query.replace("tell me about", "")
        speak(f"Here is what I found about {query}")
        results = wikipedia.summary(query, sentences=2)
        speak(results)

    elif "open" in query:
        app = query.replace("open", "")
        speak(f"Opening {app}")
        os.system(f"start {app}")  # Windows
        # For Linux or Mac, you might use: os.system(f"open {app}") or os.system(f"xdg-open {app}")

    elif "exit" in query or "quit" in query:
        speak("Goodbye! Have a nice day!")
        exit()

    else:
        speak("Sorry, I didn't get that. Please try again.")

# Main function to run the assistant
def main():
    greet()

    while True:
        query = listen()
        if query:
            perform_task(query)

if __name__ == "__main__":
    main()
