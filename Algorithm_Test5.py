def solution(n):
    answer = []
    chara = str(n)
    for i in range(len(chara)):
        answer.append(int(chara[-i-1]))
    return answer

print(solution(12345))


"""
def digit_reverse(n):
    return list(map(int, reversed(str(n))))
n을 스트링으로 받아서 리버스한 후 인트로 변환해서 리스트 안에 넣는다
"""