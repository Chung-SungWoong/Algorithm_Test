"""
콜라 빈 병 2개를 가져다주면 콜라 1병을 주는 마트가 있다. 빈 병 20개를 가져다주면 몇 병을 받을 수 있는가?
콜라를 받기 위해 마트에 주어야 하는 병 수 a, 빈 병 a개를 가져다 주면 마트가 주는 콜라 병 수 b, 가지고 있는 빈 병의 개수 n이 매개변수로 주어집니다. 
받을 수 있는 콜라의 병 수를 return 하도록 solution 함수를 작성해주세요.
"""

def solution(a, b, n):
    answer = 0
    
    while n >= a:
        pay_back = (n // a) * b
        answer += pay_back
        left = n%a
        n = left + pay_back

    return answer