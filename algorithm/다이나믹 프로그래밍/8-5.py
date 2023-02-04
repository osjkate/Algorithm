n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

# count = 0
# array.sort(reverse=True)
# for i in array:
#     while m >= i:
#         m -= i
#         count += 1
#
# if m > 0:
#     print(-1)
# elif m == 0:
#     print(count)

INF = 10001
d = [INF] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != INF:
            d[j] = min(d[j], d[j - array[i]] + 1)


