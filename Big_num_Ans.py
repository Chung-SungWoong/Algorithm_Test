"""
큰 수의 법칙 
책 해답
"""

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

data.sort() 		#수를 정렬 
first = data[n-1] 	#가장 큰 수
second = data[n-2] 	#두번째로 가장 큰 수

result = 0

while True:
    for i in range(k):      #가장 큰 수를 k번 더하기
        if m == 0:          #만약 m이 0이라면 반복문 탈출
            break
        result += first
        m -= 1              #더할 때마다 1 씩 빼기
    if m == 0:     
        break
    result += second        #두 번째로 큰 수를 한 번 더하기
    m -= 1

print(result)


"""
if문으로 예외를 정해주는 것이 아닌
while 로 모든 경우를 포괄적으로 설명하니 
내가 쓴 코드보다 확실히 간결함
"""