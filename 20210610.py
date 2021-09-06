#이코테 2.그리디&구현
'''
#<거스름돈>
n= int(input())
count = 0

array = [500, 100, 50, 10]

for coin in array:
    count += n//coin #n을 coin으로 나눈 몫을 count에 담는다
    n %= coin #나머지

print(count)

#화폐의종류 반복문이 수행된다. 소스코드의 시간복잡도는 O(K) 이다.
'''


#<문제>1이될때까지
n, k = map(int, input().split())

count = 0

while True:
    target = (n//k)*k
    count += (n-target)
    n = target

    if n<k:
        break

    count += 1
    n //= k

count += (n-1)
print(count)
