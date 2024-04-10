num = [0,0,0,0,0] #Lista vazia criada, pois sei a quantidade de posições que serão armazenadas
x = 0             #Variável criada para servir de apoio para o looping e para as posições dentro da lista conforme o valor que for recebendo
while x < len(num): #"len()" ler o tamanho da lista, quantidade de posições
    num[x] = int(input(f"\nInsira o {x+1}º número positivo: ")) #CUIDADO com "num(x)", quando for usar lista é sempre com "[]"

    #Condição para evitar o input de números negativos, caso positivo irá prosseguir
    if num[x] < 0:
        num[x] == 0
        print(f"\nErro ! Insira um número positivo !\n")
    else:
        x+=1

print(f"\nOs números informados são: {num}")
#Quero o print da lista ordenada
num.sort()
print(f"\nOs números de forma ordenada: {num}")
#Quero o print da lista ordenada inversamente
num.reverse()
print(f"\nOs números de forma inversamente ordenada: {num}")
#Quero o tamanho da lista
print(f"\nO tamanho da lista dos números informados é: {len(num)}")
#Quero o menor valor
print(f"\nO menor valor é: {min(num)}")
#Quero o maior valor
print(f"\nO maior valor é: {max(num)}")
#Quero a soma de todos os valores
print(f"\nA soma dos valores inseridos é: {sum(num)}\n")