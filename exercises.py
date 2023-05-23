"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
entrada = input("Digite um número: ")

if entrada.isdigit():  #isdigit verifica se há apenas números
    entrada_int = int(entrada)
    par_ou_impar = entrada_int % 2 == 0
    par_impar_txt = 'ímpar' #defini q a variável sempre será ímpar

    if par_ou_impar:
        par_impar_txt = 'par'
    print(f"O número digitado foi {par_impar_txt}")



else:
    print("você não digitou um número inteiro.")
"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = int(input("Digite a hora: "))

if hora >= 0 and hora < 11:
    print("Bom dia!")

elif hora >= 12 and hora < 17:
    print("Boa tarde!")

elif hora >= 18 and hora < 23:
    print("Boa noite!")

else:
    print("Número não conhecido.")







"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input("digite seu nome: ")
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print("your name is short")

    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print("your name is normal")

    else:
        print("your name is very long")

else:
 print("type one more letter")

 #peça ao usuário 5 notas e faça a média delas


#tabuada de 7 usando loop while

numero1 = 7
i2 = 1
tabuada7 = numero1 * i2
while i2 <= 10:
    print(f"{numero1} x {i2} = {tabuada7}")
    i2 += 1   