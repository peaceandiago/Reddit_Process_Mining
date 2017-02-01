import praw
import datetime
import csv

"""
This parses submission and comments from reddit r/PersonalFinanceCanada
Output: URL(unique ID), Submission Title, SCORE, USER, Date, Comment, SCORE USER, Date, More_Comments, SCORE, USER, Date
"""

reddit = praw.Reddit(user_agent='Getting comments',
                     client_id='CLIENT_ID', client_secret="SECRET",
                     username='USERNAME', password='PASSWORD')

personalfinancecanada = reddit.subreddit('PersonalFinanceCanada').hot(limit=25)
URL_LIST = [] #list of URL
SUBMISSION= [] # Submission ID, Title of submission, Score, Time/Date, Author
COMMENT = [] #Comment ID, Submission ID, Comment, Score, Time/Date, Author


#Iterate over each submission to parse links into a global dictionary
for submission in personalfinancecanada:
    URL_LIST.append(submission)

#Parse into each link from the dictionary and get title, score, and date/time
for submission in URL_LIST:
    submission_data = {}
    submission_data["submission_id"] = submission
    submission_data["timestamp"] = datetime.datetime.fromtimestamp(submission.created_utc)
    submission_data["name"] = str(submission.title)
    submission_data["score"] = submission.score
    submission_data["author"]= str(submission.author)
    SUBMISSION.append(submission_data)
keys = SUBMISSION[0].keys()

print(SUBMISSION)

with open('submission_with_titles.csv', 'w', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(SUBMISSION)

for each_submission in URL_LIST:
    submission = reddit.submission(id=each_submission)
    submission.comments.replace_more(limit=None)
    comment_queue = submission.comments[:]
    for comment in submission.comments.list():
        comment = comment_queue.pop(0)
        commentsdata = {}
        commentsdata["submission_id"] = each_submission
        commentsdata["comment_id"] = comment.permalink
        commentsdata["author"]= str(comment.author)
        commentsdata["body"] = str(comment.body)
        commentsdata["score"] = comment.score
        commentsdata["timestamp"] = datetime.datetime.fromtimestamp(comment.created_utc)
        commentsdata["comment_parent_id"] = comment.parent_id
        COMMENT.append(commentsdata)
        comment_queue.extend(comment.replies)

    keys = COMMENT[0].keys()
print(COMMENT)

with open('comments.csv', 'w', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(COMMENT)

