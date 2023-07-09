# 10k random lines from https://www.kaggle.com/kazanova/sentiment140 containing
# the polarity of the tweet ("+", "-")
# the date of the tweet 
# the user that tweeted 
# the text of the tweet 

import tasks.countUsers as cu
import tasks.heavyHitters as hh
import tasks.distinctWords as dw
import tasks.happyMessages as hm


if __name__ == "__main__":

  print("\n#################################### TASK 1 ####################################\n")

  cu.count_users()

  print("\n#################################### TASK 2 ####################################\n")

  hh.heavy_hitters()
  
  print("\n#################################### TASK 3 ####################################\n")

  dw.distinct_words()

  print("\n#################################### TASK 4 ####################################\n")
  
  hm.happy_messages()

  print("\n##################################### END ######################################\n")
