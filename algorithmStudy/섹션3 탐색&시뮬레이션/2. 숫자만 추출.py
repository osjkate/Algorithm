# s = input()
#
# cnt = 0
# sum = 0
# for i in s:
#     if 48 <= ord(i) <= 57:
#         sum = sum * 10 + int(i)
#
# print(sum)
#
# for i in range(1, sum + 1):
#     if sum % i == 0:
#         cnt += 1
#
# print(cnt)

s = input()
res = 0
for x in s:
    if x.isdecimal():
        res = res * 10 + int(x)
print(res)
cnt = 0
for i in range(1, res + 1):
    if res % i == 0:
        cnt += 1
print(cnt)
