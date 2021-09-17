"""
길 찾기 알고리즘 
내가 적은 해답
"""

n = int(input())
x = 1
y = 1

plans = input().split()

for i in range(len(plans)):
	if(plans[i] == "R"):
		x = x + 1
		if(x > n):
			x = x - 1
	elif(plans[i] == "L"):
		x = x - 1
		if(x < 1):
			x = x + 1 
	elif(plans[i] == "U"):
		y = y - 1
		if( y < 1):
			y = y + 1
	elif(plans[i] == "D"):
		y = y + 1
		if(y > n):
			y = y - 1
	
print(x,y)

