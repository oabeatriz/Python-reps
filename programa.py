def obter_nota(numero_nota):  #def é a criação de uma function
    while True:
       '''criação das funções para erros de nota'''
       nota_input = input(f"Digite a nota {numero_nota}: ")

       if nota_input == "":
            print("Erro: campo vazio. Digite uma nota válida")
            continue
       
       if not nota_input.isdigit():
            print("Erro: valor inválido. Digite uma nota numérica.")
            continue
        
       nota = float(nota_input) #declara a var "nota" em uma float padrão
     
        
       if nota >= 0 and nota <= 10:
            return nota
       

       else:
           print("Utilize números de 1 a 10.")


soma_notas = 0
num_notas = int(input("Digite o número de notas que deseja calcular: "))

notas_vazio = []   #declara uma list, onde insere-se a qntd de notas q o usuário deseja calcular
i = 1

while i <= num_notas: #essa linha estabelece a condição para executar o loop. enqt o valor de i for menor ou igual a num_notas, o loop continuará a ser executado, isso garante que o número correto de notas seja solicitado ao usuário
    nota = obter_nota(i) #chamamos a função obter_nota() para obter a nota do usuário, o argumento i é passado para a função para que possamos exibir a mensagem correta solicitando a nota correspondente ao número da iteração atual
    soma_notas += nota
    i += 1 #condição p repetição

media = soma_notas / num_notas
print(f"A média das notas é igual a: {media}")
    

if media >= 7:
    print("Aprovado! Parabéns!")
else:
    print("Reprovado.")




