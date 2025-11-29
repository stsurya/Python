'''
1       1
12     21
123   321
1234 4321
'''

N = 5
start = 0

for i in range(N):
    for j in range(i+1):
        start +=1 
        print(start, end=" ")
    print()