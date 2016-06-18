class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        return self.quicksort(nums, 0, len(nums) - 1, k)
        
    
    def quicksort(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        index = self.partition(nums, start, end)

        # print nums, index, start, end, k
        if index == end + 1 - k:
            return nums[index]
        
        elif index < end + 1 - k:
            return self.quicksort(nums, index + 1, end, k)
            
        else:
            return self.quicksort(nums, start, index - 1, k - (end + 1 - index))
    
    '''
    A method to partition the nums and return the index of partition
    '''
    def partition(self, nums, start, end):
        l, r = start, end
        pivot = nums[l]
        
        while l < r:
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
        
        nums[l] = pivot
        return l