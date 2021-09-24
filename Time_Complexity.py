"""
시간 복잡도 계산해보기
"""

# n개의 데이터의 합을 계산하는 프로그램 예제

array = [3,5,1,2,4]
summary = 0 

for x in array:
    summary += x


print(summary)

#수행 시간은 데이터의 개수 n에 비례할 것임을 예측할 수 있슴 시간 복잡도는 O(N)

# 2중 반복문을 이용하는 프로그램 예제

array = [3,5,1,2,3]

for i in array:
    for j in array:
        temp = i * j
        print(temp)

# 시간 복잡도: O(N^2)
# 모든 2중 반복문의 시간 복잡도가 O(N^2) 임은 아님

"""
연산횟수가 5억을 넘어가는 경우
Python은 5 ~ 15초 가량의 시간이 소요된다
pypy의 경우 더 빠르게 동작하기도 함

코딩 테스트의 시간제한은 통상 1 ~ 5초가량
"""