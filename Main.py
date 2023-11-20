import speech_recognition as sr
import json

settings = {
    "api": "Google",
    "mic_index": 6,
    "language": "ua-UA"
}

with open("settings.json", "w") as f:
    json.dump(settings, f)

with open("settings.json", "r") as f:
    settings = json.load(f)
    api = settings["api"]
    mic_index = settings["mic_index"]
    language = settings["language"]

with open("settings.json", "r") as f:
    settings = json.load(f)
    api = settings["api"]
    mic_index = settings["mic_index"]
    language = settings["language"]

print(f"Using {api} API")

mic = sr.Microphone(device_index=mic_index)

r = sr.Recognizer()

with mic as source:
    print("Say something!")
    audio = r.listen(source)

try:
    if api == "Google":
        recognized_text = r.recognize_google(audio, language=language)
    print(f"You said: {recognized_text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results; {e}")
