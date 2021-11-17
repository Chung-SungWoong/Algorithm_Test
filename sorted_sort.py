#sorted()는 퀵 정렬과 동작방식이 비슷한 병합 정렬을 기반으로 만들어짐. 시간복잡도 O(NlogN)을 보장한다
array = [7,5,9,0,3,1,6,2,4,8]
result = sorted(array)
print(result)

# sort 별도의 정렬된 리스트가 반환되지않고 내부 원소가 바로 정렬
array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)

array = [('banana',2), ('apple',5),('carrot',3)]

def setting(data):
    return data[1]
result = sorted(array,key = setting)
print(result)


"""
문제에서 별도의 요구가 없다면 기본 정렬 라이브러리를 사용하고, 데이터의 범위가 한정되어 있고 더 빠르게 동작해야 할 때는 계수 정렬을 사용
"""