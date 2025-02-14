class Solution:
    def mergeArrays(self, a, b):
        # code here
        na=len(a)
        nb = len(b)
        mm=a+b
        mm.sort()
        
        a[:]= mm[:na]
        b[:] =mm[na:]
        
        return a,b
        


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

        print("~")

# } Driver Code Ends