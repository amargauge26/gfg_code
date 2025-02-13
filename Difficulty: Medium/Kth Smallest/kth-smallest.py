#User function Template for python3


class Solution:

    def kthSmallest(self, arr,k):
        arr_max=max(arr)
        max_el = [0]*(arr_max + 1)
        for i in range(len(arr)):
            max_el[arr[i]]+=1
        
        
        count=0
        
        for i in range(arr_max+1):
            if  max_el[i]!=0:
                count+=max_el[i]
                
                if count==k:
                    return i
        
        return -1
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends