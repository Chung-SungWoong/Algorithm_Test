"""
연속된 세 개의 정수를 더해 12가 되는 경우는 3, 4, 5입니다. 
두 정수 num과 total이 주어집니다. 연속된 수 num개를 더한 값이 total이 될 때, 
정수 배열을 오름차순으로 담아 return하도록 solution함수를 완성해보세요.

단, num개의 연속된 수를 더하여 total이 될 수 없는 테스트 케이스는 없습니다.
"""

import math

def solution(num, total):
    answer = []
    check = math.ceil(total/num)
    start_num = check - (num//2)
    for i in range(num):
        answer.append(start_num + i)
    
    return answer