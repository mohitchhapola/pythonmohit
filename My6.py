p=input("principle value-")
r=input("rate of intrest-")
t=input("time of intrest taken-")
P=int(p)
R=int(r)
T=int(t)
m=P*R*T
M=int(m)
i=M/100
I=float(i)
a=P+I
A=float(a)
print("intrest of money after",t,"years,Rs-",I)
print("amount after",t,"years is-",a)
