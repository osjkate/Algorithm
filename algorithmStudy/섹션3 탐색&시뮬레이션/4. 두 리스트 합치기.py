n = int(input())
list1 = list(map(int, input().split()))
m = int(input())
list2 = list(map(int, input().split()))
list3 = []
p1 = p2 = 0

# p1, p2 = 0, 0
# list3 = [0] * (n + m)
# cnt = 0
# 맨 뒤에서 붙일 거기 때문에 append() 사용하는게 더 깔끔함!
# 슬라이스 기능을 사용하여 뒤에 붙여주는 것이 더 깔끔함!
# while p1 < n and p2 < m:
#     if list1[p1] <= list2[p2]:
#         # list3[cnt] = list1[p1]
#         list3.append(list1[p1])
#         # cnt += 1
#         p1 += 1
#     else:
#         list3.append(list2[p2])
#         p2 += 1
#
# if p1 == n:
#     while p2 != m:
#         list3.append(list2[p2])
#         p2 += 1
# else:
#     while p1 != n:
#         list3.append(list1[p1])
#         p1 += 1


while p1 < n and p2 < m:
    if list1[p1] <= list2[p2]:
        list3.append(list1[p1])
        p1 += 1
    else:
        list3.append(list2[p2])
        p2 += 1

if p1 == n:
    while p2 != m:
        list3.append(list2[p2])
        p2 += 1
else:
    while p1 != n:
        list3.append(list1[p1])
        p1 += 1


if p1 < n:
    list3 = list3 + list1[p1:]
else:
    list3 = list3 + list2[p2:]


for i in list3:
    print(i, end=" ")
