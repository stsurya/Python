'''
D 
C D 
B C D 
A B C D 
'''

N = 6
start = 65 + (N-1)
for i in range(N):
    for j in range(i+1):
        print(chr(start+j), end=" ")
    print()
    start-=1