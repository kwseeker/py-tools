from faster_whisper import WhisperModel

# model_size = "large-v3"

# path = "../../.tmp/faster-whisper-base"
path = "../../.tmp/faster-whisper-large-v3"

# model = WhisperModel(model_size_or_path=path)
#
# segments, info = model.transcribe("sparrow.mp3")
# for segment in segments:
#     print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

# Run on GPU with FP16
# model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="float16")
# 本机显卡 P104-100 不支持 float16 计算
# model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="float32")
model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="int8")
# or run on GPU with INT8
# model = WhisperModel(model_size_or_path=path, device="cuda", compute_type="int8_float16")
# or run on CPU with INT8
# model = WhisperModel(model_size_or_path=path, device="cpu", compute_type="int8")

wav_path = "../../.tmp/sparrow.wav"
# wav_path = "../../.tmp/first_snow.wav"

segments, info = model.transcribe(wav_path, beam_size=5, language="zh", vad_filter=True,
                                  vad_parameters=dict(min_silence_duration_ms=1000))

print("Detected language '%s' with probability %f" % (info.language, info.language_probability))

for segment in segments:
    print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))
