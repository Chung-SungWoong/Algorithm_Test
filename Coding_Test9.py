def solution(n):
    answer = 0
    i = 1
    while True:
        if i*i == n:
            answer = (i+1)*(i+1)
            break
        if i > n/2:
            return -1
        i += 1
    return answer