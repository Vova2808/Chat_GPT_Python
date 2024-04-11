from VortexGPT import Client
from googletrans import Translator
import pyttsx3


translator = Translator()

while True:
    prompt = input("👦: ")
    try:
        resp = Client.create_completion("gpt3", prompt)
        print(f"🤖: {resp}")
        engine = pyttsx3.init()
        engine.say(resp)
        engine.runAndWait()
    except Exception as e:
        print(f"🤖: {e}")
