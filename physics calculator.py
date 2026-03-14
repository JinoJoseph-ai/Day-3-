
def ke(m,v):
    return 0.5*m*v*v
g=10.0
def pe(m,h):
    return m*g*h
def f(m,a):
    return m*a
print("1.KE")
print("2.PE")
print("3.Force")
x=int(input("select which number: "))
if x==1:
    m=float(input("enter the mass"))
    v=float(input("enter the velocity"))
    print(ke(m,v))
elif x==2:
    m=float(input("enter the mass"))
    h=float(input("enter the height"))
    print(pe(m,h))
elif x==3:
    m=float(input("enter the mass"))
    a=float(input("enter the acceleration"))
    print(f(m,a))    
        


