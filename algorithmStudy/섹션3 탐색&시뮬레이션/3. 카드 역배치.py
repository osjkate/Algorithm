array = list(range(21))


# for _ in range(10):
#     i, j = map(int, input().split())
#     sumIndex = i + j - 2
#     for k in range(i - 1, (sumIndex + 1) // 2):
#         array[k], array[sumIndex - k] = array[sumIndex - k], array[k]
#         # swap 하는 방법 알아두기!!
#
# for i in array:
#     print(i, end=" ")

for _ in range(10):
    s, e = map(int, input().split())
    for i in range((e - s + 1) // 2):
        array[s + i], array[e - i] = array[e - i], array[s + i]


array.pop(0)

for x in array:
    print(x, end=" ")