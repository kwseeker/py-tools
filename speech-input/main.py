import speech_recognition as sr

r = sr.Recognizer()

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))

# 使用麦克风进行语音输入
with sr.Microphone(device_index=15) as source:
    print("请说话：")
    audio = r.listen(source)

try:
    print("识别中...")
    text = r.recognize_google(audio, language='zh-CN')
    print("你说的是：", text)
except sr.UnknownValueError:
    print("无法识别语音")
except sr.RequestError as e:
    print(f"请求语音识别服务出错：{e}")
