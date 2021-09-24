"""
리스트 컴프리헨션
"""

# 
array = [i for i in range(20) if i % 2 == 1]

print(array)

# 1부터 9까지의 숫자의 제곱 수를 포함하는 리스트
array1 = [i * i for i in range(1,10)]

print(array)

"""
리스트 컴프리헨션은 2차원 리스트를 초기화할 때 효과적으로 사용될 수 있다
n x m 크기의 2차원 리스트를 한번에 초기화 해야 할 때 매우 유용
ex)
array = [[0] * m for _ in range(n)]
bad ex)
array = [[0] * m] * n
위의 코드는 전체 리스트 안에 포함된 각 리스트가 모두 같은 객체로 인식된다
"""