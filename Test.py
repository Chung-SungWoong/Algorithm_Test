def solution(nums):
    answer = 0
    i = set(nums)
    j = list(i)
    
    if len(j) >= len(nums)/2:
        answer = len(nums)/2
    else:
        answer = int(len(j))
    
    return answer

print(solution([3,1,2,3]))