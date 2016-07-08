class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        
        if not envelopes:
            return 0
        
        envelopes.sort(key = lambda x : (x[0], -x[1]))
        m = len(envelopes)
        dp = [1] * m
        res = 1
        
        sequences = []
        
        for i, env in enumerate(envelopes):
            idx = self.findInsertPlace(envelopes, sequences, env)
            if idx >= len(sequences):
                sequences.append(i)
            else:
                sequences[idx] = i
        return len(sequences)


    def findInsertPlace(self, envelopes, sequences, k):
        l, r = 0, len(sequences) - 1
        while l <= r:
            mid = l + ((r - l) >> 1)
            if envelopes[sequences[mid]][1] >= k[1]:
                r = mid - 1
            else:
                l = mid + 1
            
        return l
            
            
            