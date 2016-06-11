class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        if not nums:
            return []
        
        # a max_queue stores the max number in the window, queue[0] is the maximum number
        queue = []
        res = []
        for i in xrange(len(nums)):
            if not queue or nums[i] <= queue[-1]:
                queue.append(nums[i])
            else:
                while queue and nums[i] > queue[-1]:
                    queue.pop()
                queue.append(nums[i])
            if i >= k - 1:
                if i > k - 1:   #remove one if that one is the max number in queue
                    if nums[i - k] == queue[0]:
                        queue.pop(0)
                
                res.append(queue[0])
        
        return res
            
        