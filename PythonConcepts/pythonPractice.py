'''
A 
A B 
A B C
A B C D
A B C D E
'''

N = 5

for i in range(N):
    for j in range(N-i):
        print(chr(65 + j), end=" ")
    print()