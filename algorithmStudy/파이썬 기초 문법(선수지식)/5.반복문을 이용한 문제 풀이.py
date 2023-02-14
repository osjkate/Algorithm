'''
반복문을 이용한 문제풀이
1) 1부터 N까지 홀수 출력하기
2) 1부터 N까지 합 구하기
3) N의 약수 출력하기
'''

# 1)
n = int(input("1. 숫자를 입력하세요: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        print(i, end=" ")
print()

# 2)
n = int(input("2. 숫자를 입력하세요: "))
result = 0
for i in range(1, n + 1):
    result += i
print(result)

# 3)
n = int(input("3. 숫자를 입력하세요: "))
for i in range(1, n + 1):
    if n % i == 0:
        if i == n:
            print(i)
            break
        print(i, end=", ")
