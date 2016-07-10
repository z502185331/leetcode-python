import heapq

class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        if not nums1 or not nums2:
            return []
        
        nums = []
        for num1 in nums1:
            for num2 in nums2:
                nums.append([num1, num2])
        
        nums.sort(cmp = lambda a, b : (a[0] + a[1]) - (b[0] + b[1]))
        
        if len(nums) <= k:
            return nums
        else:
            return nums[: k]
        
        
    def sol_heap(self, nums1, nums2, k):
        heap = []
        
        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(heap, (num1 + num2, [num1, num2]))
        
        res = []
        while heap and k > 0:
            res.append(heapq.heappop(heap)[1])
            k -= 1
        
        return res