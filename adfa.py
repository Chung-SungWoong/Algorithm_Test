arr = [9, 20, 28, 18, 11]
for i in range(len(arr)):
    format(arr[i],'b')
for j in arr:
    if len(arr[j]) < 5:
        arr[j] = '00' + arr[j]
        print(arr[j])