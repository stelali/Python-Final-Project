# Reddit API: https://www.reddit.com/prefs/apps
# PRAW Authentication: https://praw.readthedocs.io/en/latest/getting_started/authentication.html#read-only-application
# Beginning Screenscraping: https://www.geeksforgeeks.org/scraping-reddit-using-python/
# How to Use Praw: https://towardsdatascience.com/scraping-reddit-data-1c0af3040768
# VADER: https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/
# https://levelup.gitconnected.com/reddit-sentiment-analysis-with-python-c13062b862f6

# Steps Needed in Commend Window to Run
# 1. Install Pip
# 2. Install Praw: pip install praw
# 3. Install Vader: pip install vaderSentiment


import praw
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

reddit = praw.Reddit(client_id = "U5RLx7Yf_MviNDd2S_TSyA",
                     client_secret= "SxvYc20snZLTThLexc1X6nd5wLl1EQ",
                     user_agent= "Project by u/rate_my_professor")

subreddit = reddit.subreddit("AmItheAsshole")

posts = subreddit.hot(limit=10)

link = input("Insert link to AITA subreddit thread")
#"https://www.reddit.com/r/AmItheAsshole/comments/zblyc5/aita_for_crying_after_finding_out_my_mom_is/
submission = reddit.submission(url = link)

all_comments = {"Comment": [], "Consensus" : [], "Negative" : [],
                "Neutral" : [], "Positive" : [], "Overall" : []}


submission.comments.replace_more(limit=9)
# limit determines how deep into reddit it goes, but the farther it goes, the longer it takes
# 9 takes around 25 seconds and gets 1,000 first-level comments in the comment forest

YTA = 0
NTA = 0
ESH = 0
NAH = 0
None_Mentioned = 0

for a_comment in submission.comments:
    all_comments["Comment"].append(a_comment.body)

    text = str(a_comment.body).split()

    # Deciding whether four categories are used
    index = 0
    
    for word in text:
        word = word.upper()

        if "YTA" in word:
            YTA += 1
            all_comments["Consensus"].append("YTA")
            break
        elif "NTA" in word:
            NTA += 1
            all_comments["Consensus"].append("NTA")
            break
        elif "ESH" in word:
            ESH += 1
            all_comments["Consensus"].append("ESH")
            break
        elif "NAH" in word:
            NAH += 1
            all_comments["Consensus"].append("NAH")
            break
        elif len(text)-1 == index:
            None_Mentioned += 1
            all_comments["Consensus"].append("")

        index +=1


    # Sentiment Analysis on text as whole
    text = str(text)
    # Create a SentimentIntensityAnalyzer object
    sid_obj = SentimentIntensityAnalyzer()
    # polarity_scores method of SentimentIntensityAnalyzer
    # object gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(text)
        
    all_comments["Negative"].append(sentiment_dict['neg']*100)
    all_comments["Neutral"].append(sentiment_dict['neu']*100)
    all_comments["Positive"].append(sentiment_dict['pos']*100)
    
    if sentiment_dict['compound'] >= 0.05 :
        all_comments["Overall"].append("Positive")
    elif sentiment_dict['compound'] <= - 0.05 :
        all_comments["Overall"].append("Negative")
    else:
        all_comments["Overall"].append("Neutral")
         
total = len(all_comments["Comment"])    
import webbrowser

f = open('finalproject.html','w')


answers = ("<font size=12><strong>YTA:</strong>" + str(YTA) + "<br><strong>NTA:</strong>"+ str(NTA)  + "<br><strong>ESH:</strong>"
           + str(ESH) + "<br><strong>NAH:</strong>" + str(NAH) + "<br><strong>None Mentioned:</strong>" + str(None_Mentioned) + "<br><strong>Total Comments:</strong>" + str(total) + "</font>")
message = """<html>
<head></head>
<body><p>""" + answers + """ </p></body>
</html>"""

f.write(message)
f.close()

#have to change file path in order to open it
filename = 'file:///Users/ernest/Documents/College/Intro to Phython/' + 'finalproject.html'
webbrowser.open_new_tab(filename)
# Saving the data in a pandas dataframe



top_posts = pd.DataFrame(all_comments)
top_posts.to_csv("AITA Comments.csv", index=True)


