#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
		maxi = float("-inf")
		
		pre =1
		suf =1
		n = len(arr)
		for i in range(len(arr)):
		  if pre==0:
		        pre=1
		       
		  if suf==0:
		        suf=1
		    
		  pre *=arr[i]
            
          suf*=arr[n-1-i]
            
          maxi = max(maxi,max(suf,pre))
        
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