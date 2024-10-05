import random
import os
ocultar = False
do = int(input('Okay. Quero que começa do: '))
ate = int(input('Até o: '))
sequencia = 0
sequenciaMax = 0
os.system('cls') #limpar console

modoNumero = input('Modo número S ou N? ')

if modoNumero == "s":
    while(True):
        n = random.randint(do,ate)
        nd = random.randint(1,10)
        if ocultar == False:
            print(f'{n}{nd} {n * nd}')
        a = input(f' {n}{nd} ')

        if a == "e":
            print('TOGGLE Exibindo respostas')
            ocultar = not ocultar #inverte
        else:
            a = int(a)
            os.system('cls') #limpar console
            if a == n * nd:
                sequencia += 1
                if sequencia > sequenciaMax:
                    sequenciaMax = sequencia
                print(f'Correto! Sequência de acertos: {sequencia}, Sequência máxima foi: {sequenciaMax}')
                print("==============")
            else:
                sequencia = 0
                print("==============")
                print("==============")
                print("==============")
                print("==============")
                print(f'Errado! {n}{nd} {n * nd}')
                print("==============")
                print("==============")
                print("==============")
                print("==============")
else:
    while(True):
        n = random.randint(do,ate)
        nd = random.randint(1,10)
        if ocultar == False:
            print(f'{n} * {nd} = {n}{nd} {n * nd}')
        a = input(f' {n} * {nd} = ')

        if a == "e":
            print('TOGGLE Exibindo respostas')
            ocultar = not ocultar #inverte
        else:
            a = int(a)
            os.system('cls') #limpar console
            if a == n * nd:
                sequencia += 1
                if sequencia > sequenciaMax:
                    sequenciaMax = sequencia
                print(f'Correto! Sequência de acertos: {sequencia}, Sequência máxima foi: {sequenciaMax}')
                print("==============")
            else:
                sequencia = 0
                print("==============")
                print("==============")
                print("==============")
                print("==============")
                print(f'Errado! {n} * {nd} = {n * nd}')
                print("==============")
                print("==============")
                print("==============")
                print("==============")