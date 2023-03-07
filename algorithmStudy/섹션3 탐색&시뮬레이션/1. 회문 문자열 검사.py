# 내가 푼 방식
# n = int(input())
# array = []
# for i in range(n):
#     array.append(input())
# cnt = 0
# for i in array:
#     cnt += 1
#     i = i.lower()
#     tmp = i[::-1]
#     if i == tmp:
#         print("#%d %s" % (cnt, "YES"))
#     else:
#         print("#%d %s" % (cnt, "NO"))

# 강의 방식 1
# n = int(input())
# for i in range(n):
#     s = input()
#     s = s.upper()
#     size = len(s)
#     for j in range(size // 2):
#         if s[j] != s[-1 - j]:
#             print("#%d %s" % (i + 1, "NO"))
#             break
#     else:
#         print("#%d %s" % (i + 1, "YES"))

# 강의 방식 2
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#%d YES" % (i + 1))
    else:
        print("#%d NO" % (i + 1))