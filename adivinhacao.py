print("*********************************")
print("Bem vindo ao jogo da adivinhação!")
print("*********************************")

numero_secreto = 42
tentativas = 3
contador_rodada = 1

while(contador_rodada <= tentativas):
    print("Tentativa {} de {}".format(contador_rodada,tentativas))

    chute_str = input("digite um numero: ")

    print("Você digitou: ", chute_str)

    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior = numero_secreto < chute
    menor = numero_secreto > chute

    if(acertou):
        print("Você acertou")
    else:
        if(maior):
            print("Você errou,o chute foi maior que o número secreto")
        elif(menor):
            print("Você errou,o chute foi menor que o número secreto")

    contador_rodada = contador_rodada + 1

print("Fim de jogo")
