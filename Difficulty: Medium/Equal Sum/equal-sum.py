#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3
class Solution:

	def equilibrium(self,arr): 
    	# code here
    	n = len(arr)
    	if n>=3:
        	arrr=[0]*n
        	arrl=[0]*n
        	summ=0
        	for i in range(n):
        	    summ+=arr[i]
        	    arrl[i]=summ
        	summ=0
            for i in range(n-1,-1,-1):
        	    summ+=arr[i]
        	    arrr[i]=summ
            for i in range(1,n-1):
                if arrl[i-1]==arrr[i+1]:
                    return 'true'
        return 'false'


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
        print("~")
        t -= 1


# } Driver Code Ends