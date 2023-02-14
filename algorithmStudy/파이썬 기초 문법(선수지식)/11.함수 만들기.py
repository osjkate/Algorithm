'''
함수 만들기
특정 기능을 하는 코드를 계속 반복해서 작성
코드가 길어지고, 유지 보수하기 어려워짐
=> 함수를 만들어 놓으면 재사용성이 높아짐

# 함수는 스크립트 위쪽에 작성되어 있어야 한다!


def add(a, b):
    c = a + b
    print(c)


add(3, 2)


def add(a, b):
    c = a + b
    return c    # 함수를 종료하는 역할도 함!


print(add(3, 2))



def add(a, b):
    c = a + b
    d = a - b
    return c, d
# 파이썬은 여러 개의 값을 리턴할 수 있다. 튜플값으로 리턴함!


print(add(3, 2))
'''


def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


a = [12, 13, 7, 9, 19]
for x in a:
    if is_prime(x):
        print(x, end=' ')
print()
