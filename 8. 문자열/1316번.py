# 그룹 단어 체커

n=int(input())
count=0
def checker(word):
    a=[0]
    for i in word:
        if a[-1]!=i:
            if i in a:
                return False
        a+=[i]
    return True

for i in range(n):
    word=input()
    if checker(word):
        count+=1
print(count)