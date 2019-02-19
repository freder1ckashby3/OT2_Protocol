import os, sys, time, pyttsx3, subprocess
from shutil import copyfile

engine = pyttsx3.init()

speech_content = open('C:\\RobotSpeech\\speech.txt', 'r').read()
last_speech = open('C:\\RobotSpeech\\Speech Validation\\speech.txt', '+r').read()
closing_speech = open('C:\\RobotSpeech\\Speech Validation\\Close\\speech.txt', 'r').read()
	
if str(last_speech) == str(speech_content):
	print("...")
	time.sleep(1)
else:
	engine.say(speech_content)
	engine.runAndWait()
	print("ROBOT: " + speech_content)
	copyfile('C:\\RobotSpeech\\speech.txt', 'C:\\RobotSpeech\\Speech Validation\\speech.txt')
	time.sleep(1)