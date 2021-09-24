"""
집합 자료형 
"""

data = set([1,1,2,3,4,4,5,6])
print(data)

data2 = {3,4,4,5,6, 9 ,10}
print(data2)

#합집합
print(data|data2)

#교집합
print(data & data2)

#차집합
print(data - data2)

data.add(8)
#새로운 원소 여러 개 추가
data.update([0,7])

#특정한 값을 갖는 원소 삭제
data.remove(3)
print(data)