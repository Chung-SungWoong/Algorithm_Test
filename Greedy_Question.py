n = 1260
count = 0


cointypes = [500, 100, 50, 10]

for i in cointypes:
	count += n // i 
	n %= i
	
print(count)
