################################################################################
################################################################################
####																		
####		                    Tweet Deleter V1							
####		            Created by Mathew Hutchison							
####							Deletes tweets								
####							Python 3.5.2								
####																		
################################################################################
################################################################################

import tweepy
from config import *

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def tweet_delete(api):
        for status in tweepy.Cursor(api.user_timeline).items():
            try:
                api.destroy_status(status.id)
                print("Deleted tweet ID:", status.id)
            except:
                print("Failed to delete tweet:", status.id)

if __name__ =="__main__":
    tweet_delete(api)
    print("Tweets successfully deleted")
