"""
arr1 = [[1,2],[2,3]]	
arr2 = [[3,4],[5,6]]

answer = [[]]
answer.pop()

for i in range(len(arr1)):
    mid = []
    for j in range(len(arr1[0])):
        
        mid.append(arr1[i][j] + arr2[i][j])
    answer.append(mid)

print(answer)


def solution(arr1, arr2):
    answer = [[]]
    answer.pop()

    for i in range(len(arr1)):
        save = []
        for j in range(len(arr1[0])):
            save.append(arr1[i][j] + arr2[i][j])
        answer.append(save)

    return answer

"""
def solution(n):
    answer = ''
    n_swer = 0
    w = str(n)
    n_swer = sorted(w,reverse = True)
    for i in range(len(n_swer)):
        answer += n_swer[i]

    return answer

print(solution(1523))