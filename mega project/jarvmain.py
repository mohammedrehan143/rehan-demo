                    
       

import speech_recognition as sr
import webbrowser
import pyttsx3 
import musiclib


recogniser = sr.Recognizer()
engine  = pyttsx3.init()

 
def speak(text):
    engine.say(text)
    engine.runAndWait()
  
def processcomand(c):# we can add what ever we want in this so as to make 
    #open the desired website
    if "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")   
        
        # we are going to add somg here for than we r goin to
        # add in this funcyion a code for plan 
        
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        speak("playing" + song )
        link = musiclib.music[song] 
        webbrowser.open(link)   
        
        #  we are going to AI power the responsive program by using open AI
        


if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:    
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("Listening...") 
                audio = r.listen(source, timeout=5, phrase_time_limit=10)
                
            word = r.recognize_google(audio)
            print("Heard:", word)

            if word.lower() == "jarvis":
                speak("Yes boss")
                with sr.Microphone() as source:
                    print("Jarvis active") 
                    audio = r.listen(source, timeout=5, phrase_time_limit=5)
                    command = r.recognize_google(audio)
                    print("Command:", command)
                    processcomand(command)

        except Exception as e:
            print("Error:", e)