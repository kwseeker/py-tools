import os

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()

print(f"cwd: {os.getcwd()}")

# recognize speech using Vosk
try:
    with sr.Microphone() as source:
        while True:
            print("say something >>>")
            audio = r.listen(source)
            print("Vosk thinks you said: " + r.recognize_vosk(audio, language='zh'))
            # print("Whisper thinks you said: " + r.recognize_faster_whisper(audio))
except sr.UnknownValueError:
    print("could not understand audio")
except sr.RequestError as e:
    print("error; {0}".format(e))
except KeyboardInterrupt:
    print("Bye")
