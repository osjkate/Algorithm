n = int(input())
array = list(map(int, input().split()))


def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)
    return sum


# max = digit_sum(array[0])
# maxIndex = 0
# count = 0
# for i in array:
#     if max < digit_sum(i):
#         maxIndex = count
#     count += 1
#
# print(array[maxIndex])


max = -2147000000
for x in array:
    tot = digit_sum(x)
    if tot > max:
        max = tot
        res = x     # res 사용하는거 잘 보기

print(res)