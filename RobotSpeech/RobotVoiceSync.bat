echo off

cls

:start

scp -P22 "root@10.16.169.120:/22/speech.txt" "C:\RobotSpeech\speech.txt"

scp -P22 "root@10.16.169.120:/22/speechnumber.txt" "C:\RobotSpeech\Speech Validation\speechnumber.txt"

C:\RobotSpeech\pyttsx-OT-2.py

goto start