a = int(input("aを入力"))
b = int(input("bを入力"))
r = a % b
while r != 0:
    r = a % b
    a , b = b , r
print(a) 
