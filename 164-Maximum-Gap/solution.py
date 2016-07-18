class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(nums) < 2:
            return 0
        
        m = len(nums)
        
        # bucket sort
        max_num = max(nums)
        min_num = min(nums)
        
        # the number of bucket
        # each bucket contains the local_max and local_min
        bucket_size = (max_num - min_num) / m + 1
        bucket_len = (max_num - min_num) / bucket_size + 1
        buckets = [None] * bucket_len
        
        for num in nums:
            
            # get the pos of num in buckets
            i = (num - min_num) / bucket_size
            if buckets[i] is None:  # bucket is empty
                buckets[i] = []
                buckets[i].append(num)
                buckets[i].append(num)
            else:
                if num < buckets[i][0]:
                    buckets[i][0] = num
                elif num > buckets[i][1]:
                    buckets[i][1] = num
        
        # get the max gap
        max_gap = 0
        prev = 0
        for i in xrange(1, bucket_len):
            if buckets[i] is None:
                continue
            max_gap = max(max_gap, buckets[i][0] - buckets[prev][1])
            prev = i
        
        return max_gap
        