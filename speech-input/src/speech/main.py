import speech_recognition as sr


def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        print("请说话：")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio, language='zh-CN')
        print("你说的是：", text)
    except sr.UnknownValueError:
        print("无法识别语音")
    except sr.RequestError as e:
        print("请求出错；{0}".format(e))


if __name__ == "__main__":
    recognize_speech()
