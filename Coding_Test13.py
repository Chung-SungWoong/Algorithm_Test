def solution(s):
    answer = True
    if s.count("P")+ s.count('p') != s.count('y') + s.count('Y'):
        answer = False

    return answer