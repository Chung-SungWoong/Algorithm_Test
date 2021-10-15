"""
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
"""

def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        check = 0
        for j in range(1,i):
            if i % j == 0:
                check += 1
        if check % 2 == 0:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13,17))

""" 다른 답변
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:         #아마 수학적 뭐가 있는듯 1/2 제곱의 값이 자연수라면 소수가 홀수개인가?
            answer -= i
        else:
            answer += i
    return answer
"""