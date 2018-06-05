import RPi.GPIO as GPIO 
import time 
def compute(): 
	GPIO.setmode(GPIO.BCM) 
	GPIO.setup(22, GPIO.OUT) 
	pwm = GPIO.PWM(22, 100) 
	pwm.start(0) 
	angle1= 15
	print('angle: ' + str(angle1))
	duty1 = float(angle1) / 18.0 + 2
	pwm.ChangeDutyCycle(duty1)
	time.sleep(3)
	angle2 =165
	print('angle: ' + str(angle2))
	duty2 = float(angle2) / 18.0 + 2
	pwm.ChangeDutyCycle(duty2)
	time.sleep(0.8)
