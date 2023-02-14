n, m, k = map(int, input().split())
data = list(map(int, input().split()))
maxIndex = 0

data.sort()
first = data[n-1]
second = data[n-2]
result = 0

# count = 0
# while count < m:
#     count2 = 0
#     while count2 < k:
#         result += first
#         count2 += 1
#         count += 1
#         print(count, result)
#     result += second
#     count += 1
#     print(count, result)


# while True:
#     for i in range(k):
#         if m == 0:
#             break
#         result += first
#         m -= 1
#     if m == 0:
#         break
#     result += second
#     m -= 1

# result += (m // (k + 1)) * (first * k + second)   # (k + 1) 항까지 더한 수가 반복되는 횟수
# result += m % (k + 1) * first     # 나머지 항들 계산

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k + 1)) * k
count += m % (k + 1)

result += count * first #가장 큰 수 계산
result += (m - count) * second  #두 번째로 큰 수 계산

print(result)
