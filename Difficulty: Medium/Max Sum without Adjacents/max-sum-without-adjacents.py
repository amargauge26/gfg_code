#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr):
		# code here
		n = len(arr)
		dp = [-1]*n
        
        dp[0]=arr[0]
        dp[1]= max(arr[0],arr[1])
        
        
        
        for i in range(2,n):
            dp[i]=max(dp[i-2]+arr[i],dp[i-1])
           
        return dp[n-1]


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.findMaxSum(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends