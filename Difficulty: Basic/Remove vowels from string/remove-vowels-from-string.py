#User function Template for python3
class Solution:
	def removeVowels(self, S):
		# code here
        """s="aeiou"
        
        for char in S:
            if char in s:
                S=S.replace(char,"")
        
        
        return S"""
        
        
        S=S.replace("a","").replace("e","").replace("i","").replace("o","").replace("u",'')
        return S
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		
		ob = Solution()	
		answer = ob.removeVowels(s)
		
		print(answer)


# } Driver Code Ends