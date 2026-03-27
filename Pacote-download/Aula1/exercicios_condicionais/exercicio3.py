#Faca um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
#peso ideal, utilizando as seguintes formulas (onde h corresponde a altura): `
#Homens: (72.7 ∗ h) − 58   Mulheres: (62, 1 ∗ h) − 44, 7

altura = float(input("digite a altura: "))
sexo = int(input("Digite o sexo: 1 para Mulher e 2 para Homem "))

if sexo == 1 :
    pesoM = (62.1 * altura) - 44.7
    print(F"Seu peso ideal é {pesoM:.2f}")

elif sexo == 2 :
    pesoH = (72.7 * altura) - 58
    print(F"seu peso ideial é: {pesoH:.2f}")

else :
    print("valores invalidos")