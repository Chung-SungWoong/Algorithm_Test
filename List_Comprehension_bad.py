n = 4
m = 3

array = [[0] * m] *n
print(array)

array[1][1] = 5
print(array)


# 언더바는 파이썬에서 반복을 수행하되 반복을 위한 변수의 값을 무시하고자 할 때 사용

for _ in range(5):
    print("Hello World")

# 단순히 내부적으로 행동을 반복으로 사용할 때
"""
append()  = 변수명.append()
sort()    = 변수명.sort()    or     변수명.sort(reverse = True)    O(NlogN)
reverse() = 변수명.reverse()
insert()  = insert(삽입할 위치 인덱스, 삽입 할 값)
count()   = 변수명.count(특정 값) 
remove()  = 변수명.remove
"""