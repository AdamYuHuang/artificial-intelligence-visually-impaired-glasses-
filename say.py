import pyttsx3
engine=pyttsx3.init()
engine.setProperty('voice','zh')
def say(a):
    a=str(a)
    engine.say(a)
    engine.runAndWait()
    
while True:
	a=input("text")
	say(a)