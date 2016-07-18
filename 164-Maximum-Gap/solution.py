class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return 0
        
        max_num, min_num = max(nums), min(nums)
        m = len(nums)
        
        bucket_size = (max_num - min_num) / m + 1
        bucket_number = (max_num - min_num) / bucket_size + 1
        buckets = [None] * bucket_number
        
        for num in nums:
            
            # get the index of num in buckets
            idx = (num - min_num) / bucket_size
            
            if buckets[idx] is None:
                buckets[idx] = [num, num]
            
            else:
                if buckets[idx][0] > num:
                    buckets[idx][0] = num
                
                elif buckets[idx][1] < num:
                    buckets[idx][1] = num
            
        max_gap = 0
        prev = 0
        for i in xrange(1, bucket_number):
            if buckets[i] is None:
                continue
            
            max_gap = max(max_gap, buckets[i][0] - buckets[prev][1])
            prev = i
            
        return max_gap