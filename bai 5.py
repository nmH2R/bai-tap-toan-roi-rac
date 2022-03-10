arr = [3, 2, 4, 5, 1, 6]

for i in range(1, len(arr)):
    x = arr[i]
    l = 0
    r = i
    while (l < r):
        m = int(l + (r - l) / 2)
        if (arr[m] >= x):
            r = m
        else:
            l = m + 1
    index = l
    for j in range(i, index - 1, -1):
        arr[j] = arr[j - 1]
    arr[index] = x

print(arr)  