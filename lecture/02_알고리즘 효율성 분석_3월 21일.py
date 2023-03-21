# 실습 1
A = [int(n) for n in input().split()]
key = int(input())


def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return i
    return -1


# 출력합니다.
print("%d 찾기: " % (key), sequential_search(A, key))


# 실습2
n = int(input())


def compute_squeare_A(n):
    return n*n


# 실습 5
A = [int(n) for n in input().split()]


def unique_elements(A):
    n = len(A)
    for i in range(n - 1):
        for j in range(i - 1, n):
            if A[i] == A[j]:
                return False
    return True


print(unique_elements(A))


# 실습 7 recursive

n = int(input())


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(n))


# 실습 8 iterable

n = int(input())


def factorial(n):
    result = 1
    for k in range(n, 0, -1):
        result = result * k
    return result


def factorial2(n):
    result = 1
    for k in range(1, n + 1): # 직관적으로 표현하면 이렇게 표현할 수 있음.
        result = result * k
    return result


print(factorial(n))


# 실습 6 iterable 교재 81p

n = int(input())


def binary_digits(n):
    count = 1
    while n > 1:
        count = count + 1
        n = n // 2
    return count


def binary_digits2(n):
    count = 1
    k = 1
    while k < n:
        count = count + 1
        k = k * 2
    return count


print(binary_digits(n))


# 실습 10 recursive

n = int(input())


def binary_digits(n):
    if n <= 1:
        return 1
    else:
        return 1 + binary_digits(n // 2)


# 한바퀴 도는 거여서 괜찮음 별로 안비효율적임
def binary_digits2(n):
    if n < 1:
        return 0
    else:
        return 1 + binary_digits(n // 2)


print(binary_digits(n))


# 실습 9 하노이 탑

# Hanoi(1, start, tmp, to) = move(1, start, to)
# Hanoi(N, start, tmp, to) = Hanoi(N - 1, start, to, tmp) + move(N, start, to) + Hanoi(N - 1, tmp, start, to)

def hanoi_tower(n, fr, tmp, to):
    if n == 1:
        print("원판 1: %s --> %s" %(fr, to)) # move 함수와 대응됨
    else:
        hanoi_tower(n - 1, fr, to, tmp)
        print("원판 1: %s --> %s" % (fr, to))
        hanoi_tower(n - 1, tmp, fr, to)


hanoi_tower(4, 'A', 'B', 'C')


#

