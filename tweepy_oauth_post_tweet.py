import tweepy, sys
import traceback

#How to use
#python tweepy_oauth_tweet.py "API Test Message"

#For posting tweets using the API (need WRITE permission)
#For WRITE permisssions, you need to register your mobile 
consumer_key 	= 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
consumer_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token 	= 'XXXXXXXXXXXXXXXXXXXXXXXXXX'
access_token_secret = 'XXXXXXXXXXXXXXXXXXXXXXXXXX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print "Success logged in as " + api.me().name + "."

try:
 if len(sys.argv[1]) <= 140:
  api.update_status(sys.argv[1])
  print "Successfully tweeted: " + "'" + sys.argv[1] + "'!"
 else:
  raise IOError
except Exception:
 print traceback.format_exc()
finally:
 print "Shutting down script..."