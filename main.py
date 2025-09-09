import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import pyjokes
import time
recognizer=sr.Recognizer() 
engine = pyttsx3.init(driverName="sapi5")
engine.setProperty("rate", 150)   # speaking speed
engine.setProperty("volume", 1.0) # max volume

newsapi="d77773e95c904fdf8926497e0fc9abed"
url="https://newsapi.org/v2/top-headlines?country=us&apiKey=d77773e95c904fdf8926497e0fc9abed"

# speak function
def speak(text):
    engine.setProperty("rate", 150)   # slower speech
    engine.setProperty("volume", 1.0) # loud
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.3)  # prevent overlap with microphone




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
                articles = data.get('articles', [])
                for article in articles[:5]:
                    speak(article['title'])
        except:
            speak("Sorry, I couldn't fetch the news right now.")
    elif "tell joke" in c.lower():
        try:
            joke = pyjokes.get_joke()
            speak(joke)
        except Exception as e:
            speak("Sorry, I couldn't find a joke right now.")



if __name__ == "__main__":
    speak("Initializing Jack...")
    while True:
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
                word = recognizer.recognize_google(audio)
                speak("Recognition")
                if "jack" in word.lower():
                    print("Jack Activated...")

                    # Listen for the actual command
                    with sr.Microphone() as source:
                        audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
                        command = recognizer.recognize_google(audio)
                        processCommand(command)

        except sr.WaitTimeoutError:
            # No speech detected within timeout, just continue
            continue
        except Exception as e:
            print("Error:", e)
            continue