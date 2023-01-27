n, m = map(int, input().split())
result = 0


# for i in range(n):
#     data = list(map(int, input().split()))
#     data.sort()
#     if data[0] > result:
#         result = data[0]


# for i in range(n):
#     data = list(map(int, input().split()))
#     result = max(result, min(data))


for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for j in data:
        min_value = min(min_value, j)
    result = max(min_value, result)


print(result)
