'''
nome = input("Digite o nome do aluno:")
n1 = float(input("Digite a primeira nota:"))
n2 = float(input("Digite a primeira nota:"))

media = (n1 + n2) / 2

if media <= 10 and media >= 6:
    print(f"Aprovado com média {media}")
elif media < 6 and media >= 4:
    print("Recuperação")
    print("Compareça ao laboratório 1 no dia 10/12.")
elif media < 4 and media >= 0:
    print(f"Reprovado com média {media}")
else:
    print("Revise as notas do aluno")
'''
'''
peso = float(input("Digite o peso (kg): "))
altura = float(input("Digite a altura (m): "))
imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso normal"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Excesso de peso"
elif imc < 35:
    classificacao = "Obesidade classe I"
elif imc < 40:
    classificacao = "Obesidade classe II"
else:
    classificacao = "Obesidade classe III"


print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")
'''
#1
idade = int(input("Digite a idade do nadador: "))

if idade >= 5 and idade <= 7:
    print("Categoria: Infantil A")
elif idade >= 8 and idade <= 10:
    print("Categoria: Infantil B")
elif idade >= 11 and idade <= 13:
    print("Categoria: Juvenil A")
elif idade >= 14 and idade <= 17:
    print("Categoria: Juvenil B")
elif idade >= 18:
    print("Categoria: Adulto")
else:
    print("Idade abaixo da mínima para classificação.")


#2
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

if numero >= 0:
    print("O número é positivo.")
else:
    print("O número é negativo.")

#3
altura = float(input("Digite sua altura em metros: "))
sexo = input("Digite o sexo (M para masculino, F para feminino): ")

if sexo == 'M' or sexo == 'm':
    peso_ideal = (72.7 * altura) - 58
    print("Peso ideal (masculino):", round(peso_ideal, 2), "kg")
elif sexo == 'F' or sexo == 'f':
    peso_ideal = (62.1 * altura) - 44.7
    print("Peso ideal (feminino):", round(peso_ideal, 2), "kg")
else:
    print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")

#4
saldo_medio = float(input("Digite o saldo médio do último ano: "))

if saldo_medio <= 200:
    credito = 0
elif saldo_medio <= 400:
    credito = saldo_medio * 0.20
elif saldo_medio <= 600:
    credito = saldo_medio * 0.30
else:
    credito = saldo_medio * 0.40

print("Saldo médio:", round(saldo_medio, 2))
print("Crédito especial:", round(credito, 2))


#5
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

print("Escolha o tipo de média:")
print("1 - Aritmética")
print("2 - Ponderada (pesos 3, 3 e 4)")
opcao = int(input("Digite a opção (1 ou 2): "))

if opcao == 1:
    media = (nota1 + nota2 + nota3) / 3
    print("Média Aritmética:", round(media, 2))
elif opcao == 2:
    media = (nota1 * 3 + nota2 * 3 + nota3 * 4) / 10
    print("Média Ponderada:", round(media, 2))
else:
    print("Opção inválida.")
