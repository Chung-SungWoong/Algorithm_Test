def solution(lottos, win_nums):
    answer = []
    for i in range(len(lottos)):
        if lottos[i] in win_nums:
            win_nums.remove(lottos[i])
    
    best = len(win_nums) - lottos.count(0) + 1
    worst = len(win_nums)+1
    if worst > 6:
        worst = 6
    if best > 6:
        best = 6
    answer.append(best)
    answer.append(worst)
    return answer


print(solution([1,2,3,4,5,6],[7,8,9,10,11,12]))

""" 랭크를 따로 리스트로 만들어 맞춘 숫자를 세어서 랭크를 얻음. 
def solution(lottos, win_nums):

    rank=[6,6,5,4,3,2,1]

    cnt_0 = lottos.count(0)
    ans = 0
    for x in win_nums:
        if x in lottos:
            ans += 1
    return rank[cnt_0 + ans],rank[ans]
"""