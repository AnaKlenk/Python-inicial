#Leia um numero fornecido pelo usuario. Se esse numero for positivo, calcule a raiz
#quadrada do numero. Se o numero for negativo, mostre uma mensagem dizendo que o
#numero e invalido.
import math
numero = int(input("digite um numero:"))

if numero > 0 :
    raiz = math.sqrt(numero)
    print(F"A raiz do número {numero} é {raiz}")
else :
    quadrado = numero * numero
    print(F" O quadrado do numero {numero} é {quadrado}")