class Solution:
	def mergeOverlap(self, arr):
		#Code here
        
        a=sorted(arr,key = lambda x:x[0])
        
        ans =[]
        ans.append(a[0])
        for i in range(1,len(a)):
            temp = ans[-1]
            if temp[1]>=a[i][0]:
                ans.pop()
                temp=[temp[0],max(a[i][1],temp[1])]
                ans.append(temp)
            else:
                ans.append(a[i])
        
        return ans
            

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        # a = list(map(int, input().strip().split()))
        arr = []
        # j = 0
        for i in range(n):
            a = list(map(int, input().strip().split()))
            x = a[0]
            # j += 1
            y = a[1]
            # j += 1
            arr.append([x, y])
        obj = Solution()
        ans = obj.mergeOverlap(arr)
        for i in ans:
            for j in i:
                print(j, end=" ")
        print()

# } Driver Code Ends