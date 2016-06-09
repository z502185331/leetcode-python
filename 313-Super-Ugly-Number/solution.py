import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        
        # if not primes:
        #     return 0
        
        # if n == 1:
        #     return 1
        
        # heap = []
        # for i in xrange(len(primes)):
        #     heapq.heappush(heap, (primes[i], i))
        
        # num = 0
        # while n > 1:
        #     num, level = heapq.heappop(heap)
            
        #     for i in xrange(level, len(primes)):
        #         heapq.heappush(heap, (num * primes[i], i))
        #     n -= 1
        
        # return num
        ug,ct, max_n=[0,1],1,float('inf')
        pr=[1 for i in range(len(primes))]
        while ct<=n:
            x=max_n
            for i in range(len(primes)):
                while primes[i]*ug[pr[i]]<=ug[-1]:
                    pr[i]+=1
                x=min(x,primes[i]*ug[pr[i]])
            ug.append(x)
            ct+=1
        return ug[n]
            
        