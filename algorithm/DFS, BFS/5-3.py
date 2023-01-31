n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(list(map(int, input())))


def dfs(x, y):
    if x < 0 or x >= n or y < 0 or y >= m:
        return False
    if array[x][y] == 1:
        return False
    array[x][y] = 1
    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)
    return True


count = 0

for i in range(n):
    for j in range(m):
        if dfs(i, j):
            count += 1

print(count)
