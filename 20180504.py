import math
# def F(x):
#     return(2*math.sin(math.pi*x)+math.cos(math.pi*x))
def g(a,b):
    return((a+b)/2)
def f(x):
    return(x**2-2*x)  #(-1,1)  0   (1,3)  2

a=float(input('a='))
b=float(input('b='))
c=0.01
k=0
m=0

while(1):
    if (f(a) * f(b) > 0):
        a = float(input('请重新输入a='))
        b = float(input('请重新输入b='))
    else:
        if f(a)*f(b)==0:
            if f(a)==0:
                print(a,k)
                break
            else:
                print(b,k)
                break
        else:
            m=g(a,b)
            if(a-b)**2<c**2:
                print(m,k)
                break
            else:
                if(f(m)*f(b)<0):
                    a=m
                else:
                    b=m
                k=k+1