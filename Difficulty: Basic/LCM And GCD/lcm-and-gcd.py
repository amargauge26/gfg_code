#User function Template for python3

class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        arr= [0]*2
        g = math.gcd(A,B)
        l = (A*B)//g
        
        
        arr[0],arr[1]=l,g
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends