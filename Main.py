import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime 
import wikipedia
import requests
import json

listener = sr.Recognizer()
machine=pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()    

def input_instruction():
    global instruction
    try:
        with sr.Microphone() as origin:
            talk("Listening")
            print("listening")
            speech=listener.listen(origin)
            instruction=listener.recognize_google(speech)
            instruction =instruction.lower()
            if "jarvis" in instruction:
                instruction=instruction.replace('jarvis'," ")
                return instruction
            else:
                return instruction
    except:
        pass
        return instruction     

def play_Jarvis():
    instruction=input_instruction()
    print(instruction)
    if "play" in instruction:
        song=instruction.replace("play","")
        talk("Playing"+song)
        pywhatkit.playonyt(song)
    elif 'time' in instruction:
        time=datetime.datetime.now().strftime("%I:%M%p")
        print(time)
        talk("Current Time"+time)
    elif 'who is' in instruction:
        instruction=instruction.replace("who is"," ")
        try:
            info=wikipedia.summary(instruction,2)
            print(info)
            talk(info)
        except wikipedia.exceptions.PageError:
            print("Sorry, But Wikipedia cannot exactly determine the page,Dont Worry I will Give the information ,Check this Google Page")
            talk("Sorry, But Wikipedia cannot exactly determine the page,Dont Worry I will Give the information ,Check this Google Page")
            pywhatkit.search(instruction)  
    elif 'date' in instruction:
        date=datetime.datetime.now().strftime("%d /%m /%Y")
        print(date)
        talk("Today's Date"+date)
    elif "how are you" in instruction:
        talk("I am Fine,How About You")
    elif 'your name' in instruction:
        talk("I am Jarvis,What can I do for You?")
    elif 'tell me about' in instruction:
        human=instruction.replace('tell me about',' ')
        pywhatkit.search(human)
    elif 'joke' in instruction:
        url = "https://official-joke-api.appspot.com/random_joke"
        res = requests.get(url)
        joke = json.loads(res.text)
        setup = joke['setup']
        punchline = joke['punchline']
        print(setup)
        talk(setup)
        print(punchline)
        talk(punchline)
    else:
        talk("Please Repeat") 

play_Jarvis()
