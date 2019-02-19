echo off

cls

:start

scp -P22 "root@10.16.169.120:/22/speech.txt" "C:\RobotSpeech\speech.txt"

C:\RobotSpeech\pyttsx-OT-2.py

goto start