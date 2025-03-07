class Solution:
    def removeDuplicates(self, arr):
        i = 0
        n = len(arr)

        # Iterating through the array
        for j in range(1, n):
            # If the current element is not equal to the previous element,
            # then increment i and update arr[i] with the current element
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]
        
        # Return the array containing only unique elements
        return i+1


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    line = 1

    solution = Solution()

    for _ in range(t):
        if line < len(data):
            arr = list(map(int, data[line].split()))
            line += 1
            ans = solution.removeDuplicates(arr)
            for i in range(ans):
                print(arr[i], end=" ")
            print()
        print("~")

# } Driver Code Ends