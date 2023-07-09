from utils.stream import *
import structures.linear_counter as lc

def distinct_words():
    m = 100000
    counter = lc.LinearCounter(m)
    counter2 = lc.LinearCounter(m)
    my_set = set()
    my_set2 = set()

    x = mystream("data_sets/sample.csv")
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