# 10k random lines from https://www.kaggle.com/kazanova/sentiment140 containing
# the polarity of the tweet ("+", "-")
# the date of the tweet 
# the user that tweeted 
# the text of the tweet 

#import hyperloglog
from stream import *
from stream import dayPart
import heapq
import linear_counter as lc
import numpy as np

if __name__ == "__main__":
  m = 12007
  positive_counter = lc.LinearCounter(m)
  negative_counter = lc.LinearCounter(m)
  morning_counter = lc.LinearCounter(m)
  afternoon_counter = lc.LinearCounter(m)
  evening_counter = lc.LinearCounter(m)
  night_counter = lc.LinearCounter(m)

  tweet_counter = 0
  pos_counter = 0
  neg_counter = 0
  pos_morning_counter = 0
  pos_afternoon_counter = 0
  pos_evening_counter = 0
  pos_night_counter = 0
  neg_morning_counter = 0
  neg_afternoon_counter = 0
  neg_evening_counter = 0
  neg_night_counter = 0
  
  x = mystream("sample.csv")
  s = x.nextRecord ()
  while s is not None:
    tweet_counter += 1
    
    if(x.ispositive()):
      positive_counter.add(s[2])
      pos_counter += 1
    else:
      negative_counter.add(s[2])
      neg_counter += 1


    match x.timeBin():
      case dayPart.MORNING:
        morning_counter.add(s[2])
        if x.ispositive():
          pos_morning_counter+= 1
        else:
          neg_morning_counter+= 1
      case dayPart.AFTERNOON:
        afternoon_counter.add(s[2])
        if x.ispositive():
          pos_afternoon_counter+= 1
        else:
          neg_afternoon_counter+= 1
      case dayPart.EVENING:
        evening_counter.add(s[2])
        if x.ispositive():
          pos_evening_counter += 1
        else:
          neg_evening_counter += 1
      case dayPart.NIGHT:
        night_counter.add(s[2])
        if x.ispositive():
          pos_night_counter += 1
        else:
          neg_night_counter += 1
    
    s = x.nextRecord ()

  positive_morning = []
  positive_afternoon = []
  positive_evening = []
  positive_night = []

  negative_morning = []
  negative_afternoon = []
  negative_evening = []
  negative_night = []
  
  for index in range(m):
    positive_morning.append(positive_counter.mask[index] and morning_counter.mask[index])
    positive_afternoon.append(positive_counter.mask[index] and afternoon_counter.mask[index])
    positive_evening.append(positive_counter.mask[index] and evening_counter.mask[index])
    positive_night.append(positive_counter.mask[index] and night_counter.mask[index])

    negative_morning.append(negative_counter.mask[index] and morning_counter.mask[index])
    negative_afternoon.append(negative_counter.mask[index] and afternoon_counter.mask[index])
    negative_evening.append(negative_counter.mask[index] and evening_counter.mask[index])
    negative_night.append(negative_counter.mask[index] and night_counter.mask[index])

percentage_pm = positive_morning.count(True)/tweet_counter
percentage_pa = positive_afternoon.count(True)/tweet_counter
percentage_pe = positive_evening.count(True)/tweet_counter
percentage_pn = positive_night.count(True)/tweet_counter

percentage_nm = negative_morning.count(True)/tweet_counter
percentage_na = negative_afternoon.count(True)/tweet_counter
percentage_ne = negative_evening.count(True)/tweet_counter
percentage_nn = negative_night.count(True)/tweet_counter

print("Percentage of positive tweets in the morning: " + str(round(percentage_pm * 100)) + str('%'))
print("Percentage of positive tweets in the afternoon: " + str(round(percentage_pa * 100)) + str('%'))
print("Percentage of positive tweets in the evening: " + str( round(percentage_pe * 100)) + str('%'))
print("Percentage of positive tweets in the night: " + str(round(percentage_pn * 100)) + str('%'))

print("\n")

print("Percentage of negative tweets in the morning: " + str(round(percentage_nm * 100)) + str('%'))
print("Percentage of negative tweets in the afternoon: " + str(round( percentage_na * 100)) + str('%'))
print("Percentage of negative tweets in the evening: " + str(round(percentage_ne * 100)) + str('%'))
print("Percentage of negative tweets in the night: " + str(round(percentage_nn * 100)) + str('%'))

print("\n")


print("Exact and estimated count for morning: " + str(pos_morning_counter + neg_morning_counter) + ',' + str(morning_counter.mask.count(True)))
print("Exact and estimated count for afternoon: " + str(pos_afternoon_counter + neg_afternoon_counter) + ',' + str(afternoon_counter.mask.count(True)))
print("Exact and estimated count for evening: " + str(pos_evening_counter + neg_evening_counter) + ',' + str(evening_counter.mask.count(True)))
print("Exact and estimated count for night: " + str(pos_night_counter + neg_night_counter) + ',' + str(night_counter.mask.count(True)))
print("Exact and estimated count for positive: " + str(pos_counter) + ',' + str(positive_counter.mask.count(True)))
print("Exact and estimated count for negative: " + str(neg_counter) + ',' + str(negative_counter.mask.count(True)))

print("\n")

print("Total tweets: " + str(tweet_counter))


tot_percentage = (percentage_pm + percentage_pa + percentage_pe + percentage_pn + percentage_nm + percentage_na + percentage_ne + percentage_nn)
print("Total percentage: ", round(tot_percentage * 100), end="")
print("%")
  

#   positive_counter.print_mask()
#   morning_counter.print_mask()
#   print(positive_morning)
#   print('\n')
  