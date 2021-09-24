"""
순열과 조합
"""

from itertools import permutations
from itertools import combinations
from itertools import product
from itertools import combinations_with_replacement 

data = ['A','B','C']  # 데이터 준비

result = list(permutations(data,3))
result2 = list(combinations(data,2))
result3 = list(product(data, repeat = 2))                # 2개를 뽑는 모든 순열 구하기 (중복 허용)
result4 = list(combinations_with_replacement(data,2))    # 2개를 뽑는 모든 조합 구하기 (중복 허용)
print(result)
print(result2)
print(result3)
print(result4)