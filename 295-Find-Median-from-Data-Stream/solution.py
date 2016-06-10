import heapq
class MedianFinder:
    def __init__(self):
        '''
        The size of max_heap should be equal or more than size of min_heap by one
        When len(max_heap) == len(min_heap), median = (max_heap[0] + min_heap[0]) / 2
        When len(max_heap) == len(min_heap) + 1, median = max_heap[0]
        '''
        self.max_heap = []  
        self.min_heap = []
        

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)     # use negative number to represent max heap
        else:
            heapq.heappush(self.min_heap, num)
        
        # balance the length of two heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if len(self.max_heap) == len(self.min_heap) + 1:
            return -self.max_heap[0]
        elif len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / float(2)

# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()