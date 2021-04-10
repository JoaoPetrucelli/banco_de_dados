def AbrirBanco():
    Banco = open("banco.txt", "r")
    Abrir = Banco.read()
    sla = Abrir.split("\n")
    return sla



def registrar(DataBank):
    while True:
        usuario = input("Crie seu usuário")
        if usuario in DataBank:
            print("Esse usuario já existe, tente novamente")
            continue

        elif len(usuario) < 4:
            print("seu usuario é menor do que o pau do phelipe, tente novamente")


        if usuario in DataBank:
            Continuar = input("Deseja tentar novamente? Sim(1) Não(2)")
            if Continuar == 1:
                continue
            if Continuar == 2:
                break

        senha = input("Crie sua senha")
        if len(senha) > 16:
            print("sua senha é grande demais, tente novamente")
            continue


        pin = input("Escolha seu pin")
        if len(pin) < 4:
            print("seu pin é muito pequeno, tente novamente")

        elif len(pin) > 16:
            print("seu pin é muito grande, tente novamente")

        Banco = open("banco.txt","a")
        Banco.write(f"{usuario}\n{senha}\n{pin}\n")

        print("seu registro foi conclúido")

        if pin in DataBank:
            print("esse pin já existe, tente novamente")
        break

        Banco = open("banco.txt", "a")
        Banco.write(f"{usuario}\n{senha}\n{pin}\n")
        Banco.close()
        print("sua conta foi registrada")
        break



def logar(DataBank):
    while True:
        usuario2 = input("Qual o seu usuario?")
        senha2 = input("Qual a sua senha?")



        if usuario2 in DataBank:
            descobrir = DataBank.index(usuario2) + 1
            if DataBank[descobrir] == senha2:
                print("seu login foi feito")
                break
            else:
                pergunta = input("sua senha está incorreta, deseja tentar novamente?")
                if pergunta == "sim":
                    continue
                else:
                    break

        else:
            pergunta2 = input("seu usuário não existe, deseja tenta novamente?")
            if pergunta2 == "sim":
                continue
            else:
                break



while True:
    naosei = AbrirBanco()

    escolha = input("Registrar (1), Logar (2) Sair (3)")

    if escolha == "1":
        registrar(naosei)
        continue

    elif escolha == "2":
        logar(naosei)

    elif escolha == "3":
        exit()


print("hello world")

