#소프트웨어 원리 과제3_2

def calculator(x, y):
    add = x+y
    sub = x-y
    mul = x*y
    div = x/y
    return add, sub, mul, div

number1 = int(input('정수1 입력:'))
number2 = int(input('정수2 입력:'))

print("사칙연산 계산(덧셈, 뺄셈, 곱셈, 나눗셈):", calculator(number1, number2))