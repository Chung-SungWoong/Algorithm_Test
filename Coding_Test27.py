"""
실패율
전체 스테이지의 개수 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages가 매개변수로 주어질 때, 
실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열을 return 하도록 solution 함수를 완성하라.
N	stages	result
5	[2, 1, 2, 6, 2, 4, 3, 3]	[3,4,2,1,5]
"""
def solution(N, stages):
    check = []
    answer = []
    member = len(stages)
    an = 0
    for i in range(1,N+1):
        num = 0 
        num = stages.count(i)
        check.append(num / member)
        member -= num
    for j in range(len(check)):
        an = check.index(max(check))
        answer.append(an+1)
        check[an] = -1

    return answer

print(solution(4,[4,4,4,4,4]))

"""
70점 짜리 답
내일 다시 고쳐봐야 함
"""