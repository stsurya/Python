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