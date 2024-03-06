import speech_recognition as sr 
import pyttsx3 
import webbrowser

# Initialize the speech recognition and the text-to-speech engines
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
    except Exception as e:
        print(f"Error: {e}")
        return None

# Main loop 
while True:
    command = listen()

    if command is None:
        continue 

    # Set reminder
    if "remind me" in command:
        speak("What should I remind you about")
        reminder = listen()
        speak(f"Sure, I'll remind you to {reminder} later.")
    
    # Create to-do list
    elif "create a to-do list" in command:
        speak("What are the tasks you want to add to the to-do list?")
        tasks = []
        while True:
            task = listen()
            if "stop" in task:
                break
            tasks.append(task)
        speak("Here's your to-do list:")
        for i, task in enumerate(tasks):
            speak(f"{i+1}. {task}")

    # Search the web 
    elif "search for" in command:
        query = command.replace("search for", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Here are the search results for {query}.")

    # Quit the program 
    elif "quit" in command:
        speak("Thank you for using Voice Assistant")
        break

    # If command is not recognized, continue to listen
    else:
        speak("I'm sorry, I didn't understand. Please try again.")
