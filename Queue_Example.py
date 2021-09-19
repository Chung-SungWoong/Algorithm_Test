"""
파이썬 큐 예제
First In Last Out (FILO)
"""

from collections import deque

queue = deque()             # deque는 스택과 큐의 장점을 모두 채택한 것인데 데이터를 넣고 빼는 속도가 리스트 자료형에 비해 효율적이며 queue 라이브러리를 이요하는 것보다 더 간편하다

queue.append(5) 
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)
