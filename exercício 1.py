import random

numerosJogador1 = [0,0,0]
numerosJogador2 = [0,0,0]
indice = 0 
while indice < len(numerosJogador1): 
    numerosJogador1[indice] = random.randint(1,6) 
    numerosJogador2[indice] = random.randint(1,6)
    indice +=1

#Looping para armazenar valores aleatórios na lista do jogador 1
#Variavel indice para contar de 0 até o tamanho total da lista "numerosJogador1"
#Variavel indice utilizada também para determinar a posição dentro da lista que vai ser armazenada um valor
#"random.randint()" serve para randomizar numeros de um até outro ex.: (1,99) ou (-112312,756332345)
#Looping para poder armazenar valores aleatórios na lista vazia do jogador 1, simulando uma jogada de dados

print(numerosJogador1)
print(numerosJogador2)
print(f"\nA soma dos valores do jogador 1 é igual a: {sum(numerosJogador1)}")
print(f"\nA soma dos valores do jogador 2 é igual a: {sum(numerosJogador2)}\n")

#Print na tela da soma dos valores de cada jogador

if sum(numerosJogador1) > sum(numerosJogador2):
    print(f"\nO vencedor é o Jogador 1\n")
elif sum(numerosJogador1) == sum(numerosJogador2):
    print(f"\nEmpate entre os dois jogadores\n")
else:
    print(f"\nO vencedor é o Jogador 2\n")

#Condições para determinar e printar o jogador vencedor baseado na soma dos valores aleatórios dados