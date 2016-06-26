class Solution:
    # @param {integer[]} nums
    # @return {string}
    def largestNumber(self, nums):
        
        if not nums:
            return ''
        
        nums.sort(cmp=lambda a, b: int(str(b) + str(a)) - int(str(a) + str(b)))
        res = ''.join([str(x) for x in nums])
        
        i = 0
        while i < len(res) - 1:
            if res[i] != '0':
                break
            i += 1
        return res[i:]