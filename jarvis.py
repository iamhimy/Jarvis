import speech_recognition as sr
import webbrowser
import pyttsx3
import pyaudio
import os

print(" WELCOME SIR, I'M JARVIS")
pyttsx3.speak("welcome sir i am jarvis")
r=sr.Recognizer()
while True:
    with sr.Microphone() as source :
         print('Tell me something to do')
         pyttsx3.speak("Tell me something to do")
         audio=r.listen(source)
         print("okay got it")
    ch=r.recognize_google(audio)
    print("your command:",ch)
    #ch=input()
    if ("hello" in ch) and ("jarvis" in ch):
        pyttsx3.speak("hello sir")
    elif("how" in ch) and ("you" in ch):
        pyttsx3.speak("i am fine sir what about you")
    elif  ("date" in ch) and (("run" in ch) or ("show" in ch)):
        print('okay sir')
        pyttsx3.speak("okay sir")
        webbrowser.open("https://www.google.com/search?q=date&oq=date&aqs=chrome..69i57j46j0l6.1828j0j1&sourceid=chrome&ie=UTF-8")
    elif ("calendar" in ch) and (("run" in ch) and ("show" in ch)):
        print('okay sir')
        pyttsx3.speak("okay sir")
        webbrowser.open("https://www.timeanddate.com/calendar/")
    elif ("IP" in ch) and (("show" in ch) or ("what" in ch)):
        print('okay sir')
        pyttsx3.speak("okay sir")
        webbrowser.open("https://www.google.com/search?sxsrf=ALeKk00W75irEi4wKoNfgzWKmE_pcenDUQ%3A1602596368717&ei=EK6FX76lK_2N4-EPyZudMA&q=what+is+my+ip&oq=what+is+my&gs_lcp=CgZwc3ktYWIQARgAMggIABDJAxCRAjIICAAQsQMQkQIyAggAMgUIABCxAzICCAAyBQgAELEDMgIIADICCAAyBQgAELEDMgIIADoECAAQRzoHCCMQyQMQJzoECCMQJzoICAAQsQMQgwE6BAgAEEM6BAguEEM6CQgAEEMQRhD7AToHCAAQsQMQQzoFCC4QsQM6CAguEMcBEK8BOgQIABAKOgUIABDJAzoECC4QCjoKCC4QxwEQowIQCjoKCC4QxwEQrwEQCjoHCCMQ6gIQJzoNCAAQsQMQgwEQyQMQQzoHCAAQyQMQQzoFCAAQkQJQ64wDWNjHA2Cf1gNoBXACeAGAAbwCiAHwHJIBCDAuNi4xMC4xmAEAoAEBqgEHZ3dzLXdperABCsgBCMABAQ&sclient=psy-ab")

    elif ("list" in ch) and ("show" in ch):
        print('okay sir')
        pyttsx3.speak("okay sir")
        os.system("dir")
    elif ("ping" in ch) and ("Google" in ch):
        print('okay sir')
        pyttsx3.speak("okay sir")
        os.system("ping google.com")
    elif ("exit" in ch) or ("stop" in ch):
        break
    /*elif(("aws" in ch) or ("amazon" in ch)) and ("instance" in ch):
        print("which type of instance would you like ?")
        pyttsx3.speak("which type of instance would you like")
        typ=input("type:")
        print("\n")
        pyttsx3.speak("okay sir please give the following details")
        a=input("image id :")
        b=input("instance type:")
        c=int(input("no. of instances:"))
        d=input("subnet id :")
        #e=input("storage root:")
        f=input("security group name:")
        g=input("key name:")
        os.system("aws {0} run-instances --image-id {1} --instance-type {2} --count {3} --subnet-id {4} --security-group-ids {5} --key-name {6}".format(typ,a,b,c,d,f,g))*/  
    else:   
        print("not recogniosed command sir")
        pyttsx3.speak('sorry sir i can not do that')
