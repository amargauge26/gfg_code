#User function Template for python3

class Solution:

    def findMinDiff(self, arr,M):

        # code here
        n = len(arr)
        
        if M==0 or n ==0 :
            return 0
        
        if M >n:
            return -1
        
        arr.sort()
        min_dif = arr[-1]-arr[0]
        
        
        for i in range(n-M+1):
            min_dif = min(min_dif,arr[i+M-1]-arr[i])
        
        
        return min_dif


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):

        A = [int(x) for x in input().split()]
        M = int(input())

        solObj = Solution()

        print(solObj.findMinDiff(A, M))
        print("~")

# } Driver Code Ends