import math
def f(n):
    return math.exp(n) - math.exp(-n) -2 # функция
def df(n):
    return math.exp(n) + math.exp(-n) # производная фунции
mon = []
l = 0.0 # левый конец отрезка
r = 1.0 # правый конец отрезка
eps = 0.000001 # погрешность

# проверка на монотонность
for i in range(0,101):
    mon.append(df(i*0.01))
if (all(x>0 for x in mon) or all(x <0 for x in mon)) and f(l)*f(r)<0:

# поиск решения    
    while abs(r-l)>eps:
        b = l - (f(l)*(r-l))/(f(r)-f(l))
        if f(b) == 0:
            print(b)
            break
        if f(l)*f(b)<0:
            r = b
        else:
            l = b
print(b) # вывод ответа
