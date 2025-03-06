#User function Template for python3
class Solution:
    def sortArr(self, arr): 
        #code here
        arr.sort()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        obj = Solution()
        obj.sortArr(arr)
        for i in arr:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends