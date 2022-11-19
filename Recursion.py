"""
팩토리얼 계산하기
"""

def factorial(x):
    if x == 1:
        return 1
    return x * factorial(x-1)

print(factorial(4))



# 뭐지 왜 한방에 성공했지