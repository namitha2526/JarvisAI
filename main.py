import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import pywhatkit
import webbrowser
import os
import json
import time
import random


# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 250)  # Speech speed
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice

MEMORY_FILE = "memory.json"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def talk(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()

def load_memory():
    if os.path.exists(MEMORY_FILE):
        with open(MEMORY_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_memory(data):
    with open(MEMORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

memory = load_memory()

def remember(key, value):
    memory[key] = value
    save_memory(memory)
    talk(f"Got it. I will remember that {key}.")

def recall(key):
    value = memory.get(key)
    if value:
        talk(f"You told me to remember this about {key}:")
        talk(value)
    else:
        talk(f"I don't remember anything about {key}.")

def wish_user():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        talk("Good morning, Namitha!")
    elif 12 <= hour < 18:
        talk("Good afternoon, Namitha!")
    else:
        talk("Good evening, Namitha!")
    talk("I am Jarvis. How can I help you?")

def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Namitha...")
        recognizer.pause_threshold = 2
        time.sleep(1.5)
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)
    try:
        print("Recognizing Namitha...")
        query = recognizer.recognize_google(audio, language='en-in')
        print("You said:", query)
        return query.lower()
    except Exception:
        talk("Sorry, say that again Namitha?")
        return ""

def run_jarvis():

    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why was the math book sad? Because it had too many problems.",
        "What do you call fake spaghetti? An impasta!"
    ]
    wish_user()
    while True:
        query = take_command()

        if query == "":
            continue

        if 'time' in query:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The time is {current_time}")

        elif 'tell me a joke' in query:
            joke = random.choice(jokes)
            talk(joke)

        elif 'who is' in query:
            person = query.replace('who is', '').strip()
            try:
                info = wikipedia.summary(person, sentences=1)
                talk(info)
            except Exception:
                talk(f"Sorry, I couldn't find information about {person}.")

        elif 'play' in query:
            song = query.replace('play', '').strip()
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'remember that' in query:
            talk("What should I remember?")
            key = take_command()
            if key:
                talk(f"tell me the details for {key}.you can say a paragraph too")
                value = take_command()
                if value:
                    remember(key, value)

        elif 'do you remember' in query or 'recall' in query:
            talk("What should I recall?")
            key = take_command()
            if key:
                recall(key)

        elif 'open google' in query:
            talk("Opening Google")
            webbrowser.open("https://www.google.com")

        elif 'open youtube' in query:
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif 'open stackoverflow' in query:
            talk("Opening Stack Overflow")
            webbrowser.open("https://stackoverflow.com")

        elif 'open code editor' in query:
            talk("Opening code editor")
            os.startfile(r"C:\Path\To\Your\CodeEditor.exe")

        elif 'open notepad' in query:
            talk("Opening Notepad")
            os.startfile("notepad.exe")

        elif 'open command prompt' in query:
            talk("Opening Command Prompt")
            os.startfile("cmd.exe")

        elif 'open calculator' in query:
            talk("Opening Calculator")
            os.startfile("calc.exe")

        elif 'open file explorer' in query:
            talk("Opening File Explorer")
            os.startfile("explorer.exe")

        elif 'search' in query:
            search_query = query.replace('search', '').strip()
            talk(f"Searching for {search_query}")
            webbrowser.open(f"https://www.google.com/search?q={search_query}")

        elif 'weather' in query:
            talk("Please tell me the city name.")
            city = take_command()
            if city:
                talk(f"Fetching weather information for {city}")
                webbrowser.open(f"https://www.weather.com/en-IN/weather/today/l/{city}")

        elif 'joke' in query:
            talk("Sure, here's a joke for you.")
            webbrowser.open("https://www.jokes.com")

        elif 'news' in query:
            talk("Fetching the latest news for you.")
            webbrowser.open("https://news.google.com")

        elif 'reminder' in query:
            talk("What would you like to be reminded about?")
            reminder = take_command()
            if reminder:
                talk(f"Setting a reminder for {reminder}")
                # Implement reminder feature if needed

        elif 'note' in query:
            talk("What would you like to note down?")
            note = take_command()
            if note:
                talk(f"Noting down: {note}")
                with open("notes.txt", "a") as file:
                    file.write(note + "\n")

        elif 'vs code' in query:
            talk("Opening Visual Studio Code")
            os.startfile(r"C:\Path\To\Your\VSCode.exe")

        elif 'open pdf' in query:
            talk("Opening PDF reader")
            os.startfile(r"C:\Path\To\Your\PDFReader.exe")

        elif 'open image viewer' in query:
            talk("Opening Image Viewer")
            os.startfile(r"C:\Path\To\Your\ImageViewer.exe")

        elif 'open video player' in query:
            talk("Opening Video Player")
            os.startfile(r"C:\Path\To\Your\VideoPlayer.exe")

        elif 'shutdown' in query:
            talk("Shutting down the system")
            os.system("shutdown /s /t 1")

        elif 'restart' in query:
            talk("Restarting the system")
            os.system("shutdown /r /t 1")

        elif 'sleep' in query:
            talk("Putting the system to sleep")
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        elif 'hibernate' in query:
            talk("Hibernating the system")
            os.system("shutdown /h")

        elif 'lock' in query:
            talk("Locking the system")
            os.system("rundll32.exe user32.dll,LockWorkStation")

        elif 'open settings' in query:
            talk("Opening Settings")
            os.startfile("ms-settings:")

        elif 'open task manager' in query:
            talk("Opening Task Manager")
            os.startfile("taskmgr.exe")

        elif 'open control panel' in query:
            talk("Opening Control Panel")
            os.startfile("control.exe")

        elif 'open terminal' in query:
            talk("Opening Terminal")
            os.startfile(r"C:\Path\To\Your\Terminal.exe")

        elif 'open spotify' in query:
            talk("Opening Spotify")
            os.startfile(r"C:\Path\To\Your\Spotify.exe")

        elif 'open discord' in query:
            talk("Opening Discord")
            os.startfile(r"C:\Path\To\Your\Discord.exe")

        elif 'open gmail' in query:
            talk("Opening Gmail")
            webbrowser.open("https://mail.google.com")

        elif 'open facebook' in query:
            talk("Opening Facebook")
            webbrowser.open("https://www.facebook.com")

        elif 'open twitter' in query:
            talk("Opening Twitter")
            webbrowser.open("https://www.twitter.com")

        elif 'open instagram' in query:
            talk("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        elif 'open linkedin' in query:
            talk("Opening LinkedIn")
            webbrowser.open("https://www.linkedin.com")

        elif 'open whatsapp' in query:
            talk("Opening WhatsApp")
            webbrowser.open("https://web.whatsapp.com")

        elif 'open telegram' in query:
            talk("Opening Telegram")
            webbrowser.open("https://web.telegram.org")

        elif 'open skype' in query:
            talk("Opening Skype")
            webbrowser.open("https://web.skype.com")

        elif 'open zoom' in query:
            talk("Opening Zoom")
            webbrowser.open("https://zoom.us")

        elif 'open microsoft teams' in query:
            talk("Opening Microsoft Teams")
            webbrowser.open("https://teams.microsoft.com")

        elif 'open google drive' in query:
            talk("Opening Google Drive")
            webbrowser.open("https://drive.google.com")

        elif 'open dropbox' in query:
            talk("Opening Dropbox")
            webbrowser.open("https://www.dropbox.com")

        elif 'open one drive' in query:
            talk("Opening OneDrive")
            webbrowser.open("https://onedrive.live.com")

        elif 'open calendar' in query:
            talk("Opening Calendar")
            webbrowser.open("https://calendar.google.com")

        elif 'open maps' in query:
            talk("Opening Maps")
            webbrowser.open("https://www.google.com/maps")

        elif 'open net mirror' in query:
            talk("Opening Net Mirror")
            webbrowser.open("https://netfree2.cc/home")

        elif 'wait'in query or 'wait for a second' in query:
            talk("Going to sleep mode. Say 'Jarvis' to wake me up.")
            break  # Exit run_jarvis, back to listening for wake word

        elif 'exit' in query or 'stop' in query:
            talk("Goodbye! Have a great day Namitha.")
            exit(0)  # Exit entire program

        else:
            talk("I didn't understand that.")

def listen_for_wake_word():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for wake word 'Jarvis'...")

        while True:
            try:
                audio = recognizer.listen(source)
                command = recognizer.recognize_google(audio).lower()
                print(f"Heard: {command}")

                if "jarvis" in command:
                    speak("Yes, Namitha?")
                    print("Wake word detected. Starting JARVIS...")
                    run_jarvis()
                    print("JARVIS session ended. Listening for wake word again...")
                    print("Say 'Jarvis' to start again.")
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Speech Recognition API failed")

def main():
    listen_for_wake_word()

if __name__ == "__main__":
    main()
