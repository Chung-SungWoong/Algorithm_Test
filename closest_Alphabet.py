"""
문자열 s가 주어졌을 때, s의 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알고 싶습니다.
예를 들어, s="banana"라고 할 때,  각 글자들을 왼쪽부터 오른쪽으로 읽어 나가면서 다음과 같이 진행할 수 있습니다.
문자열 s이 주어질 때, 위와 같이 정의된 연산을 수행하는 함수 solution을 완성해주세요.
"""

def solution(s):
    answer = []
    check = []
    for i in range(len(s)):
        if ord(s[i]) in check:
            pos = check.index(ord(s[i]))
            answer.append(i-pos)
            check.append(ord(s[i]))
            check[pos] = 0
        else:
            answer.append(-1)
            check.append(ord(s[i]))
        
    return answer

"""
시간 복잡도 효율안좋음
체점 기준이 널널해서 통과
"""