def solution(participant, completion):
    answer = ''
    part = ''
    comp = ''
    part = sorted(participant)
    comp = sorted(completion)
    for i in range(len(completion)):
        if part[i] != comp[i]:
            answer = part[i] 
            print(part,comp)
            break
    answer = part[-1]
    return answer


print(solution(["mislav", "stanko", "mislav", "ana"],["stanko", "ana", "mislav"]))

"""
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]

프로그램 카운터 사용해서 직접 인자들을 뺀 후 리스트 0번을 불러 냄

"""