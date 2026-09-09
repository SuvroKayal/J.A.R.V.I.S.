import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    c = c.lower()

    if "open google" in c:
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com")

    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com")

    elif "open facebook" in c:
        webbrowser.open("https://www.facebook.com")

    elif "open instagram" in c:
        webbrowser.open("https://www.instagram.com")

    elif "open github" in c:
        webbrowser.open("https://github.com")

    elif "open gmail" in c:
        webbrowser.open("https://mail.google.com")

    elif "open whatsapp" in c:
        webbrowser.open("https://web.whatsapp.com")

    elif "open reddit" in c:
        webbrowser.open("https://www.reddit.com")

    elif "open twitter" in c or "open x" in c:
        webbrowser.open("https://x.com")

    elif "open chatgpt" in c:
        webbrowser.open("https://chatgpt.com")

    elif "open spotify" in c:
        webbrowser.open("https://open.spotify.com")

    elif "open amazon" in c:
        webbrowser.open("https://www.amazon.in")

    elif "open netflix" in c:
        webbrowser.open("https://www.netflix.com")

    elif "open google maps" in c or "open maps" in c:
        webbrowser.open("https://maps.google.com")

    elif "open google drive" in c or "open drive" in c:
        webbrowser.open("https://drive.google.com")

    elif "open google docs" in c:
        webbrowser.open("https://docs.google.com")

    elif "open google meet" in c or "open meet" in c:
        webbrowser.open("https://meet.google.com")

    elif "open google classroom" in c or "open classroom" in c:
        webbrowser.open("https://classroom.google.com")

    elif "open stackoverflow" in c or "open stack overflow" in c:
        webbrowser.open("https://stackoverflow.com")

    elif "open geeksforgeeks" in c or "open geeks for geeks" in c:
        webbrowser.open("https://www.geeksforgeeks.org")

    elif "open w3schools" in c:
        webbrowser.open("https://www.w3schools.com")

    elif "open coursera" in c:
        webbrowser.open("https://www.coursera.org")

    elif "open udemy" in c:
        webbrowser.open("https://www.udemy.com")

    elif "open hugging face" in c:
        webbrowser.open("https://huggingface.co")

    elif "open kaggle" in c:
        webbrowser.open("https://www.kaggle.com")

    elif "open pypi" in c:
        webbrowser.open("https://pypi.org")

    elif "open python" in c:
        webbrowser.open("https://www.python.org")
    elif c.startswith("play "):
        song = c.split(" ", 1)[1].strip()
        link = musiclibrary.music.get(song)

        if link:
            webbrowser.open(link)
        else:
            speak("Sorry Boss, I could not find that song.")
    else:
        print("Command not recognized.")

if __name__ == "__main__":
    speak("Initializing Jarvis...")

while True:
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source, timeout= 2, phrase_time_limit=1)
        word = r.recognize_google(audio)
        if(word.lower() == "jarvis"):
            speak("Yes Boss!")
            #Listen for command

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source)
                command = r.recognize_google(audio)
                processCommand(command)

    except Exception as e:
        print(f"Error! {format(e)}")
       

