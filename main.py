import speech_recognition as sr 
import pyttsx3 

 #Initialize the speech recognition and the text-to-speech engines
r = sr.Recognizer()
engine = pyttsx3.init()

# Define a function to speak the text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Define a function to recognize speech
def listen():
    with sr.Microphone() as source:
        print("Speak now...")
        audio = r.listen(source)
    try: 
        text = r.recognize_google(audio)
        return text
    except:
        return None
    
# Main loop 
while True:
    command = listen()

    if command is None: