n = int(input())
plans = input().split()
x, y = 1, 1
nx, ny = 1, 1

# L, R, U, D
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ["L", "R", "U", "D"]

for plan in plans:
    for i in range(len(move_types)):
        nx = x
        ny = y
        if plan == move_types[i]:
            nx += dx[i]
            ny += + dy[i]
            if nx < 1 or ny < 1 or nx > n or ny > n:
                continue
            else:
                x, y = nx, ny

print(x, y)
