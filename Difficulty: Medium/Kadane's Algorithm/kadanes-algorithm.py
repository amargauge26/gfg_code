class Solution:
    def maxSubArraySum(self, arr):
        # Your code here
        maxi =float("-inf")
        curr_sum=0
        
        i =0
        n = len(arr)
        while i<n:
            curr_sum+=arr[i]
            
            if curr_sum>maxi:
                maxi=curr_sum
            if curr_sum<0:
                curr_sum=0
            
            i+=1
        
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends