import linear_counter as lc
from stream import *
from stream import dayPart

def punto1():
    m = 100000

    users_counter = lc.LinearCounter(m)
    positive_counter = lc.LinearCounter(m)
    negative_counter = lc.LinearCounter(m)
    morning_counter = lc.LinearCounter(m)
    afternoon_counter = lc.LinearCounter(m)
    evening_counter = lc.LinearCounter(m)
    night_counter = lc.LinearCounter(m)
    users = set()

    tweet_counter = 0
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
        
        users_counter.add(s[2])
        users.add(s[2])

        match x.timeBin():
            case dayPart.MORNING:
                morning_counter.add(s[2])
            case dayPart.AFTERNOON:
                afternoon_counter.add(s[2])
            case dayPart.EVENING:
                evening_counter.add(s[2])
            case dayPart.NIGHT:
                night_counter.add(s[2])

        if x.ispositive():
            positive_counter.add(s[2])
        else:
            negative_counter.add(s[2])

        s = x.nextRecord ()
    
    tweet_counter = users_counter.estimate_cardinality()
    

    for index in range(m):
        pos_morning_counter += int(positive_counter.mask[index] and morning_counter.mask[index])
        pos_afternoon_counter += int(positive_counter.mask[index] and afternoon_counter.mask[index])
        pos_evening_counter += int(positive_counter.mask[index] and evening_counter.mask[index])
        pos_night_counter += int(positive_counter.mask[index] and night_counter.mask[index])

        neg_morning_counter += int(negative_counter.mask[index] and morning_counter.mask[index])
        neg_afternoon_counter += int(negative_counter.mask[index] and afternoon_counter.mask[index])
        neg_evening_counter += int(negative_counter.mask[index] and evening_counter.mask[index])
        neg_night_counter += int(negative_counter.mask[index] and night_counter.mask[index])

    print("Estimated percentage of positive tweets in the morning, afternoon, evening, night: [", end = '')
    print(str(round((pos_morning_counter / tweet_counter) * 100)) + str('%, '), end = '')
    print(str(round((pos_afternoon_counter/tweet_counter) * 100)) + str('%, '), end = '')
    print(str(round((pos_evening_counter/tweet_counter) * 100)) + str('%, '), end = '')
    print(str(round((pos_night_counter/tweet_counter) * 100)) + str('%'), end = '')
    print("]")

    print("Estimated total percentage of users: [", end = '')
    print(str(round((neg_morning_counter / tweet_counter) * 100)) + str('%, '), end = '')
    print(str(round( (neg_afternoon_counter / tweet_counter) * 100)) + str('%, '), end = '')
    print(str(round((neg_evening_counter / tweet_counter) * 100)) + str('%, '), end = '')
    print(str(round((neg_night_counter / tweet_counter) * 100)) + str('%'), end = '')
    print("]")


    tot_counter = pos_morning_counter + pos_afternoon_counter + pos_evening_counter + pos_night_counter + neg_morning_counter + neg_afternoon_counter + neg_evening_counter + neg_night_counter
    
    print("Total percentage: ", round((tot_counter / tweet_counter) * 100), end="")
    print("%")