#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        
        if low< high:
            part = self.partition(arr,low,high)
            self.quickSort(arr,low,part-1)
            self.quickSort(arr,part+1,high)
        
        return arr
    
    def partition(self,arr,low,high):
        p = arr[low]
        i = low+1
        j = high
        
        while (i<=j):
            while i<=high and arr[i]<=p:
                i+=1
            
            while arr[j]>p:
                j-=1
            
            
            if i<j:
                arr[i],arr[j]=arr[j],arr[i]
        
        arr[low],arr[j]=arr[j],arr[low]
        
        return j
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends