import sys
sys.stdin = open("input.txt", "rt")

n, m = map(int, input().split())
a = list(map(int, input().split()))

# result = 0
# cnt = 0
# for i in range(n):
#     result = a[i]
#     for j in range(i + 1, n):
#         print(result, cnt)
#         if result == m:
#             cnt += 1
#             break
#         elif result > m:
#             break
#         result += a[j]
#
# print(cnt)


# 포인터 변수를 사용하기
# tot이 목표보다 크고 작음을 비교해서 포인터를 이동시킴
# 포인터가 배열의 수보다 커지면 while문을 빠져나오기
lt = 0
rt = 1
tot = a[0]
cnt = 0


while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1


print(cnt)