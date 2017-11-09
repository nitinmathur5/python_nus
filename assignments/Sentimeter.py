from twitter import *
import requests
import json
import csv
from pprint import pprint

#-----------------------------------------------------------------------
# filename for saving the twitter data
#-----------------------------------------------------------------------

filename = "twitter_project.csv"

#-----------------------------------------------------------------------
# Create Twitter API credentials 
#-----------------------------------------------------------------------

config = {"consumer_key" : "ADbOq9myUWsmK5FmdrEdf11vF",
          "consumer_secret" : "VH7apE8RMU5QpdMAGK0RH1cWHy6GKLlAnFNWZfHA7rMWp1EwiQ",
          "access_key" : "1468729806-BBLS6GgiSPG1ucMo3FpqZoE2imASfd17kX3sWYc",
          "access_secret" : "vpepjZU08hTruTR1qI5pum6aQhjUkIX7b592KEvyfYW96"}

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(auth = OAuth(config["access_key"], config["access_secret"], 
                               config["consumer_key"], config["consumer_secret"]))

    

def write_header_to_a_csv_file():
    with open(filename, "ab") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["sno","created_at","screen_name","tweet"])

def write_to_csv(sno,created_at, screen_name, tweet):
    with open(filename, "ab") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([sno,created_at,screen_name,tweet]) 

#-----------------------------------------------------------------------
# perform a basic search 
# Twitter API docs:
# https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets.html
#-----------------------------------------------------------------------
maxTweets = 10000   # Some arbitrary large number
tweetsPerQry = 100  # this is the max the API permits
searchQuery = 'amd'  # this is what we're searching for




tweetCount = 0

data = []

write_header_to_a_csv_file()

while (tweetCount < maxTweets) :
    if (tweetCount == 0) :
        query  = twitter.search.tweets(q = searchQuery,lang="en",count=tweetsPerQry)
        #pprint (query)
        for result in query["statuses"]:
            #print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
            data = [result["created_at"], result["user"]["screen_name"], result["text"]]
            # this is to convert the unicode character in json format
            data = map(lambda x: x.encode('unicode-escape').decode('utf-8'),data) 
            #print(data)
            write_to_csv(tweetCount,data[0], data[1], data[2])
            tweetCount += 1
        pprint(tweetCount) 
    else :
        query  = twitter.search.tweets(q = searchQuery,lang="en",count=tweetsPerQry,max_id=max_id_str)
        #pprint (query)      
        for result in query["statuses"]:
            #print "(%s) @%s %s" % (result["created_at"], result["user"]["screen_name"], result["text"])
            data = [result["created_at"], result["user"]["screen_name"], result["text"]]
            data = map(lambda x: x.encode('unicode-escape').decode('utf-8'),data) 
            #print(data)
            write_to_csv(tweetCount,data[0], data[1], data[2])
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
