"""
실패함
import math
def solution(progresses, speeds):
    answer = []
    num = 0 
    for i in range(len(progresses)):
        Finish = 100 - progresses[i]
        days = math.ceil(Finish % speeds[i])
        num += 1
        if progresses[i] == progresses[-1]:
            answer.append(num)
            break
        while progresses[i+1] == progresses[-1]:
            while days * speeds[i+1] + progresses[i+1] >= 100:
                num += 1
                i += 1 
            answer.append(num)
            
    return answer

print(solution([93, 30, 55],[1, 30, 5]))
"""

def solution(progresses, speeds):
    answer = []
    num = 0 
    days = 0

    while len(progresses) > 0:
        if progresses[0] + days * speeds[0] >= 100:
            num += 1
            if len(progresses) == 1:
                answer.append(num)
                break
            progresses.pop(0) 
            speeds.pop(0)
        elif progresses[0] + days * speeds[0] < 100:
            if num > 0:
                answer.append(num)
                num = 0
            days += 1

    return answer