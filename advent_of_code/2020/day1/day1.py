with open('day1.txt') as f:
    arr = f.readlines()

d = {}
for i in range(len(arr)):
    look = 2020 - int(arr[i]) 
    if look in d:
        print(int(arr[d[look]]),' * ', int(arr[i]), ' = ', int(arr[d[look]]) * int(arr[i]))
        i = len(arr)-1
    d[int(arr[i])] = i
