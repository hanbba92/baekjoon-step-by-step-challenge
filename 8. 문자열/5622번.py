# 다이얼

word=input()
dir=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
result=0
for i in range(len(word)):
    for j in dir:
        if (word[i] in j):
            result+=dir.index(j)+3
print(result)