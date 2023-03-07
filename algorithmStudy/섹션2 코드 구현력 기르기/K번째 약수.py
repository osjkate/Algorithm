n, k = map(int, input().split())

# array = []
# for i in range(1, n + 1):
#     if n % i == 0:
#         array.append(i)
#
# if len(array) >= k:
#     print(array[k - 1])
# else:
#     print(-1)


cnt = 0
for i in range(1, n + 1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)

