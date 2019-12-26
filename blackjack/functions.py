def quer_continuar():
    while True:
        choose = input("Quer virar mais uma carta? (S/N) ").upper()
        if choose == 'S':
            return True
        elif choose == 'N':
            return False
        else:
            print('Opção inválida!')
