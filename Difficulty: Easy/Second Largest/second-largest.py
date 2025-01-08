#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        if len(arr)<=1:
            return -1
        arr.sort()
        n = len(arr)
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                return arr[i]
                break
        
        return -1


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends