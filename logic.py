import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Говорите:")
    audio = r.listen(source)

try:
    text = r.recognize_whisper(audio)
    print(f"Текст: {text}")
except sr.UnknownValueError:
    print("Не удалось распознать речь")

