# sentiment-analysis

Doing sentiment analysis using nltk and textblob


Used https://medium.com/@eleanor.watson/a-beginners-guide-to-performing-sentiment-analysis-on-text-with-python-3ce80dcac22e as reference

Quick Tips:
Do not name your files nltk.py and textblob.py 

Observations:
nltk's vader , seems to be cleaning out my exclamations before evaluating. thus losing some of the meaning of my sentences
However textBlob considers my excalamations, both the outputs have the same subjextivity but the polarity is different
