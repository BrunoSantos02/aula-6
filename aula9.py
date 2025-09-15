'''
id_aluno = int(input("Digite o ID do aluno: "))
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = float(input("Digite a media dos exercicios: "))

MA = (nota1 + nota2 * 2 + nota3 * 3 + media ) / 7

if MA >= 9.0 and MA < 10:
    conceito = "A"
elif MA >= 7.5 and MA < 9:
    conceito = "B"
elif MA >= 6.0 and MA < 7.5:
    conceito = "C"
elif MA >= 4.0:
    conceito = "D"
else :
    conceito = "E"

if conceito == "A" or conceito == "B" or conceito == "C":
    status = "APROVADO"
else:
    status = "REPROVADO"

print("\n--- RESULTADO ---")
print(f"Número do aluno: {id_aluno}")
print(f"Notas: {nota1}, {nota2}, {nota3}")
print(f"Média dos exercícios: {media}")
print(f"Média de aproveitamento: {round(MA,2)}")
print(f"Conceito: {conceito}")
print(f"Situação: {status}")
'''
'''
a = int(input("Digite o primeiro número (a): "))
b = int(input("Digite o segundo número (b): "))

if b != 0 and a % b == 0:
    print("São múltiplos")
    print(f"{a} é múltiplo de {b}")
elif a != 0 and b % a == 0:
    print("São múltiplos")
    print(f"{b} é múltiplo de {a}")
else:
    print("Não são múltiplos")
'''
'''
n = int(input("Digite a opção 1(Crescente), 2(Decrescente) ou 3(Maior no Meio): "))
a = float(input("Digite o primeiro valor (a): "))
b = float(input("Digite o segundo valor (b): "))
c = float(input("Digite o terceiro valor (c): "))

if n == 1:
    print("Ordem crescente:")
    
    if a <= b and a <= c:  
        if b <= c:
            print(f"{a}, {b}, {c}")
        else:
            print(f"{a}, {c}, {b}")
    
    elif b <= a and b <= c:
        if a <= c:
            print(f"{b}, {a}, {c}")
        else:
            print(f"{b}, {c}, {a}")
    
    else: 
        if a <= b:
            print(f"{c}, {a}, {b}")
        else:
            print(f"{c}, {b}, {a}")

elif n == 2:
   
    print("Ordem decrescente:")

    if a >= b and a >= c:
        if b >= c:
            print(f"{a}, {b}, {c}")
        else:
            print(f"{a}, {c}, {b}")
    
    elif b >= a and b >= c: 
        if a >= c:
            print(f"{b}, {a}, {c}")
        else:
            print(f"{b}, {c}, {a}")
    
    else:
        if a >= b:
            print(f"{c}, {a}, {b}")
        else:
            print(f"{c}, {b}, {a}")

elif n == 3:
    print("Maior valor no meio:")
    
    if a >= b and a >= c:
        print(f"{b}, {a}, {c}")
    
    elif b >= a and b >= c: 
        print(f"{a}, {b}, {c}")
    
    else:
        print(f"{a}, {c}, {b}")

else:
    print("Opção inválida! Digite 1, 2 ou 3.")
'''
   
'''
print("Digite um valor em minutos para converter")

tempo_minutos = float(input("Tempo em minutos: "))

horas = int(tempo_minutos // 60) 
minutos_restantes = tempo_minutos % 60
minutos = int(minutos_restantes) 
segundos = (minutos_restantes - minutos) * 60 

print(f"\nResultado: {horas} h {minutos} min {segundos:.1f} s")
'''