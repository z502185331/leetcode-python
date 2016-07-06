class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.nums = []
        self.sums = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sums += val
        self.nums.append(val)
        
        if len(self.nums) > self.size:
            num = self.nums.pop(0)
            self.sums -= num
        
        return self.sums / float(len(self.nums))
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)