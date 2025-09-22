#1

idade_homem1 = int(input("Digite a idade do primeiro homem: "))
idade_homem2 = int(input("Digite a idade do segundo homem: "))

idade_mulher1 = int(input("Digite a idade da primeira mulher: "))
idade_mulher2 = int(input("Digite a idade da segunda mulher: "))

if idade_homem1 > idade_homem2:
    homem_mais_velho = idade_homem1
    homem_mais_novo = idade_homem2
else:
    homem_mais_velho = idade_homem2
    homem_mais_novo = idade_homem1


if idade_mulher1 > idade_mulher2:
    mulher_mais_velha = idade_mulher1
    mulher_mais_nova = idade_mulher2
else:
    mulher_mais_velha = idade_mulher2
    mulher_mais_nova = idade_mulher1

soma = homem_mais_velho + mulher_mais_nova
produto = homem_mais_novo * mulher_mais_velha

print("\n=== RESULTADOS ===")
print(f"Homem mais velho: {homem_mais_velho} anos")
print(f"Homem mais novo: {homem_mais_novo} anos")
print(f"Mulher mais velha: {mulher_mais_velha} anos")
print(f"Mulher mais nova: {mulher_mais_nova} anos")
print(f"\nSoma do homem mais velho + mulher mais nova: {homem_mais_velho} + {mulher_mais_nova} = {soma}")
print(f"Produto do homem mais novo × mulher mais velha: {homem_mais_novo} × {mulher_mais_velha} = {produto}")

#2


produto = input("Digite a descrição do produto (nome): ")
quantidade = int(input("Digite a quantidade adquirida: "))
preco_unitario = float(input("Digite o preço unitário (R$): "))

total = quantidade * preco_unitario

if quantidade <= 5:
    desconto_percentual = 2
elif quantidade > 5 and quantidade <= 10:
    desconto_percentual = 3
else:  
    desconto_percentual = 5

desconto = total * (desconto_percentual / 100)

total_a_pagar = total - desconto

print("\n=== RESUMO DA COMPRA ===")
print(f"Produto: {produto}")
print(f"Quantidade: {quantidade} unidades")
print(f"Preço unitário: R$ {preco_unitario:.2f}")
print(f"Total sem desconto: R$ {total:.2f}")
print(f"Desconto aplicado: {desconto_percentual}% = R$ {desconto:.2f}")
print(f"TOTAL A PAGAR: R$ {total_a_pagar:.2f}")

print(f"\nVocê economizou: R$ {desconto:.2f}")

#3

caes_atendidos = int(input("Quantos cães foram atendidos nesta semana? "))

print("\n=== RESULTADO DA ANÁLISE ===")
print(f"Cães atendidos: {caes_atendidos}")

if caes_atendidos < 20:
    status = "OCIOSO"
    print(f"Status: {status} ")
    print("O Pet Shop ficou ocioso esta semana.")
    print(f"Faltaram {20 - caes_atendidos} cães para atingir a capacidade mínima.")
    
elif caes_atendidos >= 20 and caes_atendidos <= 30:
    status = "NORMAL"
    print(f"Status: {status}")
    print("Parabéns! O Pet Shop está funcionando dentro da capacidade ideal.")
    if caes_atendidos == 30:
        print("Você atingiu a capacidade máxima!")
    else:
        print(f"Ainda pode atender mais {30 - caes_atendidos} cães esta semana.")
        
else: 
    status = "ALTA DEMANDA"
    excesso = caes_atendidos - 30
    print(f"Status: {status}")
    print("O Pet Shop teve alta demanda esta semana!")
    print(f"{excesso} clientes não puderam ser atendidos.")

print(f"\n=== RESUMO ===")
print(f"Cães atendidos: {caes_atendidos}")
print(f"Situação: {status}")

#4
valor1 = int(input("Digite o primeior valor(inteiro): "))
valor2 = int(input("Digite o segundo valor(inteiro): "))

if valor1 > valor2:
    maior = valor1
    menor = valor2
    
elif valor1 < valor2:
    maior = valor2
    menor = valor1
   
else:
    maior = valor1
    menor = valor2

diferenca = maior - menor

print(f"A diferença do maior {maior} para o menor {menor} foi de {diferenca}")

#5
'''
A escola “APRENDER” faz o pagamento de seus professores por hora/aula. Faça um
algoritmo que calcule e exiba o salário de um professor. Sabe-se que o valor da hora/aula
segue a tabela abaixo: Professor Nível 1 R$12,00 por hora/aula Professor Nível 2 R$17,00
por hora/aula Professor Nível 3 R$25,00 por hora/aula.
'''
print("SALARIO PROFESSOR")
print("TABELA DE VALORES POR HORA/AULA:")
print("Nível 1: R$ 12,00 por hora/aula")
print("Nível 2: R$ 17,00 por hora/aula") 
print("Nível 3: R$ 25,00 por hora/aula")

nome_professor = input("Digite o nome do professor: ")
nivel = int(input("Digite o nível do professor (1, 2 ou 3): "))
horas_trabalhadas = float(input("Digite o número de horas/aula trabalhadas: "))

if horas_trabalhadas < 0:
    print("ERRO: O número de horas não pode ser negativo!")
    horas_trabalhadas = 0 

if nivel == 1:
    valor_hora = 12.00
    descricao_nivel = "Nível 1"
elif nivel == 2:
    valor_hora = 17.00
    descricao_nivel = "Nível 2"
elif nivel == 3:
    valor_hora = 25.00
    descricao_nivel = "Nível 3"
else:
    print("ERRO: Nível inválido! Use apenas 1, 2 ou 3.")
    valor_hora = 0
    descricao_nivel = "Inválido"

if valor_hora > 0 and horas_trabalhadas >= 0:
    salario = horas_trabalhadas * valor_hora

print(f"Professor: {nome_professor}")
print(f"Nível: {descricao_nivel}")
print(f"Valor da hora/aula: R$ {valor_hora:.2f}")
print(f"Horas trabalhadas: {horas_trabalhadas}")
print(f"SALÁRIO TOTAL: R$ {salario:.2f}")