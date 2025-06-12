import os
from os import path

import speech_recognition as sr

AUDIO_FILE = os.path.join(path.dirname(path.realpath(__file__)), "sparrow.wav")
audio = sr.AudioData.from_file(AUDIO_FILE)

r = sr.Recognizer()

try:
    content = r.recognize_vosk(audio, language='zh')
    print(f"Content from audio: {content}")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
