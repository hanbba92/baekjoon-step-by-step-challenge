2557
print("Hello World!")

# 10718
print("강한친구 대한육군")
print("강한친구 대한육군")

# 10171
print("""\    /\\
 )  ( ')
(  /  )
 \(__)|""")

# 10172
print("|\_/|")
print("|q p|   /}")
print('( 0 )"""\\')
print("""|"^"`    |""")
print("||_/=\\\\__|")

# 1000 
a, b = map(int,input().split())
print(a + b)
print(a - b)
print(a * b)
print(int(a / b)) #조심...실수로 나옴..
print(a % b)

# 10430
a, b, c = map(int,input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

# 2588
a = int(input())
b = int(input())
c = a * (b % 10)
d = a * ((b % 100)//10)
f = a * (b // 100)
g = a * b
print(c)
print(d)
print(f)
print(g)