'''
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15
'''

N = 5

for i in range(N):
    for j in range(i+1):
        print(chr(65 + j), end=" ")
    print()