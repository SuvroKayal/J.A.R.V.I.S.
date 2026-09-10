import os
import webbrowser
import requests
import speech_recognition as sr
import pyttsx3
import musiclibrary
from client import ask_jarvis
from dotenv import load_dotenv

load_dotenv()

recognizer = sr.Recognizer()
newsapi = os.getenv("NEWS_API_KEY")

def speak(text):
    if not text:
        return

    try:
        # Re-initialize TTS engine on each invocation to prevent SAPI5 audio thread hanging
        engine = pyttsx3.init("sapi5")
        engine.setProperty("rate", 180)
        engine.say(str(text))
        engine.runAndWait()
        engine.stop()
        del engine
    except Exception as e:
        print(f"Speech Error: {e}")

def processCommand(c):
    c = c.lower().strip()

    # Website Section
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

    # News Section
    elif "news" in c:
        try:
            r = requests.get(
                f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}",
                timeout=10
            )
            data = r.json()

            if data.get("status") == "ok":
                headlines = data.get("articles", [])
                if headlines:
                    for article in headlines[:3]:
                        title = article.get("title")
                        if title:
                            speak(title)
                else:
                    speak("Sorry Boss, I could not find any news.")
            else:
                speak("Sorry Boss, I could not fetch the news.")

        except Exception as e:
            speak("Sorry Boss, I could not fetch the news.")

    # Music Section
    elif c.startswith("play "):
        song = c.split(" ", 1)[1].strip()
        link = next(
            (url for name, url in musiclibrary.music.items()
             if name.lower() == song.lower()),
            None
        )

        if link:
            webbrowser.open(link)
        else:
            speak("Sorry Boss, I could not find that song.")

    # AI Assistant Fallback
    else:
        response = ask_jarvis(c)
        speak(response)


if __name__ == "__main__":
    print("JARVIS: Initializing Jarvis...")
    speak("Initializing Jarvis...")

    try:
        microphone = sr.Microphone()
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)

        microphone_available = True
        print("Voice mode enabled.")

    except Exception as e:
        microphone_available = False
        microphone = None
        print("Text mode enabled.")

    while True:
        try:
            if microphone_available:
                try:
                    with microphone as source:
                        print("\nListening for 'Jarvis'...")
                        audio = recognizer.listen(
                            source,
                            timeout=5,
                            phrase_time_limit=3
                        )

                    word = recognizer.recognize_google(audio)

                    if word.lower().strip() == "jarvis":
                        speak("Yes Boss!")

                        with microphone as source:
                            audio_cmd = recognizer.listen(source, timeout=5, phrase_time_limit=7)

                        command = recognizer.recognize_google(audio_cmd)

                        if command.lower().strip() in ["exit", "quit", "bye"]:
                            speak("Goodbye Boss!")
                            break

                        processCommand(command)

                except sr.WaitTimeoutError:
                    continue

                except sr.UnknownValueError:
                    pass

                except sr.RequestError:
                    pass

                except OSError:
                    microphone_available = False

            else:
                word = input("\nYou: ").strip()

                if not word:
                    continue

                if word.lower() in ["exit", "quit", "bye"]:
                    speak("Goodbye Boss!")
                    break

                if word.lower() == "jarvis":
                    speak("Yes Boss!")
                    command = input("Command: ").strip()

                    if not command:
                        continue

                    if command.lower() in ["exit", "quit", "bye"]:
                        speak("Goodbye Boss!")
                        break

                    processCommand(command)
                else:
                    processCommand(word)

        except KeyboardInterrupt:
            print("\nExiting Jarvis...")
            break

        except Exception as e:
            pass