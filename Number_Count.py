"""
두 정수 X, Y의 임의의 자리에서 공통으로 나타나는 정수 k(0 ≤ k ≤ 9)들을 이용하여 만들 수 있는 가장 큰 정수를 두 수의 짝꿍이라 합니다(단, 공통으로 나타나는 정수 중 서로 짝지을 수 있는 숫자만 사용합니다). 
X, Y의 짝꿍이 존재하지 않으면, 짝꿍은 -1입니다. X, Y의 짝꿍이 0으로만 구성되어 있다면, 짝꿍은 0입니다.

예를 들어, X = 3403이고 Y = 13203이라면, X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 3, 0, 3으로 만들 수 있는 가장 큰 정수인 330입니다. 
다른 예시로 X = 5525이고 Y = 1255이면 X와 Y의 짝꿍은 X와 Y에서 공통으로 나타나는 2, 5, 5로 만들 수 있는 가장 큰 정수인 552입니다(X에는 5가 3개, Y에는 5가 2개 나타나므로 남는 5 한 개는 짝 지을 수 없습니다.)
두 정수 X, Y가 주어졌을 때, X, Y의 짝꿍을 return하는 solution 함수를 완성해주세요.
"""
def solution(X, Y):
    answer = ''
    n = 0
    Check_X = [0,0,0,0,0,0,0,0,0,0]
    Check_Y = [0,0,0,0,0,0,0,0,0,0]
    for i in X:
        Check_X[int(i)] += 1
    
    for i in Y:
        Check_Y[int(i)] += 1

    for i in range(9,-1,-1):
        if Check_X[i] >= 1 and Check_Y[i] >= 1 and i == 0 and answer == '':
            answer = '0'
            break
        if Check_X[i] >= Check_Y[i]:
            answer += str(i) * Check_Y[i]
        else:
            answer += str(i) * Check_X[i]
        
    if answer == '':
        answer = '-1'
    return answer

print(solution("100","203045"))


"""
0이 9개 들어있는 리스트 두개를 만들어야 했던 문제
여전히 코드가 더러워 좋게할 여지가 많음
"""