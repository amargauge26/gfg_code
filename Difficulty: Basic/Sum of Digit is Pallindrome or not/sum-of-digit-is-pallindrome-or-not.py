#User function Template for python3
class Solution:
    def isDigitSumPalindrome(self, n):
        # Calculate the sum of digits
        digit_sum = 0
        while n > 0:
            digit_sum += n % 10
            n //= 10
        
        # Check if the digit sum is a palindrome
        original_sum = digit_sum
        reversed_sum = 0
        
        while digit_sum > 0:
            reversed_sum = reversed_sum * 10 + digit_sum % 10
            digit_sum //= 10
            
        return 1 if original_sum == reversed_sum else 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        ob=Solution()
        print(ob.isDigitSumPalindrome(N))
# } Driver Code Ends