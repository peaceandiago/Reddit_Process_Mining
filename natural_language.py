from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import csv

"""
Input = comment (body - [3]) from the csv file and analyze the sentiment for each row
Output = sentiment analysis for each comment (http://www.nltk.org/howto/sentiment.html)
"""

#Open file
comments = open("comments1.csv", "r")
reader = csv.reader(comments)
next(reader,None)


SENTENCE = [] #take all the comments from the csv file into a global list

for words in reader:
    sentences = str(words[3])
    SENTENCE.append(sentences)


###ANALYZE THE SENTIMENT FOR EACH ROW IN SENTENCE LIST TO
###OUTPUT eg. compound: 0.8316, neg: 0.0, neu: 0.254, pos: 0.746,
sid = SentimentIntensityAnalyzer()
for sentence in SENTENCE:
    print(sentence)
    ss = sid.polarity_scores(sentence)
    for k in sorted(ss):
        print('{0}: {1}, '.format(k, ss[k]), end='')
    print()


