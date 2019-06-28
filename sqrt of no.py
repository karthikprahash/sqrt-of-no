# sqrt-of-no
import math
i,j=map(int,input().split())
u=i*j
k=int(math.sqrt(u))
if (u==k*k):
    print('yes')
else:
    print('no')
