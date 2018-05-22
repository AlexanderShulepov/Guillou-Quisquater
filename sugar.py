def exgcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = exgcd(b % a, a)
        return (g, x - (b // a) * y, y)


def inverse_of(a, m):
    g, x, y = exgcd(abs(a), m)
    if g != 1:
        raise Exception('Обратного элемента не существует')
    else:
        if a > 0:
            return x % m
        else:
            return -x % m
def gcd(a,b):
    while a!=0 and b!=0:
       if a > b:
          a = a % b
       else:
          b = b % a
    return True if a+b==1 else False