
'''Faça um código que pergunte uma nota. 
 O código só pode aceitar notas entre 0 e 10 e deve continuar 
 perguntando caso seja digitado um valor fora desse intervalo '''
while True: 
    nota = int(input("Digite uma nota: "))

    if not 0 < nota <= 10:
        print("Digite uma nota entre 0 e 10. Tente novamente.")
        continue
    else:
        print(f"A nota digitada foi igual a {nota}")
        break

        '''Usando laços de repetição faça um programa que leia as notas C1 e C2 de 10 alunos
          e imprima as médias para cada aluno lido e conte quantos possuem média 
          acima de 7.'''

contador = 0 
aluno = 1

for aluno in range(1,11):
    print(f"Nota do aluno {aluno}")
    c1 = float(input("Digite a nota c1: "))
    c2 = float(input("Digite a nota c2: "))
    print('----------------')
    media = (c1 + c2) / 2
    print(f"A média do aluno {aluno} foi: {media}")
    print('----------------')


    if media > 7:
        contador += 1
        
        print(f"Total de alunos que ficaram acima da média: {contador}")



