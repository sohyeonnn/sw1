#소프트웨어 원리 과제2_2
result = 0
for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        result += i
print(result)