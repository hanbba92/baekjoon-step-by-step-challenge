# 알파벳 찾기
# chr():아스키 코드 값을 문자로 변환

word=input()
alphabet=list(range(97,123))
for i in alphabet:
    print(word.find(chr(i)))