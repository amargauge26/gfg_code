#User function Template for python3

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr):
        ##Your code here
        #Return true or false
        
        h ={}
        h[0]=1
        ss=0
        for num in arr:
            ss+=num
            s = ss-0
            
            if s in h:
                return True
            else:
                h[s]=1
        
        return False
        
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]
        if (Solution().subArrayExists(arr)):
            print("true")
        else:
            print("false")

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends