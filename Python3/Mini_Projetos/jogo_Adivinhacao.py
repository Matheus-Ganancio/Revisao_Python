# Jogo de adivinhação de números

# importa da documentação do python o random
import random

# gera um numero aleatorio inteiro, random para gerar algo aleatorio, randint faz
# a referencia que o que tá no aleatório são numeros
numero_secreto = random.randint(1, 10)

# criando loop de tentativas

tentativas = 0
acertou = False

while not acertou:
    palpite = int(input("Adivinhe o número entre 1 e 10: "))
    tentativas += 1

    if palpite == numero_secreto:
        print(f"Parabéns, você acertou em {tentativas} tentativas")
        acertou = True

    else:
        print("Errado! tente novamente")

        if palpite < numero_secreto:
            print("O número é maior!")
        elif palpite > numero_secreto:
            print("O número é menor!")
        else:
            print(f"Parabéns, você acertou em {tentativas} tentativas")
            acertou = True