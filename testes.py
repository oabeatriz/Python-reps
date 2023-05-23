'''exemplo de programa de tentativas com while'''

senhasalva = '123'
senha = ''
repeticao = 0

while senhasalva != senha:
    senhasalva = input(f"tentativa número({repeticao}): ")

    repeticao += 1
   


valor = 1
while valor < 30:
    valor = valor * 5 
    
    '''O código começa com x igual a 1 e, em seguida, entra em um loop while. O loop continuará enquanto x for menor que 30.
      A cada iteração, o valor de x é multiplicado por 5.

Vamos percorrer as iterações do loop:

Iteração inicial: x é igual a 1.

x é multiplicado por 5: x = 1 * 5 = 5.
O loop continua porque 5 é menor que 30.
Segunda iteração: x é igual a 5.

x é multiplicado por 5: x = 5 * 5 = 25.
O loop continua porque 25 é menor que 30.
Terceira iteração: x é igual a 25.

x é multiplicado por 5: x = 25 * 5 = 125.
O loop continua porque 125 é maior que 30.
Portanto, o loop não será executado novamente e a última atribuição de x é 125.

O valor final de x é 125.'''