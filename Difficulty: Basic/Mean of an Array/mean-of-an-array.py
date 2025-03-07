#User function Template for python3

class Solution:
    def findMean(self, arr):
        # code here 
        s = sum(arr)
        return s//(len(arr))


#{ 
 # Driver Code Starts
def main():
    t = int(input().strip())  # Reading the number of test cases
    for _ in range(t):
        arr = list(map(int,
                       input().strip().split())
                   )  # Reading and converting input to a list of integers
        solution = Solution()
        print(solution.findMean(
            arr))  # Calling the function and printing the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends