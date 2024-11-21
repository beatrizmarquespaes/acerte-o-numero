import random

# Define o número e o máximo de tentativas
numero_secreto = random.randint(1, 10)
max_tentativas = 3
tentativas = 0

print("Estou pensando em um número entre 1 e 10.")

# Loop de tentativas
while tentativas < max_tentativas:
    palpite = int(input("Qual é o seu palpite? "))

    # Verifica se o palpite está correto ou não
    if palpite < numero_secreto:
        print("O número que estou pensando é maior que o seu palpite.")
    elif palpite > numero_secreto:
        print("O número que estou pensando é menor que o seu palpite.")
    else:
        print(f"Parabéns! Você acertou o número secreto, que era {numero_secreto}.")
        break

    tentativas += 1

# Se o número máximo de tentativas tenha acabado
if tentativas == max_tentativas:
    print(f"Suas {max_tentativas} tentativas acabaram. O número secreto era {numero_secreto}.")