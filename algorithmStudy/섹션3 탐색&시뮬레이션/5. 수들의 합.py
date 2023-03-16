n, m = map(int, input().split())
a = list(map(int, input().split()))

result = 0
cnt = 0
for i in n:
    for j in (i, n):
        i += j
        if i == m:
            cnt += 1
            break
        elif i > m:
            break


print(cnt)
