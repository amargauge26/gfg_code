#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        hash = {}
        n = len(arr)
        for i in range(n):
            if arr[i] in hash:
                hash[arr[i]]+=1
            
            else:
                hash[arr[i]]=1
        ans = []
        a=0
        for i in range(1,n+1):
            if i not in hash:
                a=i
        
        b=max(hash,key=hash.get)
        ans=[b,a]
        return ans
            




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findTwoElement(arr)
        print(str(ans[0]) + " " + str(ans[1]))
        tc = tc - 1
        print("~")

# } Driver Code Ends