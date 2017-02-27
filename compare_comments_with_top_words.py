import csv
import nltk

comments = open("comments2.csv", "r", encoding="utf-8")
reader = csv.reader(comments)
next(reader,None)

all_comments = []
for comment in reader:
    document = comment[5].lower()
    tmp = nltk.word_tokenize(document)
    comment.append(tmp)
    all_comments.append(comment)
# print(all_comments)

words = open("top_words.csv", "r")
top_reader = csv.reader(words)
next(reader,None)
top_words = []
for word in top_reader:
    imp_doc = word[0]
    top_words.append(imp_doc)

# print(top_words)


for all in all_comments:
    doc_terms = all[7]
    if doc_terms in top_words: #compare each word in doc_terms in top_words
        print(doc_terms)
        match =+ 1





