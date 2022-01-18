from speech_recognition import Recognizer, AudioFile
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

recognizer = Recognizer()

with AudioFile('files/chile.wav') as audio_file:
    audio = recognizer.record(audio_file)

text = recognizer.recognize_google(audio)
print(text)

analyzer = SentimentIntensityAnalyzer()
scores = analyzer.polarity_scores(text)
print(scores)

if scores['compound'] > 0:
    print('Positive Speech Audio')
else:
    print('Negative Speech Audio')
