################################################################################
################################################################################
####																		
####		                 Automated Bot v1.3								
####		            Created by Mathew Hutchison							
####			  Retweets about x hashtags, prints quotes, reposts images
####							Python 3.5.2								
####																		
################################################################################
################################################################################

import tweepy
from time import sleep
from config import *
from multiprocessing import Process
import time
import random
import os
import sys

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)
my_file = open('tweets.txt', 'r')
file_lines = my_file.readlines()
my_file.close()

# Search tweets relating to #Unity4J via Twitter
# Retweets a random tweet every 30 minutes

def Process1():
	for tweet in tweepy.Cursor(api.search, q='#HASHTAG').items() :
		try:
			# Add \n escape character to print() to organize tweets
			print('\nTweet by: @' + tweet.user.screen_name)
			print('Retweeted about #HASHTAG')
			
			# Retweet random tweet
			tweet.retweet()

			sleep(1800)

		except tweepy.TweepError as e:
			print(e.reason)

		except StopIteration:
			break

# Tweet quotes from a file
# Give motivation and inspiration
# Posts every 30 minutes
			
def Process2():
    for line in file_lines:
        try:
             print('Current quote:\n' + line)
             if line != '\n':
                 api.update_status(line)
                 sleep(1800)
             else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
            sleep(2)
			
			
# Tweet images from a local folder
# Inspirational ideas just to test it
			
def Process3():
    imagePath = r'INSERT DIRECTORY HERE'
    randQuote = os.path.join(imagePath, random.choice(os.listdir(imagePath)))
    status = 'TWEET TEXT WITH IMAGE'
    api.update_with_media(randQuote, status)
    sleep(2)


# Creating a process to run multiple functions
# Currently running two tweets and a quote finally, can add more if desired
# Added a wait process when starting the script, the second and third process start 30 to 60 seconds after the first one
# This makes it so the script doesn't spam Twitter each time the bot is started
			
if __name__=='__main__':
	p1 = Process(target = Process1)
	p1.start()
	print('\nTweets started about Process1')
	time.sleep(30)
	p2 = Process(target = Process2)
	p2.start()
	print('\nTweets started to print from file')
	time.sleep(30)
	p3 = Process(target = Process3)
	p3.start()
	print('\nUploading image')
	time.sleep(30)
