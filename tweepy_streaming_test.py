# -*- coding: utf-8 -*-
#import tweepy, sys
import traceback
import sys
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from django.utils.encoding import smart_str, smart_unicode

consumer_key 	= 'DcUn75oC8cZm3H2vLolPEwJpm'
consumer_secret = 'Q8C0wrCvOt2kafqgDM0x7XD84YXDvoHpdXUgKVJBgwa6pG8vZ2'
access_token 		= '1511458178-mAAG0IXulkVi6Nod18w3G78gJv4JEmzbXjpc76J'
access_token_secret = 'epu9vynJ8vCCOYeK16S1OL0e8G8Ko2zM3pIMMYeP0fTEd'

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """

    def on_status(self, status):
        # We'll simply print some values in a tab-delimited format
        # suitable for capturing to a flat file but you could opt 
        # store them elsewhere, retweet select statuses, etc.

        try:
            str = u"\n\n*******\n%s\n%s\n%s\n%s" % (status.text, 
                                      status.author.screen_name, 
                                      status.created_at, 
                                      status.source,)
            print smart_str(str)
        except Exception, e:
            print >> sys.stderr, 'Encountered Exception:', e
            pass
	
	
    #def on_data(self, data):
    #    print data
    #    return True

    def on_error(self, status):
        print status

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True # Don't kill the stream

if __name__ == '__main__':
    try:
        auth = OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)

        stream = Stream(auth, StdOutListener(), timeout=60)
        stream.filter(track=['cricket'])
    except KeyboardInterrupt:
        quit()
