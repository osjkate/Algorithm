
n = int(input())
# 이차리스트 입력 받는 법 외우기
a = [list(map(int, input().split())) for _ in range(n)]

# 2차원 리스트 보기 좋게 출력하는 법
# for x in a:
#     print(x)

# maxNum = 0
#
# for i in range(n):
#     if maxNum < sum(a[i]):
#         maxNum = sum(a[i])
#     sumNum = 0
#     for j in range(n):
#         sumNum += a[j][i]
#     if maxNum < sumNum:
#         maxNum = sumNum
#
#
# sumNum2 = 0
# sumNum3 = 0
# for i in range(n):
#     sumNum2 += a[i][i]
#     sumNum3 += a[n - i - 1][i]
# if maxNum < sumNum2:
#     maxNum = sumNum2
# if maxNum < sumNum3:
#     maxNum = sumNum3
#
# print(maxNum)

#최소값 초기화
largest = -2147000000

# 행과 열의 최대 합 구하기
for i in range(n):
    sum1 = sum2 = 0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]

    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선의 최대 합 구하기
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n - i - 1]

if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)