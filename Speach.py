import pyttsx3
import speech_recognition as sr

def text_to_speech(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Говоріть щось...")
        audio = recognizer.listen(source)
        print("Завершено розпізнавання голосу.")

    try:
        voice_input = recognizer.recognize_google(audio, language="uk-UA")
        print("Розпізнано: " + voice_input)
    except sr.UnknownValueError:
        print("Не вдалося розпізнати голос.")
        voice_input = ""

    # Отримуємо текст
    text_input = input("Введіть текст: ")

    # Відтворюємо вхідний голос
    text_to_speech(voice_input)

    # Зчитуємо текст
    text_to_speech(text_input)

if __name__ == "__main__":
    main()


