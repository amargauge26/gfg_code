#User function Template for python3
class Solution:
    def sort(self, s): 
        #code here
        s=sorted(s)
        
        return "".join(s)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        obj = Solution()
        ans = obj.sort(s)
        print(ans)
        print("~")
# } Driver Code Ends