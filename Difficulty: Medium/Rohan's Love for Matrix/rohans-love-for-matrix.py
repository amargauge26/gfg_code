#User function Template for python3
class Solution:
    def firstElement(self, n):
        MOD = 1000000007  # Modulo constant

        # Handle base cases directly
        if n == 1 or n == 2:
            return 1
        
        # Initialize variables for previous Fibonacci values
        prev = 1      # F(n-2)
        prev1 = 1    # F(n-1)

        # Calculate Fibonacci iteratively
        for i in range(3, n + 1):
            curr = (prev + prev1) % MOD  # F(n) = F(n-1) + F(n-2)
            prev = prev1                 # Update F(n-2) to F(n-1)
            prev1 = curr                 # Update F(n-1) to F(n)
        
        return curr  # Return F(n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        
        ob = Solution()
        print(ob.firstElement(n))
# } Driver Code Ends