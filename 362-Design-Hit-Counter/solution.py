class HitCounter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nodes = []

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        
        if not self.nodes or self.nodes[-1][0] != timestamp:
            self.nodes.append([timestamp, 1])
        else:
            self.nodes[-1][1] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        
        idx = self.binarySearch(timestamp)
        if idx >= len(self.nodes) or self.nodes[idx][0] > timestamp:
            idx -= 1
        
        count = 0
        while idx >= 0 and self.nodes[idx][0] > timestamp - 300:
            count += self.nodes[idx][1]
            idx -= 1
        
        return count
        
    
    def binarySearch(self, target):
        """
        Find the index of target or the supposed place in the nodes
        """
        l, r = 0, len(self.nodes) - 1
        
        while l <= r:
            mid = l + ((r - l) >> 1)
            if self.nodes[mid][0] > target:
                r = mid - 1
                
            else:
                l = mid + 1
        return l


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)