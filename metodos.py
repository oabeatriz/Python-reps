#operadores in e not in
nome = "beatriz"
print('b' in nome) #retorna True
print('y' in nome) #retorna False
print('y' not in nome) #retorna True
print('b' not in nome) #retorna False
print(10 * '-')

#fatiamento de strings

var = "olá mundo"
print(var[5]) #o numero apresenta a posição da letra
print(var[-4]) 
print(var[:5]) #fatia a string
print(len(var)) #conta a qntd de letras
print(var[0:9:1])
print(var[0:9:2])


  # Exercício :: Peça ao usuário para digitar seu nome :::::: Peça ao usuário para digitar sua idade                        Se nome e idade forem digitados:                           Exiba:          Seu nome é {nome} :::::::::::::::::::::::::::: Seu nome invertido é {nome invertido}                        Seu nome contém (ou não) espaços                             Seu nome tem {n} letras                                         A primeira letra do seu nome é {letra}                         A última letra do seu nome é {letra}                           Se nada for digitado em nome ou idade:                     exiba "Desculpe, você deixou campos vazios."





#introdução ao try e except                    try => tenta executar o código               except => ocorre algum erro ao executar

#isdigit = verifica se o usuário digitou apenas números!
numero = input("digite um número: ")
print(numero.isdigit()) #retorna True / booleano / pois digitei somente números // se o número for Float ele retorna False.

numero_str = input("digite um valor: ")

try:
  print('STR:', numero_str)
  numero_float = float(numero_str)
  print('FLOAT:', numero_float)
  
#capta o erro. é diferente de if e else
except:
  print('Não é um número')




