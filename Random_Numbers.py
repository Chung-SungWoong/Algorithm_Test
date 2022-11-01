"""
숫자 20개를 랜덤으로 뽑고 거기서 3개의 숫자 더하기
"""

import random

score=[random.randint(-100,100) for i in range(20)]
n = random.choices(score,k = 3)
print(-1) if sum(n) else print(0)
