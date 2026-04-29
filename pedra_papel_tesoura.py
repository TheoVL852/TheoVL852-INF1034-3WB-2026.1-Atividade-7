import random

ponto_computador = 0
ponto_jogador = 0
jogada = 0
jogada_comp = 0

def jogadorganha():
    print('-----> Jogador ganha')
    print(f'Computador: {ponto_computador}')
    print(f'Jogador: {ponto_jogador}')

def computadorganha():
    print('-----> Computador ganha')
    print(f'Computador: {ponto_computador}')
    print(f'Jogador: {ponto_jogador}')

def empate():
    print('-----> Empate')
    print(f'Computador: {ponto_computador}')
    print(f'Jogador: {ponto_jogador}')

print('=====-INICIO DO JOGO-=====')
print('Pedra = 1 / Papel = 2 / Tesoura = 3')

while 3>=jogada>=0:
    jogada = int(input('Sua jogada: '))
    jogada_comp = random.randint(1,3)
    print(f'Jogada do Computador: {jogada_comp}')
    #pedra
    if jogada == 1 and jogada_comp == 2:
        ponto_computador+=1
        computadorganha()
    elif jogada == 1 and jogada_comp == 3:
        ponto_jogador+=1
        jogadorganha()
    elif jogada == 1 and jogada_comp == 1:
        empate()
    #papel
    elif jogada == 2 and jogada_comp == 1:
        ponto_jogador+=1
        jogadorganha()
    elif jogada == 2 and jogada_comp == 3:
        ponto_computador+=1
        computadorganha()
    elif jogada == 2 and jogada_comp == 2:
        empate()
    #tesoura
    elif jogada == 3 and jogada_comp == 1:
        ponto_computador+=1
        computadorganha()
    elif jogada == 3 and jogada_comp == 2:
        ponto_jogador+=1
        jogadorganha()
    else:
        empate()
    print('='*30)

print('=== Fim de jogo ===')
if ponto_computador>ponto_jogador:
    print(f'Computador ({ponto_computador}) ganhou do Jogador ({ponto_jogador})')
elif ponto_jogador>ponto_computador:
    print(f'Jogador ({ponto_jogador}) ganhou do Computador ({ponto_computador})')
else:
    print('O jogo empatou')
