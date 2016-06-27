class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        
        if num == 0:
            return 'Zero'
        
        self.dict = {
            1 : 'One', 2 : 'Two', 3 : 'Three', 4 : 'Four', 5 : 'Five', 6 : 'Six', 7 : 'Seven', 8 : 'Eight', 9 : 'Nine',
            10 : 'Ten', 11 : 'Eleven', 12 : 'Twelve', 13 : 'Thirteen', 14 : 'Fourteen', 15 : 'Fifteen', 16 : 'Sixteen', 
            17 : 'Seventeen', 18 : 'Eighteen', 19 : 'Nineteen', 20 : 'Twenty', 30 : 'Thirty', 40 : 'Forty', 50 : 'Fifty', 
            60 : 'Sixty', 70 : 'Seventy', 80 : 'Eighty', 90 : 'Ninety'
        }
        
        res = ''
        if num >= 1000000000:
            res += self.translate(num / 1000000000) + ' Billion '
            num %= 1000000000
        
        if num >= 1000000:
            res += self.translate(num / 1000000) + ' Million '
            num %= 1000000
        
        if num >= 1000:
            res += self.translate(num / 1000) + ' Thousand '
            num %= 1000
        
        res += self.translate(num)
        return res.strip()
        
        
    '''
    A method to translate the num to English, the num should less than 1000
    '''
    def translate(self, num):
        
        res = []
        if num >= 100:
            res.append(self.dict[num / 100])
            res.append('Hundred')
            num %= 100
        
        if num >= 20:
            res.append(self.dict[num / 10 * 10])
            num %= 10
        
        if num < 20 and num > 0:
            res.append(self.dict[num])
        
        return ' '.join(res) 
        
        