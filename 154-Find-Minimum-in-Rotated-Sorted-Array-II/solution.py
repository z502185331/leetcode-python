class Solution(object):
    def findMin(self, num):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        min = num[0]
        start, end = 0, len(num) - 1
        while start<end:
            mid = (start+end)/2
            if num[mid]>num[end]:
                start = mid+1
            elif num[mid]<num[end]:
                end = mid
            else:
                end = end - 1
        return num[start]