"""

"""
def solution(s):
    answer = ''
    
    while s > 0:
        s, rest = divmod(s,3)
        answer += str(rest)

    answer = int(answer,3)
        
    return answer