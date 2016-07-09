import heapq
class Solution(object):
    def rearrangeString(self, str, k):
        """
        :type str: str
        :type k: int
        :rtype: str
        """
        
        if not str:
            return ''
        
        m = len(str)
        
        # count the characters
        counts = {}
        for c in str:
            counts[c] = counts.get(c, 0) + 1
        
        # put the (count, c) into max heap
        heap = []
        for key, val in counts.items():
            heapq.heappush(heap, (-val, key))
        
        # fill the characters in res
        res = []
        queue = []
        while heap:
            count, c = heapq.heappop(heap)  # pop the character with most appearances
            count = -count - 1

            res.append(c)
            queue.append((count, c))
            if len(queue) < k:
                continue
            else:
                next_count, next_c = queue.pop(0)
                if next_count != 0:
                    heapq.heappush(heap, (-next_count, next_c))
        
        return ''.join(res) if len(res) == m else ''

            