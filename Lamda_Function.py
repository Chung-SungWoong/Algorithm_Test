"""
람다 표현식 예시
"""

array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x): 
    return x[1]                 # 두번째 숫자를 기준으로 

print(sorted(array, key=my_key))      #정렬 기준하게
print(sorted(array, key=lambda x: x[1]))


list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]

result = map(lambda a, b: a + b, list1,list2)

print(list(result))