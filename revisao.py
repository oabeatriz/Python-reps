# Faça um programa que peça ao usuário para digitar um número e imprima se o número é par ou ímpar

entrada = int(input("Digite um número: "))
verificador = (entrada % 2) == 0

if entrada and verificador == True:
  print('par')
else:
  print('ímpar')
  



# Faça um programa que peça ao usuário para digitar um número e imprima se o número é positivo, negativo ou zero

entrada2 = float(input("Digite um número: "))

if entrada2 > 0:
  print(f"{entrada2} é positivo")
elif entrada2 < 0:
  print(f"{entrada2} é negativo")
else:
  print(f"{entrada2} é igual a zero.")


#Faça um programa que peça ao usuário para digitar a sua idade e imprima se ele é menor ou maior de idade

idade = int(input("Digite sua idade: "))

if idade >= 18:
  print("É maior de idade.")
else:
  print("É menor de idade.")

#Faça um programa que peça ao usuário para digitar o seu nome e a sua idade e imprima se ele pode ou não dirigir

pode_ou_nao_nome = input("Digite seu nome: ") 
pode_ou_nao_idade = int(input("Digite sua idade: "))

if pode_ou_nao_idade >= 18:
  print(f" {pode_ou_nao_nome} pode dirigir!")
else:
  print(f"{pode_ou_nao_nome} não pode dirigir!")

#Faça um programa que peça ao usuário para digitar a sua nota e imprima se ele foi aprovado (nota maior ou igual a 7) ou reprovado (nota menor que 7)

nota = float(input("Digite sua nota: "))

if nota >= 7:
  print("Aprovado!")
else: 
  print("Reprovado!")

#Faça um programa que peça ao usuário para digitar o seu salário e imprima se ele deve ou não pagar imposto de renda (salário maior que R$ 1.903,98)

salario = float(input("Digite seu salário: "))

if salario >= 1903.98:
  print("Deve pagar o imposto!")
else:
  print("Não precisa pagar imposto!")

#Faça um programa que peça ao usuário para digitar dois números e imprima o maior deles.

numero_1 = int(input("Digite um número: "))
numero_2 = int(input("Digite outro número: "))
numero_3 = int(input("Digite outro número: "))

if numero_1 > numero_2 and numero_1 > numero_3:
  print(f"{numero_1} é maior que todos.")
elif numero_2 > numero_1 and numero_2 > numero_3:
  print(f"{numero_2} é maior que todos.")
elif numero_3 > numero_1 and numero_3 > numero_2:
  print(f"{numero_3} é maior que todos")
else:
  print("são todos iguais")
print('----------------------')


#Loop while: Faça um programa que imprima os números pares de 0 a 10.

for i in range(2,11,2):
    print(i)
print('-----------------')
#. Loop for: Faça um programa que imprima os números ímpares de 1 a 9

for u in range(1,9,2):
  print(u)
print('--------------------------')

# Loop while: Faça um programa que imprima a sequência de Fibonacci até o décimo termo

#screva um programa que peça ao usuário para digitar uma senha. Enquanto a senha digitada não for "senha123", o programa deve continuar pedindo que o usuário digite a senha

tentativa = True

while tentativa:
  senha = input("Digite sua senha: ")

  if senha == 'senha123':
    break
  

  else:
    print("Você digitou campos vazios.")
print("Login feito com sucesso")