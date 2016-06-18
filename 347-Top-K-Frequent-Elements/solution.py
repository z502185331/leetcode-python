import heapq

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        heap = []
        for key, val in count.items():
            heapq.heappush(heap, (-val, key))
        
        res = []
        for i in xrange(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
            
                
                