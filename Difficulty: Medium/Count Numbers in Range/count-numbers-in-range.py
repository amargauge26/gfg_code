#User function Template for python3
import math
class Solution:
    def count3DivNums(self, L, R):
        # code here 
        maxl = int(math.sqrt(R)+1)
        is_prime = [True]*(maxl+1)
        is_prime[0]=False
        is_prime[1]=False
        
        for i in range(2,int(math.sqrt(maxl) +1)):
            if is_prime[i]:
                for j in range(i*i,maxl+1,i):
                    is_prime[j]=False
        
        count=0
        
        for i in range(2,maxl+1):
            if is_prime[i]:
                s=i*i
                if L<=s<=R:
                    count+=1
        
        return count


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