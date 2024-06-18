# NISHITA KADIYA 

        # TASK 1 : Voice Assistant

# Importing Necessary Libraries
import speech_recognition as sr     # gets user's voice speech as input and convert it into text
# for whether the output is on youtube or chrome
import pywhatkit
from gtts import gTTS 
# for user interface
import streamlit as stm    
import io
from datetime import datetime #for date and time

def get_user_voice1():
    
    # objects handles capturing voice input from microphone and converting it to text
    record1 = sr.Recognizer()

    with sr.Microphone() as source:
        stm.subheader(":blue Voice Assistant") # Title
        stm.markdown("---") # Horizontal Line
        stm.info(":green A Voice Assistant built in python and can perform various Tasks based on your Voice Commands. \n Such as Opening Chrome, Youtube, Checking Time and Data and Weather Checking")

        if stm.button(":blue Activate Voice Assistant"):

            # listening voice command of user input
            voice1 = record1.listen(source)
            
            # error mechanism so that it handles any connection error or user's speech will not indetified 
            try:
                txt = record1.recognize_google(voice1)
                stm.subheader(f":orange You Said : {txt}")
                return txt
            except sr.UnknownValueError:
                stm.error("I apologize, Could you please rephrase your question??")
                return None
            except sr.RequestError:
                stm.error("I apologize for not able to recognize your speech")
                return None
        else:
            return None

# converts text into speech using google's text to speech gtts 
def speok1(txt1): 
    txt_sp1 = gTTS(text=txt1, lang='en')   
    buff = io.BytesIO()
    txt_sp1.write_to_fp(buff)
    buff.seek(0)
    stm.audio(buff.read(), format='voice/mp3')   

def main():

    inputs1 = get_user_voice1()     # getting users input 

    # conditions
    if inputs1:
        
        if "hello" in inputs1.lower():
            ans = "Hello! I am Voice Assistant built in Python, How can I assist you "
            speok1(ans)
            stm.subheader(ans)

        elif "youtube" in inputs1.lower():
            # if youtube word is present then play it on yt by using 
            pywhatkit.playonyt(inputs1)

        elif "time" in inputs1.lower():
            ans = datetime.now().strftime("%H:%M") # used datetime librabr for getting time in form of hours nd minutes
            ans1 = f"The Current Time is {ans}."
            speok1(ans1)
            stm.subheader(ans1)

        elif "date" in inputs1.lower():
            t_date = datetime.now().strftime("%B %d, %y")
            ans1 = f"Today's date is {t_date}"
            speok1(ans1)
            stm.subheader(ans1)
        
        else:
            # seraching on google for weather or any web page
            pywhatkit.search(inputs1)
            ans = f"Search Results  '{inputs1}' : "
            speok1(ans)
            stm.subheader(ans)

if __name__ == "__main__":
    main()