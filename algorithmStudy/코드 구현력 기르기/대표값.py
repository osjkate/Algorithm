n = int(input())
a = list(map(int, input().split()))

ave = int((sum(a) / n) + 1)
# round는 round_half_even 방식을 택한다.
# 4.5 => 4 짝수쪽으로 근사값을 가진다.
# 그래서 0.5를 더하고 버림을 택함으로써 오류를 없애기

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