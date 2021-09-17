#(1<N, M<100) 
"""
숫자 카드 게임은 여러 개의 숫자 카드 중에서 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임이다.
n x m 형태로 놓여있고
먼저 뽑고자 하는 카드가 포함되어 있는 행을 선택한 후 그 행에 포함된 카드 중 가장 숫자가 낮은 카드를 뽑는다
따라서 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야한다

ex)					ans)  2
3 3						
3 1 2 
4 1 4 
2 2 2
"""

n, m = map(int, input().split())				#input값 입력. 

result = 0

for i in range(n):
	data = list(map(int, input().split()))		#각 인풋값들을 리스트에 저장
	
	min_val = min(data)							#한 행중 가장 작은 값
	
	result = max(result, min_val)				#각 행들의 가장 작은 값들 중 가장 큰 값. 찐중최
	
print(result)
