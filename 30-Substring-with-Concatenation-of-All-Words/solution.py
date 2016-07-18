class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        
        
        if not s or not words:
            return [0]
        
        word_length = len(words[0])
        total_length = len(words) * len(words[0])
        
        marks = {}
        for word in words:
            marks[word] = marks.get(word, 0) + 1
        
        res = []
        for i in xrange(len(s) - total_length + 1):
            if self.dfs(s, marks, i, word_length):
                res.append(i)
        
        return res
        
    
    def dfs(self, s, marks, index, word_length):
        
        if not marks:
            return True
            
        cur_word = s[index : index + word_length]
        if cur_word not in marks:   # the cur_word has been used or never in words
            return False
            
        marks[cur_word] -= 1    
        if marks[cur_word] == 0:
            del marks[cur_word]
        
        flag = self.dfs(s, marks, index + word_length, word_length)
        marks[cur_word] = marks.get(cur_word, 0) + 1
        
        return flag
        