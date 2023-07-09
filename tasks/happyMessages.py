from utils.stream import *

def happy_messages():
    happy_counter = 0
    sad_counter = 0
    tweets_counter = 0

    x = mystream("data_sets/sample.csv")
    s = x.nextRecord ()

    while s is not None:
        tweets_counter += 1
        words = x.tokenizedTweet()
        tweet_len = 0
        # count number of characters of the tweet
        for word in words:
            tweet_len += len(word) + 1 # +1 for the space between words
        
        if x.ispositive():
            happy_counter += (tweet_len - 1) / 280 # we are removing the final space and renormalizing wrt max tweet length
        else:
            sad_counter += (tweet_len - 1) / 280  
        
        s = x.nextRecord ()

    print("Average length of happy users' tweets:", round(happy_counter * 280/tweets_counter))
    print("Average length of unhappy users' tweets:", round(sad_counter * 280/tweets_counter))