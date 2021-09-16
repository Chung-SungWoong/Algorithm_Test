# There are only two possible process in this question.
# The first porcess is subtract 1 from N 
# And the other is divide N with K
# Make N as 1 and get the number of steps that you conduct the process

n, k = 187, 3
count = 0

while True:
	if(n%k == 0):
		n = n/k
		count += 1
	elif(n == 1):
		break
	elif(n%k != 0):
		n = n-1
		count += 1

		
print(count)
		
 
