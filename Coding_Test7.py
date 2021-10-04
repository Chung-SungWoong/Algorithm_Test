def solution(n):
    answer = 0
    h = str(n)
    m = []
    
    for i in range(len(h)):
        answer += int(h[i])
    return answer

print(solution(123))

def sum_digit(number):
    if number < 10:
        return number
    return (number % 10) + sum_digit(number // 10) # 재귀함수로 돌려서... 아니 이걸 재귀함수로 돌릴 생각을 하네

print(sum_digit(123))
