n, k = map(int, input().split())
array = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i + 1, n):
        for m in range(j + 1, n):
            res.add(array[i] + array[j] + array[m])
res = list(res)
res.sort(reverse=True)
print(res[k - 1])