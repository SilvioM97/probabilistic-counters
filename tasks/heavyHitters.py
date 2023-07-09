import structures.space_saving as ss
from utils.stream import *

def heavy_hitters():
    k = 30
    m = 7*k
    space_saving_counter = ss.SpaceSavingCounter(m)
    dizionario = {}

    x = mystream("data_sets/sample.csv")
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