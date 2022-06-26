#calculadora de baskara!!
def text(titulo):
    tam=len(titulo)
    print(' ','-'*tam)
    print('|',titulo,'|')
    print(' ','-'*tam)
def espacamento(msg):
    print()
    print(msg)
    print()
text('calculadora de Bhaskara')
while True:
    try:
        a=0
        b=0
        n1=0
        n2=0
        n3=0
        n4=0
        raiz=0
        x1=0
        x2=0
        bb=0
        a=float(input("Digite o valor de a: "))
        b = float(input("Digite o valor de b: "))
        c = float(input("Digite o valor de c: "))
        n1=4*a*c
        n2=(b)**2
        n3=2*a
        n4=(n2)-(n1)
        raiz=(n4**(1/2))
        bb=-1*b
        x1=(bb+raiz)/n3
        x2=(bb-raiz)/n3
        print()
        text('O resultado é x1= {} e x2= {}'.format(x1,x2))
        print()
        print('digite novos valores:')
        print()
        #para teste
        #print(n1,' ', n2,' ', n3,' ', n4,' ', raiz,' ', bb ,' ', x1,' ',x2)
    except ValueError:
        espacamento('Valores invalidos, tente novamente.')
    except ZeroDivisionError:
        espacamento('Erro de divisão por zero. confira seus dados e tente novamente')
    continue

