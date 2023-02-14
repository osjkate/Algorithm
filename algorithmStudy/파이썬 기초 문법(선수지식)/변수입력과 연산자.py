'''
변수 입력과 연산자

a = input("숫자를 입력하세요 : ")
print(a)


a, b = input("숫자를 입력하세요 : ").split()
print(type(a))
c = a + b
print(type(c))
print(c)


a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
print(type(a))
b = int(b)
print(a + b)

a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
'''

a = 4.3
b = 5
c = a + b
print(type(c))  # 더 큰 범위의 타입으로 나온다.
