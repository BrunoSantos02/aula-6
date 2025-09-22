print("=== POSTO DE COMBUSTÍVEL ===")

preco_gasolina = 5.15
preco_alcool = 4.29

print("PREÇOS BASE:")
print(f"Gasolina: R$ {preco_gasolina:.2f} por litro")
print(f"Álcool: R$ {preco_alcool:.2f} por litro")
print("\n TABELA DE DESCONTOS:")
print("ÁLCOOL:")
print("  • Até 20 litros: 3% de desconto")
print("  • Acima de 20 litros: 5% de desconto")
print("GASOLINA:")
print("  • Até 20 litros: 4% de desconto")
print("  • Acima de 20 litros: 6% de desconto")

litros = float(input("Digite a quantidade de litros: "))
tipo_combustivel = input("Digite o tipo de combustível (A-álcool, G-gasolina): ").upper()

if litros <= 0:
    print(" ERRO: A quantidade de litros deve ser maior que zero!")
    litros = 0

if tipo_combustivel == "A":  
    nome_combustivel = "Álcool"
    preco_por_litro = preco_alcool
    
    if litros <= 20:
        desconto_percentual = 3
    else:
        desconto_percentual = 5
        
elif tipo_combustivel == "G": 
    nome_combustivel = "Gasolina"
    preco_por_litro = preco_gasolina
    
    if litros <= 20:
        desconto_percentual = 4
    else:
        desconto_percentual = 6
        
else:  
    print("ERRO: Tipo de combustível inválido! Use 'A' para álcool ou 'G' para gasolina.")
    nome_combustivel = "Inválido"
    preco_por_litro = 0
    desconto_percentual = 0

if preco_por_litro > 0 and litros > 0:

    valor_sem_desconto = litros * preco_por_litro

    valor_desconto = valor_sem_desconto * (desconto_percentual / 100)
    
    valor_a_pagar = valor_sem_desconto - valor_desconto
    
    print(f"\n=== NOTA FISCAL ===")
    print(f"Combustível: {nome_combustivel}")
    print(f"Quantidade: {litros} litros")
    print(f"Preço por litro: R$ {preco_por_litro:.2f}")
    print(f"Valor sem desconto: R$ {valor_sem_desconto:.2f}")
    print(f"Desconto aplicado: {desconto_percentual}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"VALOR A PAGAR: R$ {valor_a_pagar:.2f}")
    
else:
    print(" Não foi possível calcular o valor devido a dados inválidos.")