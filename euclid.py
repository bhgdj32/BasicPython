a = input()
b = input()
def euclid(a,b):
    r = 1
    while r != 0:
        r = a % b
        a , b = b , r
    return a
def euclid_prime_number(a,b):
    if euclid(a , b) == 1:
        return True
    else:
        return False
print(euclid(a,b))
print(euclid_prime_number(a,b))