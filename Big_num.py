#큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때 주어진 수들을 m번 더하여 가장 큰 수를 만드는 법칙, 단 해당하는 수가 연속해서 k번 초과하여 더해질 수 없다 
# N(2<N<1000), M(1<M<10000), k(1<K<10000)
# 배열의 크기 N, 숫자가 더해지는 횟수 M, K번 초과할수없는 수
# 직접 짠 코드 

n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

data.sort() 		#수를 정렬 
first = data[n-1] 	#가장 큰 수
second = data[n-2] 	#두번째로 가장 큰 수

result = 0			
while True:
	if (m >= k+1):			#만약 더하는 수의 길이가 반복할수 있는 수보다 길때
		result += (first*k) #가장 큰 수 * k 를 result에 추가
		result += second	#두번째로 가장 큰 수를 result에 추가
		m = m - (k+1) 		#더한 횟수만큼 m에서 삭감
	
	elif(0 < m < k):		#만약 더하는 수의 길이가 반복할 수 있는 수보다 짧을 때
		result += (first*m) #가장큰수 곱하기 더하는 횟수
		m = 0				#m = 0

	elif(m == 0):			#만약 m이 0이라면
			break			#while loop 탈출

print(result)
