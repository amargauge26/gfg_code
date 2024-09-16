#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:

	def equilibrium(self,arr): 
    	# code here
    	l_s=0
    	t_s=sum(arr)
    	
    	for i in range(len(arr)):
    	    r_s=t_s - l_s - arr[i]
    	    
    	    if r_s==l_s:
    	        return "true"
    	   
    	    l_s+=arr[i]
    	
        return "false"

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.equilibrium(arr)
        print(res)
        t -= 1


# } Driver Code Ends