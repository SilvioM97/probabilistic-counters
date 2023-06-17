# 10k random lines from https://www.kaggle.com/kazanova/sentiment140 containing
# the polarity of the tweet ("+", "-")
# the date of the tweet 
# the user that tweeted 
# the text of the tweet 

#import hyperloglog
from stream import *
from stream import dayPart
import heapq as heap
import linear_counter as lc
import space_saving as ss
import punto1 as p1


if __name__ == "__main__":

  print("\n#################################### PUNTO 1 ####################################\n")
  p1.punto1()

  print("\n#################################### PUNTO 2 ####################################\n")
  

  k = 30
  m = 7*k
  space_saving_counter = ss.SpaceSavingCounter(m)
  dizionario = {}

  x = mystream("sample.csv")
  s = x.nextRecord ()
  while s is not None:
    if x.ispositive():
      words = x.tokenizedTweet()
      for word in words:
        space_saving_counter.inc(word)
        if word in dizionario:
          dizionario[word] += 1
        else:
          dizionario[word] = 1
    
    s = x.nextRecord()
  
  # Retrieve the 30 keys with the largest values
  print("Heavy hitters:")
  heavy_hitters = space_saving_counter.heavy_hitters(k)
  print(heavy_hitters)
  
  print("\n#################################### PUNTO 3 ####################################\n")

  m = 100000
  counter = lc.LinearCounter(m)
  counter2 = lc.LinearCounter(m)
  my_set = set()
  my_set2 = set()

  x = mystream("sample.csv")
  s = x.nextRecord ()
  while s is not None:
    if x.ispositive():
      words = x.tokenizedTweet()
      for word in words:
          
          # used to get the exact number of repeated words
          if word in my_set:
             my_set2.add(word)
          else:
             my_set.add(word) 

          # used to approximate the number of repeated words
          if counter.bit(counter.hash(word)):
             counter2.add(word)
          else:
             counter.add(word)

    s = x.nextRecord ()
    
    
  print("Approximated number of words of happy users: ", counter.estimate_cardinality())
  print("Real number of words of happy users: ", len(my_set))

  print("Approximated number of repeated words of happy users: ", counter2.estimate_cardinality())
  print("Real number of repeated words of happy users: ", len(my_set2))





    #################################### PUNTO 4 ####################################

  print("\n#################################### PUNTO 4 ####################################\n")
  
  happy_counter = 0
  sad_counter = 0
  tweets_counter = 0

  x = mystream("sample.csv")
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

  print("\n#################################################################################\n")
