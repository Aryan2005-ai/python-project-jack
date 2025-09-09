import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pyjokes
import time

# recognizer + engine
recognizer = sr.Recognizer()
engine = pyttsx3.init("sapi5")

# configure voice
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)  # change index if needed
engine.setProperty("rate", 150)
engine.setProperty("volume", 1.0)

# news api
newsapi = "d77773e95c904fdf8926497e0fc9abed"
url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}"

# speak function
def speak(text):
    print("Speaking:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)  # prevent overlap with microphone

# process command function
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open spotify" in c.lower():
        webbrowser.open("https://www.spotify.com/")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            speak(f"Sorry, I don't have {song} in my library.")
    elif "tell news" in c.lower():
        try:
            r = requests.get(url)
            if r.status_code == 200:
                data = r.json()
                articles = data.get("articles", [])
                for article in articles[:5]:
                    speak(article["title"])
                    time.sleep(0.5)
        except:
            speak("Sorry, I couldn't fetch the news right now.")
    elif "tell joke" in c.lower():
        try:
            joke = pyjokes.get_joke()
            speak(joke)
        except Exception:
            speak("Sorry, I couldn't find a joke right now.")

# main loop
if __name__ == "__main__":
    speak("Initializing Jack...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                word = recognizer.recognize_google(audio)

                if "jack" in word.lower():
                    print("Wake word detected.")
                    speak("Jack Activated...")

                    # wait before listening again
                    time.sleep(1)

                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)

        except sr.WaitTimeoutError:
            continue
        except Exception as e:
            print("Error:", e)
            continue
