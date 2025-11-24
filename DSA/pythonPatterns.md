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