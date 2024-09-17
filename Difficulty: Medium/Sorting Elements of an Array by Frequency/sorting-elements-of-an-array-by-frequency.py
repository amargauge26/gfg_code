#code
from collections import Counter
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr.sort()
    
    arr_counted = Counter(arr)
    
    arr_sorted = sorted(arr_counted.items(), key=lambda x: (-x[1], x[0]))
    
    
    for k,val in arr_sorted:
        for i in range(val):
            print(k,end=' ')
        
    print()
    
    