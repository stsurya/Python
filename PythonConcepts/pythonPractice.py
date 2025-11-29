'''
A B C D E 
A B C D 
A B C
A B
A
'''

N = 5

for i in range(N):
    for j in range(i+1):
        print(chr(65 + i), end=" ")
    print()