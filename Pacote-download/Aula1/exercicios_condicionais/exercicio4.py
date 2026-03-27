#calculaar a equação de segundo grau. delta = b^2 - 4*a*c
#x = -b +- raizdelta / 2*a
import math
a = int(input("digite o valor de a: "))
b = int(input("digite o valor de b: "))
c = int(input("digite o valor de c: "))

delta = pow(b,2) - 4 * a * c

if a == 0 :
    print("Nao é equação de segundo grau")

else:
    delta = pow(b, 2) - 4 * a * c

    if delta < 0:
        print("Não existem raízes reais.")

    elif delta == 0:
        x = -b / (2 * a)
        print(f"Existe uma única raiz real: {x}")

    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"As raízes são {x1} e {x2}")
