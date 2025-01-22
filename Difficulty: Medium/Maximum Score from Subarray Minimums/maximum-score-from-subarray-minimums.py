#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        # Your code goes here
        maxxi= float("-inf")
        s =0
        
        l =0
        for i in range(len(arr)):
            if l>=2:
                s-=arr[i-2]
                l-=1
            l+=1
            s+=arr[i]
            if s>maxxi:
                maxxi=s
            
            if s==0:
                s=0
        
        return maxxi
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends