#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		n = len(arr)
		pre =1
		suf =1
		maxi = float("-inf")
		for i in range(n):
		    if pre ==0:
		        pre=1
		    if suf ==0:
		        suf=1
		    pre*=arr[i]
		    suf*=arr[n-i-1]
		    maxi = max(maxi,max(pre,suf))
	    return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr)
        print(ans)
        tc -= 1

# } Driver Code Ends