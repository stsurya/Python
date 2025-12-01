'''
******
**  **
*    *
*    *
**  **
******
'''

sp = 0
N = 3
for i in range(N):
    print("*" * (N-i),end="")
    print(" "*sp,end="")
    print("*"*(N-i))
    sp+=2

sp -= 2
for i in range(1, N+1):
    print("*" * i,end="")
    print(" "*sp,end="")
    print("*"*i)
    sp-=2