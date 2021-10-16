"""
나머지가 1이 되는 수 찾기
자연수 n이 매개변수로 주어집니다. n을 x로 나눈 나머지가 1이 되도록 하는 가장 작은 자연수 x를 return 하도록 solution 함수를 완성해주세요. 
답이 항상 존재함은 증명될 수 있습니다.
"""

def solution(n):
    answer = n - 1
    for i in range(2,answer):
        if answer % i == 0:
            answer = i
            return answer
    return answer

print(solution(3043))
"""
def solution(n):
    answer = 0
    for i in range(2, n):
        if n % i == 1:
            return i
    return answer

이 코드가 결과 값을 발견했을 때 바로 코드를 끝낼 수 있어서 더 좋은 코드로 보임
"""
