def quer_continuar():
    while True:
        choose = input("Quer virar mais uma carta? (S/N) ").upper()
        if choose == 'S':
            return True
        elif choose == 'N':
            return False
        else:
            print('Opção inválida!')

def convert_carta_in_value(carta):
    try:
        n = int(carta)
    except:
        if carta == 'A':
            return 1
        elif carta in 'JQK':
            return 10
    else:
        return n