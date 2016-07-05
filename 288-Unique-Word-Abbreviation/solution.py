class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.count = {}
        for word in dictionary:
            abbr = word
            if len(abbr) > 2:
                abbr = word[0] + str(len(word) - 2) + word[-1]
            
            if abbr not in self.count:
                self.count[abbr] = word
            elif word != self.count[abbr]:
                self.count[abbr] = None
        

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        abbr = word
        if len(abbr) > 2:
            abbr = word[0] + str(len(word) - 2) + word[-1]
        
        return abbr not in self.count or word == self.count[abbr]


# Your ValidWordAbbr object will be instantiated and called as such:
# vwa = ValidWordAbbr(dictionary)
# vwa.isUnique("word")
# vwa.isUnique("anotherWord")