class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.nums = vec2d
        self.row = -1
        self.col = 0
        self.nextNum = None

    def next(self):
        """
        :rtype: int
        """
        res, self.nextNum = self.nextNum, None
        return res
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.nextNum is not None:
            return True
        
        if self.row >= 0 and self.col < len(self.nums[self.row]) - 1: # continue iterate current row
            self.col += 1

        else:   # finish current row and find out next non-empty row
            self.row += 1
            while self.row < len(self.nums) and not self.nums[self.row]:
                self.row += 1
            
            if self.row == len(self.nums):
                return False
            
            self.col = 0
            
        self.nextNum = self.nums[self.row][self.col]
        return True
        
        
# Your Vector2D object will be instantiated and called as such:
# i, v = Vector2D(vec2d), []
# while i.hasNext(): v.append(i.next())