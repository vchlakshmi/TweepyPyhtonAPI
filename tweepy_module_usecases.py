# -*- coding: utf-8 -*-
import tweepy, sys
import traceback
from pprint import pprint
import json
#How to use
#python tweepy_oauth_tweet.py "API Test Message"

#For posting tweets using the API (need WRITE permission)
#For WRITE permisssions, you need to register your mobile 
consumer_key    = 'DcUn75oC8cZm3H2vLolPEwJpm'
consumer_secret = 'Q8C0wrCvOt2kafqgDM0x7XD84YXDvoHpdXUgKVJBgwa6pG8vZ2'
access_token    = '1511458178-mAAG0IXulkVi6Nod18w3G78gJv4JEmzbXjpc76J'
access_token_secret = 'epu9vynJ8vCCOYeK16S1OL0e8G8Ko2zM3pIMMYeP0fTEd'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print "Success logged in as " + api.me().name + "."

def get_user_friends():
    try:
        #print "\n\nUser Time Line"
        #for status in api.user_timeline():
        #    print status.id

        # Iterate through all of the authenticated user's friends
        for friend in tweepy.Cursor(api.friends).items():
            #pprint (vars(friend)) #This will print the Friend Twitter object
            friends_str = "\n\n*******\nFriend Name: %s\nFriend Id: %s\nFriend Screen Name: %s\nAccount Created At: %s\nLocation: %s\nFriends Count: %s" % (friend.name, friend.id, friend.screen_name, friend.created_at, friend.location,friend.friends_count)
            print friends_str
            #Pass the values into hash
            # freinds = {}
            # friends[name] = friend.name
            # friends[id] = friend.name    
            # friends[screen_name] = friend.name

    except Exception:
        print traceback.format_exc()
    finally:
        print "Finished get_user_friends"

def get_trends_place():
#Top Trends Weekly
    try:
        trends1 = api.trends_place(1) 
        data = trends1[0] 
        # grab the trends
        trends = data['trends']
        # grab the name from each trend
        names = [trend['name'] for trend in trends]
        # put all the names together with a ' ' separating them
        trendsName = '\n'.join(names)
        print trendsName.encode('utf-8')
    except Exception:
        print traceback.format_exc()
    finally:
        print "Finished get_trends_place"

def get_search():
    try:
        for tweet in tweepy.Cursor(api.search,
                                   q="google",
                                   rpp=100,
                                   result_type="recent",
                                   include_entities=True,
                                   lang="en").items():
            print "\n-----------"
            print tweet.created_at
            print tweet.text.encode('utf-8')
    except Exception:
        print traceback.format_exc()
    finally:
        print "Finished get_search"


if __name__ == "__main__":
    try:
		get_user_friends()
		get_weekly_trends()
		get_search()
    except KeyboardInterrupt:
        quit()

