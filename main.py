import speech_recognition as sr
import webbrowser
# library that convert text into speech and only support english language
import pyttsx3  
import musiclibrary
import requests
import google.generativeai as genai

#creating object
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="a94e10db220d4692aa558c01f4f66672"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    # Configure your Gemini API key
    genai.configure(api_key="AIzaSyBiP3HJCO1KDGqkvlexosQDAQA-Pd16z74")

    model = genai.GenerativeModel("gemini-2.5-flash")  # Valid model
    response = model.generate_content(command)
    return response.text

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")  
    # for music 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    else:
        #let openAI handle the request
        output=aiProcess(c)
        speak(output)
        


if __name__=="__main__":
    speak("Initializing Friday .....")
    while True:
        #Listen for the wake word "Friday"
        #obtain audio from the microphone
        r=sr.Recognizer()
        # recognize speech using google
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio=r.listen(source , timeout=2  , phrase_time_limit=1)
            word=r.recognize_google(audio)
            print("recognizing...")

            if(word.lower()=="friday"):
                speak(" Hi ! How may i help you")
                # Listen for command
                with sr.Microphone() as source:
                    print("Friday Active...")
                    audio=r.listen(source )
                    command=r.recognize_google(audio)

                    processCommand(command)
        
        except Exception as e:
            print("Error; {0}".format(e))