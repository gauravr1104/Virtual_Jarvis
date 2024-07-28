import speech_recognition as sr
import webbrowser
import pyttsx3
import pywhatkit as kit

engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processcommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "play" in c.lower():
        kit.playonyt(c)
    elif "search" in c.lower():
        search_query = c.replace("search", "")
        kit.search(search_query)

if __name__=="__main__":
    speak("initialising jarvis....")
    while True:
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                print("listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=3 )
                print("recognizing....")
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("yes sir")
                with sr.Microphone() as source:
                    print("jarvis active....")
                    audio = r.listen(source,timeout=2,phrase_time_limit=3)
                command=r.recognize_google(audio)

                processcommand(command)
                
        except sr.WaitTimeoutError:
            print("Listening timed out while waiting for phrase to start")
        except sr.UnknownValueError:
            print("Google Web Speech API could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Web Speech API; {e}")
        except Exception as e:
            print(f"Error: {e}")



