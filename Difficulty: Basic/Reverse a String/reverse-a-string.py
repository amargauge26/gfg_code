#User function Template for python3

class Solution:
     def reverseString(self, s: str) -> str:
        # code here
        arr_list=list(s)
        arr_list.reverse()
        return "".join(arr_list)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while (t > 0):
        s = input()
        ob = Solution()
        print(ob.reverseString(s))
        t = t - 1

        print("~")

# } Driver Code Ends