import sys
sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

ave = int((sum(a) / n) + 1)

# b = list(map(lambda k: abs(k - ave), a))
#
# minStd = 0
# for i in range(n):
#     if b[minStd] > b[i]:
#         minStd = i
#     elif b[minStd] == b[i]:
#         if a[minStd] < a[i]:
#             minStd = i
#
# print(ave, minStd + 1)

min = 214000000
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if x > score:
            score = x
            res = idx + 1
print(ave, res)


