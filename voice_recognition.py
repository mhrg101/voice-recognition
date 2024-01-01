# Import the necessary libraries and modules
import speech_recognition as sr
import pyttsx3
import random
import pyjokes

# Create an instance of the voice recognizer
r = sr.Recognizer()

# Create an instance of the voice synthesizer
engine = pyttsx3.init()

# Change the language of the synthesizer to English
engine.setProperty("voice", "english")

# Define a function to speak to the user
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Define a function to listen to the user
def listen():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language="en-US")
            return text.lower()
        except:
            return ""


# Start the program
speak("Hello, I am Mónica, How can I help you?")
print("Hello, I am Mónica, How can I help you?")
text = listen()
#user must say the word joke and program will tell a joke
if "joke" in text:
    speak("Okay, I'm going to tell you a joke.")
    print("Okay, I'm going to tell you a joke.")
    jok = pyjokes.get_joke(language='en') # library to tell jokes
    print(jok) # Tell the joke
    speak(jok) # Tell the joke
else:
    speak("I'm sorry, I didn't understand you. Please repeat what you want me to do.")
    print("I'm sorry, I didn't understand you. Please repeat what you want me to do.")

speak("Thank you it is time to say goodbye")
print("Thank you it is time to say goodbye")
text = listen()
if "goodbye" in text or "goodbye" in text:
    speak("Have a nice day.")
    print("Have a nice day.")
else:
    speak("I'm sorry I am going. Please restart the program.")
    speak("I'm sorry, I am going. Please restart the program.")
