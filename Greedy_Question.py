"""
손님에게 돈을 거슬러 줘야 할 때 가장 동전을 적게 사용하여 돌려주는 알고리즘 
n = 거슬러줘야 하는 돈
사용 가능한 동전 (*동전의 수는 무한)
"""
n = 1260  
count = 0


cointypes = [500, 100, 50, 10]   		# 코인 타입을 어레이에 지정

for i in cointypes: 			#첫번째 코인 타입부터 for loop
	count += n // i 			#count 에 동전을 값을 나눈 수를 더함
	n %= i						#n에 i를 나눈 값의 나머지를 입력 
	
print(count)
