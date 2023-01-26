from functools import reduce
import sys

a = [1, 2, 3, 4, 5, 5, 5]
remove_set = [3, 5]

result = [i for i in a if i not in remove_set]
print(result)

print("")


data = dict()
data["apple"] = "Apple"
data["banana"] = "Banana"
data["coconut"] = "Coconut"

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)


score = 85
result = "Success" if score > 80 else "Fail"
print(result)
print("")

a = [1, 2, 3, 4, 5, 5]
remove_set = {3, 5}
result = []
for i in a:
    if i not in remove_set:
        result.append(i)
print(result)

result = [i for i in a if i not in remove_set]
print(result)
print("")

i = 1
result = 0

while i <= 9:
    result += i
    i += 1
print("1씩 더하기: ", result)

i = 1
result = 0
while i <= 9:
    if i % 2 == 1:
        result += i
    i += 1
print("홀수만 더하기: ", result)

print("")
# for문 사용하기
result = 0
for i in range(1, 10):
    result += i
print("for문 사용해서 1씩 더하기: ", result)
result = 0
for i in range(1, 10):
    if i % 2 == 1:
        result += i
print("for문 사용해서 홀수만 더하기: ", result)
print()

# 구구단
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(i, " * ", j, " = ", i * j)
#     print()

# (lambda 매개변수 : 함수 구현)(인자)
print((lambda a, b: a + b)(4, 5))
print()

map_lambda = list(map((lambda x: x**2), range(5)))
reduce_lambda = reduce(lambda a, b: b + a, "abcde")
filter_lambda = list(filter((lambda a: a < 4), range(10)))
print(map_lambda)
print(reduce_lambda)
print(filter_lambda)
print()

# 입력
# n = int(input())
# data = list(map(int, input().split()))
# data.sort(reverse=True)
# print(data)
# print()
#
# data = sys.stdin.readline().rstrip()
# print(data)
# print()

# 출력
answer = 9
print(f"정답은 {answer}입니다.")
print()

# sorted
result = sorted([("홍길동", 35), ("이순신", 75), ("아무개", 50)], key=lambda x: x[1], reverse=True)
print(result)