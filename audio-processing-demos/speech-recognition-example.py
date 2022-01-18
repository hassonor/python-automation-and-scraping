from speech_recognition import Recognizer, AudioFile

# pip install SpeechRecognition https://pypi.org/project/SpeechRecognition/
recognizer = Recognizer()

with AudioFile('files/speech2.wav') as audio_file:
    audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)
print(text)

''' 
Text From Audio :-):
I wanted Chief Justice of the Massachusetts Supreme Court in April the sjc's current leader Edward Hennessey reaches the mandatory retirement age of 70 and a successor is it

'''
