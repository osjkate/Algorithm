n = int(input())
array = []
for i in range(n):
    array.append(tuple(input().split()))


def setting(data):
    return data[1]


array.sort(key=setting)
# array.sort(key=lambda student: student[1])

for i in array:
    print(i[0], end=" ")

