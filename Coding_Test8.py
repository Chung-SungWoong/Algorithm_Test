def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if numbers[i]+numbers[j] not in answer:
                answer.append(numbers[i]+numbers[j])
    answer.sort()
    return answer


"""다른 사람 풀이
def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            answer.append(numbers[i] + numbers[j])
    return sorted(list(set(answer)))

거의 동일하나 if ~~ not in 함수 대신 answer 리스트를 set으로 변환시킨 후 다시 리스트로 변환 시켜 중복 값을 삭제 시킴
"""

print(solution([2,1,3,4,1]))