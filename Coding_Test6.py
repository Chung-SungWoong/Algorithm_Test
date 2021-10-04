"""
두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
"""

def solution(n, m):
    answer = []
    CSG = []
    CDG = []
    i = 1
    while True:
        if n % i == 0 and m % i == 0:
            CSG.append(i) 
        i += 1
        if i > n or i > m:
            break
            
    for j in range(n*m,0,-1):               # n * m 에서 시작하여 1까지 -1씩 줄어들게 for loop 돌림
        if j % n == 0 and j % m == 0:
            CDG.append(j)
    answer.append(max(CSG))
    answer.append(min(CDG))

    return answer


""" 다른 사람들의 답변 
1. 유클리드 호제법
def gcdlcm(a, b):               인풋 a, b
    for i in range(a):          for a 까지
        if a%(a-i)+b%(a-i) == 0:    a와 b를 무슨 값으로 나눈 몫이 0이라면 
            return [a-i, a*b/(a-i)] 최소공배수는 그 값이고 최대 공약수는 a,b를 곱한값을 최소공배수로 나눈 값이다
"""