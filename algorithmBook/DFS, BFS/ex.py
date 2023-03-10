from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)


def recursive_function(i):
    if i == 100:
        return
    print(i, "번째 재귀 함수에서", i + 1, "번째 재귀 함수를 호출합니다.")
    recursive_function(i + 1)
    print(i, "번째 재귀 함수를 종료합니다. ")


recursive_function(1)


# factorial 함수
# 반복 함수
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# 재귀 함수
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)


print(factorial_iterative(5))
print(factorial_recursive(5))

INF = 999999999
# 인접 행렬
graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print(graph)

# 인접 리스트
graph2 = [[] for _ in range(3)]
graph2[0].append((1, 7))
graph2[0].append((2, 5))
graph2[1].append((0, 7))
graph2[2].append((0, 5))
print(graph2)
