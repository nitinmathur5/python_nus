from twitter import *
import requests
import json
import csv
from pprint import pprint
from collections import Counter
from aylienapiclient import textapi
import matplotlib.pyplot as plt
#-----------------------------------------------------------------------
# filename for saving the twitter data
#-----------------------------------------------------------------------

filename = "twitter_project.csv"

#-----------------------------------------------------------------------
# Create Twitter API credentials 
#-----------------------------------------------------------------------

config = {"consumer_key" : "91Cdp6KsR8GT0trmDRvnYPjQb",
          "consumer_secret" : "RUH5eyyOFnTEEjtdC90pZabesGzl5KcG3BdoBnz82Cgl5KHR0f",
          "access_key" : "137959957-nChVNGjRC8aSzYOVS4myNgWsx3nTMlasejNSBWpT",
          "access_secret" : "wwmbZehdA6TUiJ4QxhkPaVhlXwAsCbS4Qh0Wl89NqT1Ox"}

#-----------------------------------------------------------------------
# Create AYLIEN credentials
#-----------------------------------------------------------------------
allient_client = textapi.Client("0e2d34c9", "d684b183362da22f89b510a2a71178d3")

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], 
                               config["consumer_key"], config["consumer_secret"]))


def write_header_to_a_csv_file():
    with open(filename, "ab") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["sno","created_at","screen_name","Sentiment", "Sentiment confidence", "tweet"])

def write_to_csv(sno,created_at, screen_name, sentiment_polarity, sentiment_confidence, tweet):
    with open(filename, "ab") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([sno,created_at,screen_name,sentiment_polarity,sentiment_confidence, tweet]) 

def get_sentiment(sentiment_string):
    response = allient_client.Sentiment({'text': sentiment_string})
    return (response['polarity'], str(response['polarity_confidence']))

def draw_plot():
    with open (filename, 'r') as data:
        counter = Counter()
        for row in csv.DictReader(data):
            counter[row['Sentiment']] +=1
        
        positive = counter['positive']
        negative = counter['negative']
        neutral = counter['neutral']
        colors = ['green', 'red', 'grey']
        sizes = [positive, negative, neutral]
        labels = 'Positive', 'Negative', 'Neutral'

        plt.pie(x=sizes,
        shadow=True,
        colors=colors,
        labels=labels,
        startangle=90)
        plt.title("Sentiment of {} Tweets about {}".format(tweetCount, searchQuery))
        plt.show()

#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
#-----------------------------------------------------------------------
maxTweets = 10000   # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
#searchQuery = 'ONGC'  # this is what we're searching for
searchQuery = raw_input("What stock do you want to analyze?\n")
tweetCount = 0
data = []

write_header_to_a_csv_file()

while (tweetCount < maxTweets) :
    if (tweetCount == 0) :
        query  = twitter.search.tweets(q = searchQuery,lang="en",count=tweetsPerQry)
    else :
        query  = twitter.search.tweets(q = searchQuery,lang="en",count=tweetsPerQry,max_id=max_id_str)

    #pprint (query)      
    for result in query["statuses"]:
        #print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
        data = [result["created_at"], result["user"]["screen_name"], result["text"]]
        data = map(lambda x: x.encode('unicode-escape').decode('utf-8'),data) 
        #print(data)
        print "Analyzing Tweet " + str(tweetCount)
        sentiment_polarity, sentiment_confidence = get_sentiment(data[2])
        write_to_csv(tweetCount,data[0], data[1], sentiment_polarity, str(sentiment_confidence), data[2])
        tweetCount += 1
    pprint(tweetCount)         
    try : 
        new_url = query["search_metadata"]["next_results"] 
        max_id_str =new_url.split("&")[0].split("=")[-1]
        pprint ((max_id_str))
        #pprint (data)       
    except KeyError: 
        print("No more tweets found")
        break
draw_plot()