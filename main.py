import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from ecapture import ecapture as ec

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
    except:
        pass
    return command

def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif "your name" in command:
        talk("My name is Alexa , i am your assistant")

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        day = datetime.datetime.now().strftime('%A')
        msg = f"Current time is {time} And the day is {day}"
        talk(msg)


    elif 'are you single' in command:
        talk('I am in a relationship with Siri')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif "selfie" in command:
        ec.capture(0, "test", "img.jpg")
    elif "picture" in command:
        ec.capture(0, "test", "img1.jpg")
    elif "funny" in command:
        talk("I know ")
    elif command == "ok":
        talk("ok")
    elif "good morning" in command:
        talk("Good morning")
    elif "good evening" in command:
        talk("Good evening")
    elif "good night" in command:
        talk("Good Night , have a sweet dreams")
    elif "message" in command:
        if "wife" in command:
            talk("What is the message?")
            msg2=take_command()
            print(msg2)
            now = datetime.datetime.now()
            now10 = now + datetime.timedelta(minutes=2)
            print(now10)
            pywhatkit.sendwhatmsg("+919036870038",msg2, now10.hour,now10.minute)
            print("Message delivered")

    elif "what can you do" in command:
        talk("You can ask me to play songs"
             "ask about a person or ask me for a joke")

    elif "exit" in command:
        talk("Ok exiting program")
        exit()

    elif 'who is' in command:
        if 'tell me about' in command:
            person = command.replace('tell me about', '')
        else:
            person = command.replace('who is', '')
        print(person)
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)

    else:
        talk('Sorry i dont know that one.')



while True:
    run_alexa()
