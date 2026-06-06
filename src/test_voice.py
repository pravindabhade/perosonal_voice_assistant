import pyttsx3

engine = pyttsx3.init()

engine.say("Testing voice")

engine.runAndWait()

print("Voice test completed")