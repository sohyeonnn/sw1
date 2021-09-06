#백준(사칙연산) 2588 곱셈
'''
a = int(input())  # 첫번째 입력받은 문자 : 숫자로 변환
b = input()       # 두번째 입력받은 문자 : 문자열 그대로 둠
#왜? 숫자를 하나씩 떼어내서 a에 b의 각 자리수를 각각 곱해야 하기 때문에

# 문자열의 인덱스를 이용해서 두번째 입력 받은 문자를 하나씩 숫자로 반환하고 A와 곱한다.
AxB2 = a * int(b[2])
AxB1 = a * int(b[1])
AxB0 = a * int(b[0])
AxB = a * int(b)

print(AxB2, AxB1, AxB0, AxB, sep='\n')
# sep='\n'로 줄바꿈, sep은 print함수에서 출력할 값이 여러개 일 때 각 값의 사이사이에 삽일할 문자를 지정할 수 있는 파라미터이다.
'''


#백준(if문) 1330; 두 수 비교하기


'''
a, b = map(int, input().split())

if a > b :
    print('>')
elif a < b:
    print('<')
else:
    print('==')
'''


#9498; 시험 성적
'''
score = int(input())

if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('F')
'''


#2753; 윤년
'''
연도가 주어졌을 때, 윤년이면 1, 아니면 0을 출력하는 프로그램을 작성하시오.

윤년은 연도가 4의 배수이면서, 100의 배수가 아닐 때 또는 400의 배수일 때이다.


year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print('1')
elif year % 4 == 0 and year % 400 == 0:
    print('1')
else:
    print('0')
'''


#14681; 사분면 고르기
'''
x = int(input())
y = int(input())

if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
else:
    print('4')
'''


#2884; 알람 시계
'''
h, m = map(int, input().split())

if m >= 45:
    print(h, m-45)
elif h > 0 and m < 45:
    print(h - 1 , m + 15)
else:
    print(23, m + 15)
'''


#백준(for문); 2739; 구구단
'''
n = int(input())
result = 0     #result에 결과값을 담아줘야함

for i in range(9):
    i = i + 1
    result = n * i
    print(n,'*', i,'=',result)
'''


#10950; A+B-3
'''
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(a + b)
'''


#8398; 합
'''
n = int(input())
hap = 0

for i in range(n):
    i += 1
    hap += i
print(hap)
'''


#15552; 빠른 A+B
'''
python 을 사용하고 있다면ㅁ input대신 sys.stdin.readline 을 사용할 수 있다.
맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고싶을 경우 .rstrip()을 추가로 해주는것이 좋다.
***
rstrip을 하라는 건 문자열 자체를 변수에 저장하고 싶을 때 얘기지,
개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있습니다.
즉 int(sys.stdin.readline()), sys.stdin.readline().split()
이렇게 해도 아무 문제 없습니다.
참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.

import sys
n = int(input())

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
'''


#2741; N찍기
'''
n = int(input())

for i in range(1, n+1):
    print(i)
    

#2742; 기찍 N
n = int(input())

for i in range(1, n+1):
    n = n - 1
    print(n+1)
'''


#11021; A+B-7
'''
n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print("Case #"+str(i+1)+": "+str(a)+" + "+str(b)+" =", a + b)
'''


#2438,9; 별찍기-1,2
'''
n = int(input())

for i in range(n):
    i += 1
    print(" " * (n-i) + "*"* i)
'''


#10871; X보다 작은 수
'''
n, x = map(int, input().split())


a = list(map(int, input().split()))
for i in range(n):
    if x > a[i]:
        print(a[i], end=' ')
'''


##백준(while문); 10952; A+B-5
'''
while True:

    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
'''

#**오류처리를 위한 try, except문 기본 구조 활용
#10951; A+B-4
'''
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)

    except:
        break
'''


#1110; 더하기 사이클
'''
n = int(input())
num = n
count = 0

while True:     #n = 26들어가면 num = 26이 입력된다
    a = num // 10       #a = 2(나눈값)
    b = num % 10        #b = 6(나머지)
    c = (a+b) % 10
    new_num = (b * 10) + c
    count += 1

    if new_num == n:
        break
    num = new_num
print(count)
'''
'''
input_num = int(input())

num = input_num  # num 변수에 input_num을 지정
cnt = 0
while True:
    sum_num = (num // 10) + (num % 10)  # 각 자릿수를 더한수
    new_num = ((num % 10) * 10) + (sum_num % 10)  # 새로 만들어지는 수
    cnt += 1  # 사이클 카운트
    if new_num == input_num :
        break
    num = new_num  # num 변수에 last_num을 지정
print(cnt)
'''


##백준(리스트); 10818; 최소, 최대
'''런타임에러
n = int(input())

for i in range(n):
    a = list(map(int, input().split()))
    print('{} {}'.format(min(a), max(a)))
'''


#2562; 최댓값
# a = [int(input()) for _ in range(9)]    #여러줄에 입력받기 (한줄에 입력받기는 split함수를 사용)

'''잘못쓴 내 코드 ,_,
a = []
for i in range(9):
    a = [int(input()) for i in range(9)]

print(max(a))
print(max(str(a[i])))
'''
'''
a = []  #빈 리스트 생성
for i in range(9):
    a.append(int(input()))
print(max(a))
print(a.index(max(a))+1)       #이때는 str이 아니라 index값을 돌려받는다
'''


#2577; 숫자의 개수
'''
a = int(input())
b = int(input())
c = int(input())
AxBxC = list(str(a*b*c))

#list = [[0 for j in range(1)] for i in range(10)]



for i in range(10):
    print(AxBxC.count(str(i)))
'''


#3052; 나머지    **기억하기*** 중복제거는 set함수 이용!!!!!
'''#**리스트나 튜플은 순서가 있기(ordered)때문에 인덱싱을 통해 자료형의 값을 얻을 수 있지만
set 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 값으 ㄹ 얻을 수 없다.
(딕셔너리 역시 순서가 없는 자료형이라 인덱싱을 지원하지 않는다.)
set 자료형에 저장된 값을 인덱싱으로 접근하려면 다음과 같이 리스트나 튜플로 변환한 후 해야한다.
*중복을 허용핟지 않는 set의 특징*은 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용되기도 한다.
'''

#n = [int(input()) for i in range(10)]    #수 10개를 입력받음 여기서는 사용 x
n = []      #빈 리스트 

for i in range(10):     #0~9까지 총 10개의 자리를 만들어줌
    a = int(input())    #10개의 자리에 입력을 받음
    b = a % 42          # 입력받은 10개의 a를 42로 나눠서 나머지값을 b에 넣어줌
    n.append(b)         #빈 리스트 n에 b값을 넣어줌
s = set(n)              #set(n)으로 중복을 제거한 값을 s에 넣어줌(이때 중복이 제거된 42의 나머지값들이 들어가게됨)
print(len(s))           #s의 길이(몇개인지)를 출력함

