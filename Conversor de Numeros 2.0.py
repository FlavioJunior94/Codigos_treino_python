while True:
    try:
        esc=int(input('\n1) DECIMAL\n2) BINARIO\n3) OCTAL\n4) HEXADECIMAL\nescolha sua BASE: '))
        if esc==1:
            num=int(input('Digite seu numero decimal: '))
            b=bin(num)
            o=oct(num)
            h=hex(num)
            print(f'\n{num} em binario: {b[2:]}\n{num} em octal: {o[2:]}\n{num} em hexagonal: {h[2:]}')
        elif esc==2:
            num = input('Digite seu numero binario: ')
            num2=int(num,2)
            o = oct(num2)
            h = hex(num2)
            print(f'\n{num} em decimal: {num2}\n{num} em octal: {o[2:]}\n{num} em hexagonal: {h[2:]}')
        elif esc==3:
            num = input('Digite seu numero octal: ')
            num2=int(num,8)
            b = bin(num2)
            h = hex(num2)
            print(f'\n{num} em decimal: {num2}\n{num} em binario: {b[2:]}\n{num} em hexagonal: {h[2:]}')
        elif esc == 4:
            num = input('Digite seu numero hexagonal: ')
            num2 = int(num, 16)
            o = oct(num2)
            b = bin(num2)
            print(f'\n{num} em decimal: {num2}\n{num} em octagonal: {o[2:]}\n{num} em binario: {b[2:]}\n')
    except:
        print('\nNUMERO INVALIDO! TENTE NOVAMENTE!\n OK!!!\n ')
    print("-" * 50)