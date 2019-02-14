import os, sys, time, pyttsx3, subprocess
from shutil import copyfile

engine = pyttsx3.init()

speech = open('C:\\RobotSpeech\\speech.txt', 'r')
speechnum = open('C:\\RobotSpeech\\Speech Validation\\speechnumber.txt', 'r')
old_speechnum = open('C:\\RobotSpeech\\Speech Validation\\old_speechnumber.txt', 'r')

speech_content = speech.read()
speech_check = int(speechnum.read())
last_speech = int(old_speechnum.read())

if last_speech == speech_check:
	print("Speech not yet updated.")
else:
	engine.say(speech_content)
	engine.runAndWait()
	print("ROBOT: " + speech_content)

copyfile('C:\\RobotSpeech\\Speech Validation\\speechnumber.txt', 'C:\\RobotSpeech\\Speech Validation\\old_speechnumber.txt')