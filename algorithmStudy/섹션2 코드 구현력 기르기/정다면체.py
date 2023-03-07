n, m = map(int, input().split())
array = [0] * (n + m + 1)

for i in range(1, n + 1):
    for j in range(1, m + 1):
        array[i + j] += 1


maxNum = 0
for i in range(n + m + 1):
    if array[i] > maxNum:
        maxNum = array[i]
for i in range(n + m + 1):
    if maxNum == array[i]:
        print(i, end=" ")