import random


def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if(nivel == 1):
        tentativas = 6
    elif(nivel == 2):
        tentativas = 5
    else:
        tentativas = 4

    for rodada in range(1, tentativas + 1):
        print("Tentativa {} de {}.".format(rodada, tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if(acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute) * nivel
            pontos = pontos - pontos_perdidos
            if(rodada == tentativas):
                print("O número secreto era {}. Você fez {} pontos.".format(numero_secreto, pontos))

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()