n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

reward = [0] * n
cnt = 0
for i in array:
    if i[0] == i[1] and i[1] == i[2]:
        reward[cnt] = 10000 + i[0] * 1000
    elif i[0] == i[1] or i[0] == i[2]:
        reward[cnt] = 1000 + i[0] * 100
    elif i[1] == i[2]:
        reward[cnt] = 1000 + i[1] * 100
    else:
        reward[cnt] = max(i) * 100
    cnt += 1

print(max(reward))

