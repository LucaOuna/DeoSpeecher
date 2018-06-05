from servo import compute 				#Code relative to servo-motor control
import speech_recognition as sr 		#The speech recognition python library
import time
import RPi.GPIO as GPIO					#Allow to work on GPIO
from subprocess import call 			#Allow to read and write audio files (here wav files)
import pyttsx							#Enable eSpeak module

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)


PIN = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

r = sr.Recognizer()

def textToWav(text,file_name):
	call(["espeak", "-w"+file_name+".wav", text])		#Convert text into audio signal and store it in a wav file called file_name.wav


while True:
	GPIO.wait_for_edge(PIN, GPIO.FALLING)			#Wait for pushing button
	print "Pressed"
	with sr.Microphone() as source:					
		textToWav("Ok !","hello")
		call(["aplay", "hello.wav"])				#Output sound = "Ok !"
		GPIO.output(20,GPIO.HIGH)					#Switch on green light to mean: "I'm ready to listen to you"
		r.adjust_for_ambient_noise(source)
		audio = r.listen(source)					#Register audio signal from microphone and store it into the variable audio
		GPIO.output(20,GPIO.LOW)					#Switch off the green light: "I finished the record"
	
	
	try:
		phrase = r.recognize_google(audio)			#Translate audio signal into text
		print('Google hears :' + phrase)
		if phrase.count('smell')==1:				#Case one: activate deodorant
			print('launch deodorant')
			textToWav("Oh, you, smell, very, bad","hello")		
            call(["aplay", "hello.wav"]) 			#Output sound = "Oh you smell very bad" (stored into the file hello.wav)
			GPIO.output(21,GPIO.HIGH)				#Switch on red led because you smell very bad (haha)
			compute()								#Action with servo-motor
			GPIO.output(21,GPIO.LOW)
		elif phrase.count('stop')==1:				#Case 2: If we say "stop", we stop the program (leave the while loop)
			print('goodbye')
			textToWav("Goodbye","hello")
                        call(["aplay", "hello.wav"])

			break
		elif phrase.count('repeat')==1:				#Case 3: the raspberry repeats all we say
			with sr.Microphone() as source:
                textToWav("Ok, I, will, repeat, boss","hello")
				call(["aplay", "hello.wav"])
				GPIO.output(20,GPIO.HIGH)
                		r.adjust_for_ambient_noise(source)
                		audio2 = r.listen(source)
                		GPIO.output(20,GPIO.LOW)
			try:
        		phrase2 = r.recognize_google(audio2)
        		print('Google hears :' + phrase2)
				textToWav(phrase2,'hello')
				call(["aplay", "hello.wav"])
                print('phrase: ', phrase2)
              
			except:
				print('error in repeat')
	except:
		print('Error ! I did not understand what you said')

GPIO.cleanup()
