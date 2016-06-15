class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        left, right = 0, len(nums)-1

        while left<=right:
            mid = left+(right-left)/2
            lv, mv, rv = nums[left], nums[mid], nums[right]

            if lv<target<mv or mv<lv<target or target<mv<rv:
                right = mid-1
            elif lv<mv<target or target<rv<mv or mv<target<rv:
                left = mid+1
            else:
                break

        return left if target==lv else mid if target==mv else right if target==rv else -1
        
    #     if not nums:
    #         return -1
        
    #     m = len(nums)
    #     l, r = 0, m - 1
        
    #     if nums[0] < nums[-1]:
    #         return self.find(nums, 0, m - 1, target)
        
    #     while l < r:
    #         mid = l + (r - l) / 2
    #         if nums[mid] == target:
    #             return mid
                
    #         if nums[mid] > nums[0]:
    #             if target < nums[mid] and target >= nums[l]:
    #                 return self.find(nums, l, mid - 1, target)
    #             else:
    #                 l = mid + 1
            
    #         elif nums[mid] < nums[0]:
    #             if target > nums[mid] and target <= nums[r]:
    #                 return self.find(nums, mid + 1, r, target)
    #             else:
    #                 r = mid - 1
        
    #     return l if nums[l] == target else -1
    
    # '''
    # A method to find the target in a sorted range
    # '''
    # def find(self, nums, l, r, target):
        
    #     while l <= r:
    #         mid = l + (r - l) / 2
    #         if nums[mid] > target:
    #             r = mid - 1
    #         elif nums[mid] < target:
    #             l = mid + 1
    #         else:
    #             return mid
        
    #     return -1
        