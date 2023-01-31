# 위치 입력 받기
location = input()

# 위치를 좌표로 바꾸기
x = int(ord(location[0]))-int(ord('a')) + 1
y = int(location[1])

count = 0

# 움직일 수 있는 모든 경우의 수
move_types = [(-2, -1), (-2, 1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2)]


for move_type in move_types:
    # 움직인 후 위치 좌표
    nx = x + move_type[0]
    ny = y + move_type[1]

    # 이동한 좌표가 체스판을 벗어날 경우
    if nx < 1 or nx > 8 or ny < 1 or ny > 8:
        continue
    count += 1

print(count)