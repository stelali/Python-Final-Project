# Status Report

#### Your name

Stela Licheva

#### Your section leader's name

Unsure

#### Project title

Reddit AITA

***

Short answers for the below questions suffice. If you want to alter your plan for your project (and obtain approval for the same), be sure to email your section leader directly!

#### What have you done for your project so far?

I have finished screenscraping comments and using sentiment analysis. The final product is an excel with the comment, whether there is an "AITA", "NTA", "ESH", or "NAH" consensus. Then, the percentage of negative, neutral, and positive words.

#### What have you not done for your project yet?

I have not created a portal thing to see the data. My partner Ernest will be in charge of that.

#### What problems, if any, have you encountered?

I wasn't able to download Flair the sentiment analysis package onto my laptop, so I used Vader instead.

Here is the code:
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

submission = reddit.submission(url="https://www.reddit.com/r/wallstreetbets/comments/z76bq4/elon_musk_declares_war_on_apple_puts/")

all_comments = {"Comment": [], "Consensus" : [], "Negative" : [],
                "Neutral" : [], "Positive" : [], "Overall" : []}


submission.comments.replace_more(limit=2)
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
         
    
print("YTA", YTA,"NTA", NTA, "ESH", ESH, "NAH", NAH, "None Mentioned", None_Mentioned)

# Saving the data in a pandas dataframe

print(len(all_comments["Comment"]), len(all_comments["Consensus"]))

top_posts = pd.DataFrame(all_comments)
top_posts.to_csv("AITA Comments.csv", index=True)