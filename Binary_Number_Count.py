"""
입력 받은 정수를 이진수로 변환하여 1의 개수를 세는 프로그램을 작성하라
"""

def Bi_Count(n):
    m = str(bin(n))
    
    return m.count('1')
    


print(Bi_Count(1000))