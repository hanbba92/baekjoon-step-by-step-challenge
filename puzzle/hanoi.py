def hanoi(source,goal,path,n):
    if n==1:
        print("move disk 1 from", source,"to",goal)
        return
    hanoi(source,path,goal,n-1)
    print("move disk",n,"from",source,"to",goal)
    hanoi(path,goal,source,n-1)
N=4
hanoi('A','C','B',N)
