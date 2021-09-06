#6092: 이상한 출석 번호 부르기1
'''
출석 번호를 n번 무작위로 불렀을 때,
각 번호(1 ~ 23)가 불린 횟수를 각각 출력해보자.

입력:첫 번째 줄에 출석 번호를 부른 횟수인 정수 n이 입력된다. (1 ~ 10000)
두 번째 줄에는 무작위로 부른 n개의 번호(1 ~ 23)가 공백을 두고 순서대로 입력된다.



n = int(input())
a = list(map(int, input().split()))

number = []
for i in range(24):      #[0 ,0, .., 0] 과 같이 24개의 정수 값 0을 추가해넣음 (23개의 자리를 만듦)
    number.append(0)    #각 값은 number[0] ~ number[23]으로 값을 읽고 저장할수 있음
for i in range(0, n):      #번호를 부를 때마다, 그 번호에 대한 카운트가 1씩 증가한다.
    number[a[i]] += 1
for i in range(1, 24):      #0,1,2,....23번째 까지 이던것을 1부터 24(전까지)  즉 23개 출력한다.
    print(number[i], end=' ')



#셀프 리뷰 코드
n = int(input())
a = list(map(int, input().split()))

number = []             #1; 빈 (list)를 만들어준다
for i in range(24):     #2; 23개의 (list)자리를 만들어준다
    number.append(0)    #3; (list)의 모든 자리에 0을 넣어준다
for i in range(0,n):    #4; 1 ~ n-1 까지의 자리에
    number[a[i]] += 1   # 번호를 부를 때 마다 그 번호에 대한 카운트를 1씩 증가시킨다.
for i in range(1, 24):
    print(number[i], end=' ')   # 카운트한 값을 공백을 두고 출력한다.
'''


#6093: 이상한 출석 번호 부르기2
'''
출석 번호를 n번 무작위로 불렀을 때, 부른 번호를 거꾸로 출력해 보자.

입력: 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.


#대표답안
n = int(input())
k = list(map(int, input().split()))

for i in range(n-1,-1,-1):      #n-1+1 즉 n 부터 
    print(k[i], end=' ')
'''


#6094: 이상한 출석 번호 부르기3
'''
출석 번호를 n번 무작위로 불렀을 때, 가장 빠른 번호를 출력해 보자.
단, 
첫 번째 번호와 마지막 번호가 몇 번인지는 아무도 모른다.
음수(-) 번호, 0번 번호도 있을 수 있다.
*리스트에 출석 번호를 기록해 두었다가, 그 중에서 가장 작은 값을 찾아내면 된다.
입력: 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력된다.
n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력된다.



n = int(input())
k = list(map(int, input().split()))

list2 = []

for i in range(n):
    list2.append(k)

print(min(list2[i]))        #list2.append(k)와 같은 줄에 입력하게되면 최소값이 n 번 출력된다. 유의할것
'''


#6095: 바둑판에 흰 돌 놓기
'''
**이중for문 문제**    
바둑판(19 * 19)에 n개의 흰 돌을 놓는다고 할 때,
n개의 흰 돌이 놓인 위치를 출력하는 프로그램을 작성해보자.
참고) 리스트가 들어있는 리스트를 만들면?
가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있고,
확장한 n차원의 리스트도 만들 수 있다.
입력: 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력된다.
둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력된다.
n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며,
똑같은 좌표는 입력되지 않는다.

///  **리스트 컴프리헨션**
-리스트를 초기화하는 방법중 하나이다.
-대괄호안에 반복문으로 선언한다.
a = [i for i in range(10)]  <- i라는 원소의 값이 차례대로 리스트에 담기도록 하겠다.

*실사용 리스트 컴프리헨션
-리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용
-N*M 크기의 2차원 리스트를 한 번에 초기화 해야할 때 유용
array = [[0] * m for _ in range(n)] 
# n번 반복을 할때마다 길이가 m인 리스트를 새롭게 초기화 하는 방식으로 전체 리스트를 구성한다. 
= N x M 크기이다.


'''

#n = int(input())
#x, y = list(map(int, input().split()))

             #빈 1차원 리스트를 생성


#badook = [[0 for j in range(20)] for i in range(20)]        #리스트 컴프리헨션을 이용하여 한줄로 나타낼 수 있다.
'''

#badook = []
for i in range(20):             #**리스트 가로번호
    badook.append([])   #리스트 안에 다른 리스트를 추가해 넣음
    for j in range(20):         #**리스트 세로번호
        badook[i].append(0)     #리스트안에있는 리스트 안에 0을 추가해 넣음
#print(badook)
'''

'''
n = int(input())
for i in range(n):
    x, y = list(map(int, input().split()))
    badook[int(x)][int(y)] = 1      #리스트이름[번호][번호] 형식으로 저장된다
    # 2 2 /3 3/4 4 .. 꼴로 입력받기위해

for i in range(1, 20):              #1~19까지 출력
    for j in range(1, 20):          #1~19까지 출력
        print(badook[i][j], end=' ')#2차원 리스트를 공백을 두고 한줄로 출력한다
    print()                         #줄바꿈을 해준다.
'''




#6096: 바둑알 십자 뒤집기
'''
십자 뒤집기는
그 위치에 있는 모든 가로줄 돌의 색을 반대(1->0, 0->1)로 바꾼 후, 
다시 그 위치에 있는 모든 세로줄 돌의 색을 반대로 바꾸는 것이다.
어떤 위치를황 골라 집자 뒤집기를 하면, 그 위치를 제외한 가로줄과 세로줄의 색이 모두 반대로 바뀐다.
입력:바둑알이 깔려 있는 상이 19 * 19 크기의 정수값으로 입력된다.
십자 뒤집기 횟수(n)가 입력된다.
십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수이다.



#리스트 컴프리헨션 사용한 코드 // 내부에있는 for 문을 먼저 써줘야한다
unbadook = [[0 for j in range(19)] for i in range(19)]

#일반 중첩for문 사용한 코드
unbadook = []

for i in range(19):         #0~18까지 19개를 가진다.
    unbadook.append([])

    for j in range(19):
        unbadook[i].append(0)       #19*19바둑판에 0 이 들어간 리스트르 만든다.


for i in range(19):
    unbadook[i] = list(map(int, input().split()))



n = int(input())

for i in range(n):
    x, y = list(map(int, input().split()))

    for j in range(19):
        if unbadook[x-1][j] == 0:       #2 2 를 입력했다고 치자, 0~18까지의 자리르 차례대로 돌면서 x에 -1을 한 y축이 2에 해당하는 모든 x자리를 돌게된다. 
            unbadook[x-1][j] = 1
        else:
            unbadook[x-1][j] = 0

        if unbadook[j][y-1] == 0:
            unbadook[j][y-1] = 1
        else:
            unbadook[j][y-1] = 0

for i in range(19):
    for j in range(19):
        print(unbadook[i][j], end=' ')
    print()
'''


#6097: 설탕과자 뽑기
'''
격자판의 세로(h),
가로(w),
막대의 개수(n),
각 막대의 길이(l),
막대를 놓는 방향(d:가로는 0, 세로는 1)과
막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때,

격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

입력: 첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d)->막대를 놓는 방향(d:가로는 0, 세로는 1), 좌표(x, y)가 입력된다.


h, w = map(int, input().split())
#n = int(input()) 위치 어디에해도 상관없음
#zeros = [[0] * w for _ in range(h)]    #리스트컴프리헨션 이용한 다른 코드
pan = [[0 for j in range(w)] for i in range(h)]     #0으로 이루어진 w*h크기의 배열
n = int(input())    #놓을 수 있는 막대의 개수

for i in range(n):  #막대의 개수만큼 막대의 조건을 입력
    l, d, x, y = map(int, input().split())      #n에 해당하는 수만큼 입력

    for j in range(l):
        if d == 0:      #가로방향: x가 기준이 되기때문에 y값이 변한다.
            pan[x-1][y-1+j] = 1     #해당하는 위치/부분에 1을 넣는다
        else:       #세로방향: y값이 기준이 되기 때문에 x값이 변한다.
            pan[x-1+j][y-1] = 1
#x,y좌표가 0,0에서 시작하는 것이아닌 1,1에서 시작하기때문에 x,y에서 1씩 빼준다.

for i in range(h):      #세로 가로를 입력받는다고 했으니까 h가 먼저 입력되어야 함
    for j in range(w):
        print(pan[i][j], end=' ')
    print()
'''


#6098: 성실한 개미
'''
미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고,
먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.

맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는
더이상 이동하지 않고 그 곳에 머무른다고 가정한다.

미로 상자의 테두리는 모두 벽으로 되어 있으며,
개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

입력: 10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.


ant_house= [[0 for j in range(10)] for i in range(10)]

for i in range(10):
    ant_house[i] = list(map(int, input().split()))

x, y = 1, 1

while True:

    if ant_house[x][y] == 2:
        ant_house[x][y] = 9
        break


    if ant_house[x][y+1] != 1:      #오른쪽으로 이동이 가능하다면
        ant_house[x][y] = 9
        y = y + 1
    else:           #오른쪽으로 이동이 불가능하다면
        if ant_house[x+1][y] != 1:
            ant_house[x][y] = 9
            x = x + 1
        else:
            break

for i in range(10):
    for j in range(10):
        print(ant_house[i][j], end=' ')
    print()
'''

ant = [[0 for j in range(10)] for i in range(10)]

for i in range(10):
    ant[i] = list(map(int, input().split()))

x, y = 1, 1

while True:

    if ant[x][y] == 2:
        ant[x][y] = 9
        break

    if ant[x][y + 1] != 1:  # 0이면 접근 가능/ 오른쪽으로 갈 때
        ant[x][y] = 9
        y = y + 1

    else:
        if ant[x + 1][y] != 1:
            ant[x][y] = 9
            x = x + 1
        else:
            ant[x][y] = 9        #14번째 예시 오류 해결 코드
            break


for i in range(10):
    for j in range(10):
        print(ant[i][j], end=' ')
    print()