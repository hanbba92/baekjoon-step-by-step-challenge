T=int(input())
x,y=map(int,input().split())
for case in range(T):
    x,y=map(int,input().split())
    k=0
    count=0
    while y>x:
        k+=1
        x+=k
        count+=1
        if x>y:
            x-=k-1
            k-=1
        y-=k
        count+=1
    print(count)
    
