#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function template for Python

import heapq
class Solution:
    #Function to find the days of buying and selling stock for max profit.
	def stockBuySell(self, arr):
        # code here
        n = len(arr)
        
        if n <2:
            return 0
        
        total=0
        i=0
        
        while i <n-1 :
            #finding tera bhai ka minima
            while i <n-1 and arr[i] >= arr[i+1]:
                i+=1
            
            if i ==n-1:
                break
            
            buy =i
            i+=1
            heap=[]
            while i  <n and arr[i]>=arr[i-1]:
                heapq.heappush(heap,(-arr[i],i))
                i+=1
            
            
            if heap:
                sellamount,ind = heapq.heappop(heap)
                total+=arr[ind]-arr[buy]
        
        return total
                
        

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.stockBuySell(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends