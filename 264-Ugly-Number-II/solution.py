import heapq
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        if n <= 1:
            return n
        
        heap = []
        ugly_number = [2, 3, 5]
        heapq.heappush(heap, (1, 0))
        
        cur = 0
        while n != 0:
            cur, level = heapq.heappop(heap)
            
            while level < len(ugly_number):
                heapq.heappush(heap, (ugly_number[level] * cur, level))
                level += 1
            
            n -= 1
        
        return cur
        
        