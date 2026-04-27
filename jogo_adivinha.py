# JOGO DE ADIVINHAÇÃO

import random

funcao = input('Quem tentará adivinhar (usuario ou computador) ? : ')

#USUARIO TENTA ADIVINHAR

if funcao == 'usuario':

    numero_adivinha = random.randint(1,1023)
    tentativa = 0
    num=int(input('Numero (entre 1 e 1023): '))

    while num!=numero_adivinha:
        if num>numero_adivinha:
            print('-1')
            tentativa+=1
            num=int(input('Numero: '))
        elif num<numero_adivinha:
            print('1')
            tentativa+=1
            num=int(input('Numero: '))

    if num==numero_adivinha:        
        tentativa+=1
        print('0')
        print(f'Parabéns, o número era {numero_adivinha}, você achou em {tentativa} tentativas')

# COMPUTADOR TENTA ADIVINHAR

if funcao == 'computador':

    numero_adivinha = int(input('Insira um número entre 1 e 1023: '))
    tentativa = 0 
    num_maior = 1023
    num_menor = 1
    num = random.randint(num_menor,num_maior)
    maior_menor = 0
    while num!=numero_adivinha:
        if num>numero_adivinha:
            tentativa+=1
            maior_menor==-1
        elif num<numero_adivinha:
            tentativa+=1
            maior_menor==1

    
        if maior_menor==-1:
            num_maior=num
            num=random.randint(num_menor,num_maior)  
        elif maior_menor==1:
            num_menor=num
            num=random.randint(num_menor,num_maior)
           
        

    if num==numero_adivinha:        
        tentativa+=1
        print(f'O número era {numero_adivinha}, o computador achou em {tentativa} tentativas')

