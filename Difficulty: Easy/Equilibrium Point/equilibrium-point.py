# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        t=arr[:]
        v=arr[:]
        ss=0
        vv=0
        for i in range(len(arr)):
            ss+=arr[i]
            t[i]=ss
        
        for i in range(len(arr)-1,-1,-1):
                    vv+=arr[i]
                    v[i]=vv
        
        for i in range(len(arr)):
            if t[i]==v[i]:
                return i
        
        return -1
        
                    
                    

