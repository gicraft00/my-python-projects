import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Digite o número: (entre 1 e 100): "))
    tentativas += 1  # Incrementa o número de tentativas

    if tentativa == numero_secreto:
        print(f"Parabéns! Você adivinhou o número em {tentativas} tentativas.")
        break
    elif tentativa < numero_secreto:
        print("O número secreto é maior.")
    else:
        print("O número secreto é menor.")