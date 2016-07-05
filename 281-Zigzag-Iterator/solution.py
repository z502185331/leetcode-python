class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.nums = []
        i = 0
        m, n = len(v1), len(v2)
        while i < max(m, n):
            if i < m:
                self.nums.append(v1[i])
            if i < n:
                self.nums.append(v2[i])
            i += 1
        
        self.cur = -1

    def next(self):
        """
        :rtype: int
        """
        num = self.nums[self.cur + 1]
        self.cur += 1
        return num

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur + 1 != len(self.nums)
        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())