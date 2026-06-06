from speech_to_text import record_audio, transcribe
from assistant import ask_ai
from text_to_speech import speak

while True:

    audio_file = record_audio()

    user_text = transcribe(audio_file)

    print("You:", user_text)

    if not user_text:
        continue

    if "goodbye" in user_text.lower():
        speak("Goodbye")
        break

    reply = ask_ai(user_text)

    print("Assistant:", reply)

    speak(reply)