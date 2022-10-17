"""
거스름 돈
"""

n = int(input())        #거슬러줘야 할 값
count = 0               #동전 갯수

coin_types = [500,100,50,10]    #거슬러 줄 동전 타입

for coin in coin_types:         #가장 큰 500원부터 100 50 10 순서대로 
    count += n // coin          #카운트에 n을 단위로 나눈 몫을 더한다
    n %= coin                   #n에 거스름돈 갱신

print(count)                    #동전 갯수 프린트