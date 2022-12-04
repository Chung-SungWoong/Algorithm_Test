from collections import Counter

def solution(k, tangerine):
    answer = 0
    c = Counter(tangerine).most_common()
    while k > 0:
        k -= c[answer][1]
        answer += 1
    
    return answer

print(solution(6,[1, 3, 2, 5, 4, 5, 2, 3]))