'''
#6022
a= input()
print(a[0:2],a[2:4],a[4:])
'''

'''
#6027
s=ord(input())
print(s)
print(chr(s+1))

'''
#6046 비트단위 시프트 연산자 <<,>>
'''정수를 2배로 곱하거나 나누어 계산해 준다.
컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,
왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
가장 오른쪽에 있는 1비트는 사라진다.
'''
#a=int(input())
#print(a<<1)

'''#6047
a, b = map(int, input().split())

print(a<<b)
'''

#6048 정수2개 입력받아 비교하기

#a, b, c=map(int, input().split())

'''#6071
n=1

while n!=0:
    n = int(input())
    if n!=0:
        print(n)
    else:
        break

'''

'''
#6072,7073
n = int(input())

#2
while 1 <= n <= 100:
    print(n-1)
    n = n-1

#3
while True:
    n = n-1
    print(n)

    if n==0:
        break
'''
'''
#6074
n = ord(input())
start = ord('a')

while True:
    print(chr(start), end = ' ')

    n = n - 1


    if n == 96:
        break

        '''
'''
#6074 c, a b c 출력하기
a = input()
start = ord('a')
while True:
    print(chr(start), end = ' ')
    start = start + 1
    if chr(start) == a:
        print(a)
        break
'''

'''
#출력한계 초과가 자주 일어난다
n = int(input())
start = 0

while 0 <= n <= 100:
    print(start)

    start = start+1
    if start == n:
        print(n)
        break

#따라서 코드도 간단하며 직관적인 for문을 이용하자
a = int(input())

for i in range(0, a+1):
    print(i)
'''

#6077
'''영문 소문자 'q'가 입력될 때까지
입력한 문자를 계속 출력하는 프로그램을 작성해보자.
'''
'''
while True:
    n = input()

    print(n)

    if n =="q":
        break
'''

