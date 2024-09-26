class Solution:
    def convertFive(self, n):
        # Convert the integer to a string
        s = str(n)
        
        # Replace all occurrences of '0' with '5'
        s = s.replace("0", "5")
        
        # Convert the modified string back to an integer and return it
        return int(s)

#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n=int(input())
        print(Solution().convertFive(n))
# Contributed by: Harshit sidhwa

# } Driver Code Ends