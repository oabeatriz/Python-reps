contador  =  0

while contador <= 100:
    contador += 1
    if contador == 6:
        print('nao mostro o 6')
        continue
    if contador >= 10 and contador <= 27:
        print('off')
        continue
    print(contador)

    if contador == 30:
        break
    


""""" media de notas "" """
y = 1
soma = 0

while y <= 5:
    nota = float(input(f"Informe a {y} nota: "))
    soma += nota  #soma += nota vai somar as notas em 5 (nota + nota + nota + nota ..etc)
    y += 1 #vai gerar a 1, 2, 3 , 4 e 5 nota
    

media = soma / 5  #a media deve estar paralela alinhada ao while

print(f"a média é igual a {media}")





""" Calculadora com while """

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos.')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('Operador inválido.')
        continue  #continue vai retornar a ação

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print("realizando sua conta... confira o resultado abaixo:")

    if operador == '+':
        print(num_1_float + num_2_float)

    elif operador == '-':
        print(num_1_float - num_2_float)

    elif operador == '*':
        print(num_1_float * num_2_float)

    elif operador == '/':
        print(num_1_float / num_2_float)         

    else:
        print("Erro de servidor/cliente")


    ### sair do programa 

    sair = input('Quer sair? [s]im ou [n]ão ').lower().startswith('s')

    if sair is True:
        print("Você saiu da calculadora. Até mais!")
        break
    else:
        print("Retornando a calculadora...")
     