"""
to make 1
"""

n, k = map(int,input().split())
result = 0

while True:
    target = (n//k) * k         #(N === K로 나누어떨어지는 수)가 될 때까지 1씩 뺴기
    result += (n - target)
    n = target
    if n < k:                   #N이 K보다 작을 때 반복문 탈출
        break
    result += 1                 #k로 나누기
    n //= k
result += (n - 1)
print(result)