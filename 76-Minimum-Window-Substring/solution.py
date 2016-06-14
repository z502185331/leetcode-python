class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        
        if not s or not t:
            return ''
        
        need_to_find = {}
        has_found = {}
        m, n = len(s), len(t)
        count = n
        
        # init two dict
        for c in t:
            need_to_find[c] = need_to_find.get(c, 0) + 1
            has_found[c] = has_found.get(c, 0)
        
        l, r = 0, 0
        min_str = s + ' '
        while r < m:
            c = s[r]
            if c not in need_to_find:
                r += 1
                continue
            
            if has_found[c] < need_to_find[c]:  # if find enough c, count doesn't decrease
                count -= 1
            has_found[c] += 1
            
            if count == 0:
                while True:
                    tmp = s[l]
                    if tmp not in need_to_find:
                        l += 1
                        continue
                    
                    if has_found[tmp] > need_to_find[tmp]:
                        has_found[tmp] -= 1
                    else:
                        cur_str = s[l : r + 1]
                        min_str = cur_str if len(cur_str) < len(min_str) else min_str
                        break
                    
                    l += 1
            r += 1
            
        return min_str if min_str != s + ' ' else ''
                