#User function Template for python3

class Solution:
    def isStrong(self, N):
        # code here 
        n =N
        sum=0
        while N>0:
            digit = N%10
            sum += self.fac(digit)
            N//=10
        
        
        if sum==n:
            return 1
        
        return 0
    
    
    def fac(self,num):
        if num==1 or num ==0:
            return 1
        
        return self.fac(num-1)*num


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        
        ob = Solution()
        print(ob.isStrong(N))
# } Driver Code Ends