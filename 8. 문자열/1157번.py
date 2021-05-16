# 단어 공부

word=input().upper() #ABCABCA
word_list=list(set(word)) #ABC
word_most=list()
for i in word_list: #ABC 순서대로 들어감.
    a=word.count(i)
    word_most.append(a) # [3,2,2]
if word_most.count(max(word_most))>=2: # 3이 [3,2,2]에서 2개 이상이면
    print("?")
else:
    print(word_list[word_most.index(max(word_most))]) #word_list[0]=A