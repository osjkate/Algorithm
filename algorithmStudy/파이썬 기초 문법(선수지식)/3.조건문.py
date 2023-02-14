'''
조건문 if(분기, 중첩)
'''

x = 15
if x == 7:
    print("Lucky")
    print("ㅋㅋ")

if x >= 10:
    if x % 2 == 1:
        print("10 이상의 홀수")


x = 10
if x > 0:
    if x < 10:
        print("x는 10보다 작은 자연수")


x = 7
if x > 0 and x < 10:
    print("10보다 작은 자연수")


x = 5
if 0 < x < 10:  # 파이썬만 가능한
    print("10보다 작은 자연수")


x = 10
if x > 0:
    print("양수")
else:
    print("음수")


x = 93
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print('C')
elif x >= 60:
    print('D')
else:
    print('F')


x = 93
if x >= 90:
    print('A')
if x >= 80:
    print('B')
if x >= 70:
    print('C')
if x >= 60:
    print('D')
