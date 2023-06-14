import math, heapq

class SpaceSavingCounter:
    def __init__(self, m):
        self.size = m                       # size of SpaceSaving table
        self.m = m                          # support
        self.updated_counters = dict()      # counters of elements in the table (used for heap counters lazy update)
        self.heap = []                      # min-heap wrt counters, store all the elements in the table

    def inc(self, x):

        # x is being watched
        if x in self.updated_counters:
            self.updated_counters[x] += 1

        # x is not being watched
        else:
            eps = 0
            # make room for x
            if self.m == 0:
                while True:
                    count, eps, key = self.heap_pop()
                    # assert self.counts[key] >= count
                    if self.updated_counters[key] == count:
                        eps = count
                        del self.updated_counters[key]
                        break
                    else:
                        self.heap_push(self.updated_counters[key], eps, key)
            else:
                self.m = self.m-1
                count = 0
                

            # watch x
            self.updated_counters[x] = count + 1
            self.heap_push(self.updated_counters[x], eps, x)


    def heap_push(self, count, eps, key):
        heapq.heappush(
            self.heap,
            (count, eps, key)
        )

    def heap_pop(self):
        return heapq.heappop(self.heap)
    
    # pop every heap element (count, eps, key) and check counts[key]

    def heavy_hitters(self, k):
        # k is the number of elements to retrieve

        assert(k <= self.size)

        hitters = []

        for i in range(self.size):
            count, eps, key = self.heap_pop()
            count = self.updated_counters[key]        
            hitters.append((count - eps, key))
        
        hitters.sort(reverse=True)
            
        return [hitters[i][1] for i in range(k)]