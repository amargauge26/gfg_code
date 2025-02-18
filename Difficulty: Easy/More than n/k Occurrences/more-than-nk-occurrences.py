#User function Template for python3

from collections import Counter
class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr, k):
        #Your code here
        l = Counter(arr)
        c=0
        for kk,v in l.items():
            if v>len(arr)//k:
                c+=1
        
        
        return c
        
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.countOccurence(A, D)
        print(ans)
        print("~")
# } Driver Code Ends