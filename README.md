# DeoSpeecher
By [Ounaïs Samawi](https://www.linkedin.com/in/ounais-samawi/) and [Luca La Fisca](https://www.linkedin.com/in/luca-la-fisca-28554415a/)

## Introduction
This project consists of speech recognition on Raspberry Pi. It performs a speech to text conversion as well as following voice controlled actions:
- Activate a deodorant
- Repeat sentences from microphone signal (speech to text then text to speech)
- Shut down the running program with the command "stop"

## Demonstration
[![Watch the video](https://raw.github.com/LucaOuna/DeoSpeecher/master/Demonstration/H&S.mp4)]
## Requirements
Once you have a Raspberry Pi with Python3 installed, you have to add some libraries for performing the project:
- [pip](https://pip.pypa.io/en/stable/)
```Shell
sudo apt-get install python3-pip
```
That allows libraries installation with "pip" command
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
```Shell
sudo pip install speechrecognition
```
That is the main library to convert speech to text
- [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/docs/)
```Shell
sudo pip install pyaudio
```
That is python audio I/O library
- [Pyttsx](https://pypi.org/project/pyttsx/)
```Shell
sudo pip install pyttsx
```
That contains "eSpeak" module to convert text to audio
- [Subprocess](https://docs.python.org/2/library/subprocess.html) (already installed in official python versions)
```Shell
sudo pip install subprocess
```
That contains the "call" function allowing to save text into audio wav file thanks to "eSpeak" module

## Hardware
There are different devices to connect on the Raspberry Pi:
- Microphone thanks to a USB sound card on input port
- Speakers directly connected to the output jack port
- Button with the following electric circuit
![alt text](https://raw.githubusercontent.com/LucaOuna/DeoSpeecher/master/Images/Electrical_circuit.png)
