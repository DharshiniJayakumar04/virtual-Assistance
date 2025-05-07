import speech_recognition as sr
import pyttsx3
import time

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Recognize speech from microphone
def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for a command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said:", command)
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't understand that.")
        return ""
    except sr.RequestError:
        speak("Network error.")
        return ""

# Simulated home automation actions
def control_device(command):
    if "turn on the light" in command:
        speak("Turning on the light.")
        # Place actual control code here (like GPIO or API call)
    elif "turn off the light" in command:
        speak("Turning off the light.")
    elif "turn on the fan" in command:
        speak("Turning on the fan.")
    elif "turn off the fan" in command:
        speak("Turning off the fan.")
    elif "goodbye" in command or "exit" in command:
        speak("Goodbye!")
        return False
    else:
        speak("Sorry, I don't know how to do that.")
    return True

# Main loop
def main():
    speak("Hello! I am your home assistant. How can I help you?")
    running = True
    while running:
        command = listen_command()
        if command:
            running = control_device(command)
        time.sleep(1)

if __name__ == "__main__":
    main()
