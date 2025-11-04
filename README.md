# 🎙️ Jack — Your Personal Voice Assistant

Jack is a Python-based voice-controlled personal assistant that can perform tasks like opening websites, playing music, fetching news headlines, and telling jokes — all hands-free!  
It uses **SpeechRecognition**, **pyttsx3**, and **NewsAPI** to interact intelligently through speech.

---

## 🚀 Features

| Category | Description |
|-----------|--------------|
| 🔊 **Voice Interaction** | Wake-word detection (“Jack”) with speech recognition and text-to-speech responses. |
| 🌐 **Web Navigation** | Opens popular websites like Google, YouTube, LinkedIn, Spotify, and Facebook. |
| 🎵 **Music Player** | Plays songs from a custom local music library. |
| 🗞️ **News Headlines** | Fetches the top U.S. headlines from the NewsAPI. |
| 😂 **Jokes** | Tells random programming jokes using `pyjokes`. |
| 🧠 **Modular Design** | Easy to add more commands and features. |

---

## 🧩 Tech Stack

- **Python 3.x**
- **Libraries Used**
  - `speech_recognition`
  - `pyttsx3`
  - `webbrowser`
  - `requests`
  - `pyjokes`
  - `time`
  - `musicLibrary` (custom module)

---

## ⚙️ Installation

### 1. Clone this repository
```bash

2. Install dependencies

Make sure you have Python installed, then run:

pip install -r requirements.txt


Example requirements.txt:

SpeechRecognition
pyttsx3
requests
pyjokes
pyaudio


⚠️ If pyaudio installation fails, install it manually using:

Windows: pip install pipwin && pipwin install pyaudio

macOS/Linux: brew install portaudio then pip install pyaudio

3. Add your NewsAPI key

Replace the key inside main.py:

newsapi = "YOUR_API_KEY_HERE"


or set it as an environment variable:

setx NEWS_API_KEY "your_api_key_here"


Sign up for a free key at: https://newsapi.org/

🎧 Usage

Run the assistant:

python main.py


Wait for Jack to initialize.

Say “Jack” to activate.

Then try commands like:

“Open Google”

“Play Shape of You”

“Tell news”

“Tell joke”

“Open YouTube”

“Exit”

🎶 Example Music Library

Create a file named musicLibrary.py in the same folder:

music = {
    "shape of you": "https://youtu.be/JGwWNGJdvx8",
    "believer": "https://youtu.be/7wtfhZwyrcc",
    "perfect": "https://youtu.be/2Vv-BfVoq4g"
}

🧠 How It Works

Wake Word Detection: Listens for “Jack” using SpeechRecognition.

Command Recognition: Processes speech input and identifies intent.

Execution: Executes predefined commands (open web, play music, etc.).

Response: Uses pyttsx3 to respond via text-to-speech.

🪲 Troubleshooting

Assistant doesn’t hear me:
Check your microphone settings or background noise.

PyAudio errors:
Reinstall PyAudio or check device permissions.

No response from Jack:
Make sure the wake word “Jack” is clearly spoken before giving commands.

💡 Future Enhancements

🗓️ Add reminders and alarms

🌦️ Fetch live weather updates

📚 Wikipedia summaries

🧭 Location-based services

💬 Conversation memory and context

👨‍💻 Author

Aryan Oberoi


📝 License

This project is licensed under the MIT License — feel free to use, modify, and share with credit.

“Jack listens, understands, and executes — your personal voice companion in Python!”
git clone https://github.com/<your-username>/Jack-Voice-Assistant.git
cd Jack-Voice-Assistant

---
