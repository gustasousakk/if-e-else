import math

a = float(input("Digite o valor de A:"))
b = float(input("Digite o valor de B:"))
c = float(input("Digite o valor de C:"))
delta = (b**2) - (4*a*c)

x=math.sqrt
x1 = (-b+x(b**2-4*a*c))/(2*a)
x2 = (-b-x(b**2-4*a*c))/(2*a)

if delta >= 0:
    print ("(",x1,",",x2,")") 
elif delta <= 0:
    print("Não há raízes reais")
elif a==0:
    print("Não é equação de segundo grau")