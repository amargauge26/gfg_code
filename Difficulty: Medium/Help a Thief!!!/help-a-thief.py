#User function Template for python3
class Solution:
    def maxCoins(self, A, B, T, N):
        # Combine the values and counts into a list of tuples
        plates = [(B[i], A[i]) for i in range(N)]
        
        # Sort the plates based on coin value in descending order
        plates.sort(reverse=True, key=lambda x: x[0])
        
        # Initialize variables for maximum coins collected and number of plates used
        maxi = 0
        plates_used = 0
        
        # Iterate through each plate in sorted order
        for value, count in plates:
            if plates_used >= T:
                break
            # Determine how many coins to take from the current plate
            coins_to_take = min(count, T - plates_used)
            maxi += coins_to_take * value
            plates_used += coins_to_take
        
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        T,N=map(int,input().split())
        A=list(map(int,input().split()))
        B=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxCoins(A,B,T,N))
# } Driver Code Ends