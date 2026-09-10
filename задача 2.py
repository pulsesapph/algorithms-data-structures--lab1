import math
def f(n):
    return math.exp(n) - math.exp(-n) -2
def df(n):
    return math.exp(n) + math.exp(-n)
mon = []
l = 0.0
r = 1.0
eps = 0.000001
for i in range(0,101):
    mon.append(df(i*0.01))
if (all(x>0 for x in mon) or all(x <0 for x in mon)) and f(l)*f(r)<0:
    while abs(r-l)>eps:
        b = l - (f(l)*(r-l))/(f(r)-f(l))
        if f(b) == 0:
            print(b)
            break
        if f(l)*f(b)<0:
            r = b
        else:
            l = b
print(b)
