```
*****
*****
*****
*****
*****

N = 5
for i in range(N):
    for j in range(N):
        print("*",end="")
    print()
```

```
* 
* * 
* * *
* * * *
* * * * *
* * * * * *

N = 5

for i in range(N):
    for j in range(i+1):
        print("*",end="")
    print()
```

```
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6

N = 5
for i in range(N):
    for j in range(i+1):
        print(j+1,end=" ")
    print()
```

```
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
6 6 6 6 6 6

N = 5
for i in range(N):
    for j in range(i+1):
        print(i+1,end=" ")
    print()
```

```
* * * * * *
* * * * * 
* * * * 
* * * 
* * 
* 

N = 5
for i in range(N):
    for j in range(N-i):
        print("*",end=" ")
    print()
```

```
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2 
1


N = 5
for i in range(N):
    for j in range(N-i):
        print(j+1,end=" ")
    print()
```
```
     *     
    ***    
   *****   
  *******  
 ********* 
***********

N = 5
for i in range(N):
    for j in range(N-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    for j in range(N-i):
        print(" ",end="")
    print()
```

```
***********
 *********
  *******
   ***** 
    ***    
     *

N = 5
for i in range(N):
    for j in range(i):
        print(" ",end=" ")
    for j in range(2*N-(2*i+1)):
        print("*",end=" ")
    for j in range(i):
        print(" ",end="")
    print()

```

```
  *  
 ***
***** 
*****  
 ***
  *    


N = 3
for i in range(N):
    for j in range(N-i):
        print(" ",end=" ")
    for j in range(2*i+1):
        print("*",end=" ")
    for j in range(i):
        print(" ",end="")
    print()

for i in range(N):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(2*N-(2*i+1)):
        print("*",end=" ")
    for j in range(i):
        print(" ",end=" ")
    print()
```

```
*  
**
***  
**
*    

N = 3
for i in range(N):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(N,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
```

```
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1 
0 1 0 1 0 1

N = 6
for i in range(N):
    if(i%2 == 0):
        start = 1
    else:
        start = 0
    for j in range(i+1):
        print(start,end=" ")
        start = 1 - start
    print()
```

```
1       1
12     21
123   321
1234 4321


N = 4
space = 2 * (N-1)
for i in range(N):
    for j in range(i+1):
        print(j+1,end="")
    for j in range(space+1):
        print(" ",end="")
    for j in range(i,-1,-1):
        print(j+1,end="")
    space -= 2
    print()
```

```
1 
2 3 
4 5 6
7 8 9 10
11 12 13 14 15


N = 5
start = 0

for i in range(N):
    for j in range(i+1):
        start +=1 
        print(start, end=" ")
    print()
```

```
A 
A B 
A B C
A B C D
A B C D E

N = 5

for i in range(N):
    for j in range(i+1):
        print(chr(65 + j), end=" ")
    print()
```

```
A B C D E 
A B C D 
A B C
A B
A

N = 5

for i in range(N):
    for j in range(N-i):
        print(chr(65 + j), end=" ")
    print()
```

```
A 
B B 
C C C
D D D D
E E E E E

N = 5

for i in range(N):
    for j in range(i+1):
        print(chr(65 + i), end=" ")
    print()
```

```
D 
C D 
B C D 
A B C D 

N = 6
start = 65 + (N-1)
for i in range(N):
    for j in range(i+1):
        print(chr(start+j), end=" ")
    print()
    start-=1
```

```
******
**  **
*    *
*    *
**  **
******

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
```

```
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *


N = 5
sp = (2*N) - 2
for i in range(N):
    print("*" * (i+1),end="")
    print(" "*sp,end="")
    print("*"*(i+1))
    sp-=2

sp+=4
for j in range(N-1):
    print("*"*(N-(j+1)),end="")
    print(" "*sp,end="")
    print("*"*(N-(j+1)))
    sp+=2
```

```
*****
*   *
*   *
*   *
*****

n = 5

for i in range(n):
    # Inner loop for columns
    for j in range(n):
        # Print star if it's a border cell
        if i == 0 or j == 0 or i == n - 1 or j == n - 1:
            print("*", end="")
        # Print space otherwise
        else:
            print(" ", end="")
    # Move to next line after each row
    print()
```

```
3 3 3 3 3 
3 2 2 2 3 
3 2 1 2 3 
3 2 2 2 3 
3 3 3 3 3

n = 3

for i in range(2 * n - 1):
    # Inner loop for columns
    for j in range(2 * n - 1):
        # Calculate distance from top
        top = i
        # Calculate distance from left
        left = j
        # Calculate distance from bottom
        bottom = (2 * n - 2) - i
        # Calculate distance from right
        right = (2 * n - 2) - j

        # Take the minimum of all four distances
        minDist = min(top, bottom, left, right)

        # Print number (starts with n at border, decreases inside)
        print(n - minDist, end=" ")
    # Move to the next row
    print()
```