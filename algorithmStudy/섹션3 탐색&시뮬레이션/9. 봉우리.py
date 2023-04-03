# 북 동 남 서 탐색하는 방법!
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

# 테두리 0으로 초기화 하기
a.insert(0, [0] * n)
a.append([0] * n)
for x in a:
    x.insert(0, 0)
    x.append(0)

# all() 모두 참일 경우 참!
cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if all(a[i][j] > a[i+dx[k]][j + dy[k]] for k in range(4)):
            cnt += 1

print(cnt)