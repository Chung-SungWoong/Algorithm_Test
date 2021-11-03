"""
소수 찾기
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)
"""

def solution(n):
    answer = 0
    i = 0
    array = []
    for k in range(2,n+1):
        array.append(k)
    
    while True:
        j = 2
        answer += 1
        while array[i] * j <= n: 
            if array[i] * j in array:
                array.remove(array[i]* j)
            j += 1
        if array[i] == array[-1]:
            break
        else:
            i += 1
    return answer

print(solution(10))

"""
시간 초과 및 효율성 테스트 0점
"""