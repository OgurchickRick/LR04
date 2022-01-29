arr = [-11, 10, 19, -20, -14, -14, 13, -15, -5, 7, 10, -8, -1, 15, -20, -14, -11, 16, -15, 3]
brr = [arr[i] for i in range(len(arr)) if arr[0:i].count(arr[i]) == 0 and arr[i+1:].count(arr[i]) > 0]
print(*brr)