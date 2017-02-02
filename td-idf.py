"""
Input - reddit comments from csv
Output - term frequency/inverse document frequency to get global list of top keywords
"""

import math
import csv
from textblob import TextBlob as tb

comments = open("comments1.csv", "r")
reader = csv.reader(comments)
next(reader,None)

bad_word =['we', 'Oh', 'oh', 'it', 'is', 'It', 'Is', 'You', 'you', 'We', 'we', 'A', 'a', 'The', 'the', 'do', 'Do'
           'So', 'so', 'In', 'in', 'He', 'he', 'She', 'she', 'Our', 'our', 'Not', 'not', 'That', 'that', 'These', 'these'
           'hes', 'shes', 'im']

all_comments = []
for comment in reader:
    document = comment[3].lower()
    tmp = document.split(' ')
    final_string = ""
    for a in tmp:
        if a not in bad_word:
            final_string = final_string + a + " "
    all_comments.append(final_string)

print(all_comments)

def tf(word, blob):
    return blob.words.count(word) / len(blob.words)

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob.words)

def idf(word, bloblist):
    return math.log(len(bloblist) / (1 + n_containing(word, bloblist)))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)


#isolate the comments into a list
bloblist = []
for comment in all_comments:
    lower_comment = comment.lower()
    bloblist.append(tb(lower_comment))

# print(bloblist)

# with open('frequency.csv', 'wb') as csvfile:
#     spamwriter = csv.writer(csvfile)

csvfile = open('frequency.csv','w')
spamwriter = csv.writer(csvfile)
# spamwriter.writerow(bytes("this is a string", 'UTF-8'))
for i, blob in enumerate(bloblist):
    # print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, bloblist) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        # print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))
        row = str(i+1) + "," + str(word) + "," + str(round(score, 5))
        print(row)
        # spamwriter.write(row)

csvfile.close()
