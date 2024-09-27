#User function Template for python3

import math

class Solution:
    def count3DivNums(self, l, r):
        # Helper function to find all primes up to sqrt(r) using Sieve of Eratosthenes
        def sieve(limit):
            primes = []
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False  # 0 and 1 are not primes
            for num in range(2, limit + 1):
                if is_prime[num]:
                    primes.append(num)
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False
            return primes
        
        # Find primes up to sqrt(r)
        sqrt_r = int(math.sqrt(r))
        primes = sieve(sqrt_r)
        
        count = 0
        
        # For each prime, check if its square lies within [l, r]
        for prime in primes:
            prime_square = prime * prime
            if l <= prime_square <= r:
                count += 1
        
        return count

        return c
                    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        L,R=map(int,input().split())
        
        ob = Solution()
        print(ob.count3DivNums(L,R))
# } Driver Code Ends