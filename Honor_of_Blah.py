"""
가수의 점수가 지금까지 출연 가수들의 점수 중 상위 k번째 이내이면 해당 가수의 점수를 명예의 전당이라는 목록에 올려 기념합니다.
k일 다음부터는 출연 가수의 점수가 기존의 명예의 전당 목록의 k번째 순위의 가수 점수보다 더 높으면, 출연 가수의 점수가 명예의 전당에 오르게 되고 기존의 k번째 순위의 점수는 명예의 전당에서 내려오게 됩니다.
"""

def solution(k, score):
    answer = []
    honor = []
    for i in range(len(score)):
        if len(honor) < k:
            honor.append(score[i])
            honor.sort(reverse=True)
        elif len(honor) == k and min(honor) < score[i]:
            honor.pop()
            honor.append(score[i])
            honor.sort(reverse=True)
            print(honor)
        answer.append(honor[-1])
    return answer


print(solution(4,[0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))