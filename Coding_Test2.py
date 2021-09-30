
def solution(arr):
    answer = []
    print(len(arr))
    for i in range(len(arr)):
        if i+1 == len(arr):
            answer.append(arr[i])
            continue
        if arr[i] == arr[i+1]:
            continue
        else:
            answer.append(arr[i])
    
    return answer


print(solution([1,2,3,3,3,1,2]))


"""
def no_continuous(s):
    a = []
    for i in s:
        if a[-1:] == [i]: continue
        a.append(i)
    return a
"""