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
            
        return self.sol_heap(nums1, nums2, k)
    
    def sol_sort(self, nums1, nums2, k):
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
        
        for i in xrange(len(nums1)):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))
        
        res = []
        while heap and k > 0:
            s, i, j = heapq.heappop(heap)
            if j < len(nums2) - 1:
                heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
            res.append([nums1[i], nums2[j]])
            k -= 1
        
        return res