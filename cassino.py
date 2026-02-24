
import random ##para que a ordem das frutas sejam aleatorias
import time ##para o tempo que as frutas fiquem em aleatoriedade

frutas = ["🍓", "🍒", "🍋", "🍉"] ##define as frutas do cassino

print("Bem vindo(a)!")

while True:  ##para que o codigo fique em loop

    play = input("Pressione Enter para jogar ou digite 'sair': ").lower() ##para que o cliente possa continuar ou sair quando quiser

    if play == "sair":
        print("Você saiu")
        break
    else:

        print("=====Cassino=====")

    s1 = s2 = s3 = ""

    for i in range(25): ##define a aleatoriedade das variaveis
        if i < 15:
            s1 = random.choice(frutas)
        if i < 20:
            s2 = random.choice(frutas)
        if i < 25:
            s3 = random.choice(frutas)
        print(f"\r   {s1} | {s2} | {s3}   ", end="", flush=True) ##onde fica as frutas
        time.sleep(0.2)

    print()

    if s1 == s2 == s3: ##se as 3 frutas forem iguais, jackpot!
        print("JACKPOT!!🎉🎉🎉")
    else:
        print("Perdeu") ##se não, perdeu
