
#Quickstart: pip install SpeechRecognition. See the “Installing” section for more details.
# NOTE: this requires PyAudio because it uses the Microphone class

#Example 1
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    print("You said " + r.recognize(audio))    # recognize speech using Google Speech Recognition
except LookupError:                            # speech is unintelligible
    print("Could not understand audio")
    
    
#Example 2

import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("Transcription: " + r.recognize(audio))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
    
    
#Example 3

#Transcribe a WAV audio file and show the confidence of each:

import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("test.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    list = r.recognize(audio,True)                  # generate a list of possible transcriptions
    print("Possible transcriptions:")
    for prediction in list:
        print(" " + prediction["text"] + " (" + str(prediction["confidence"]*100) + "%)")
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")
    
    
#Example 4

#Listening in the background:

def callback(self, audio):
    try:
        print("You said " + self.recognize(audio))
    except LookupError:
        print("Oops! Didn't catch that")
r.listen_in_background(m, callback)

import time
while True: time.sleep(0.1)
