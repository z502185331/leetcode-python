class Solution(object):
    def nextPermutation(self, num):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        if num is None or not num:
            return
        
        for i in range(1, len(num)):
            i = len(num) - i - 1 # traverse the num from back
            if num[i + 1] > num[i]:
                for j in reversed(range(i + 1, len(num))): 
                    # find the first digit that larger than num[1 - 1]
                    if num[j] > num[i]:
                        break
                num[i], num[j] = num[j], num[i]
                num[i + 1 :] = num[i + 1 :][::-1]
                return
        
        num.reverse()
        
        return