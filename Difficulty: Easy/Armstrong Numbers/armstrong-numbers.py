#User function Template for python3
class Solution:
    def armstrongNumber(self, n):
        # Store the original number
        original_n = n
        
        # Extract digits
        d1 = n % 10
        n //= 10
        d2 = n % 10
        n //= 10
        d3 = n % 10
        
        # Calculate the sum of cubes of digits
        sum_of_cubes = d1**3 + d2**3 + d3**3
        
        # Check if the sum of cubes is equal to the original number
        return "true" if sum_of_cubes == original_n else "false"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = input()
        n = int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))

# } Driver Code Ends