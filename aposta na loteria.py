aposta1=float(input('aposta 1: '))
aposta2=float(input('aposta 2: '))
aposta3=float(input('aposta 3: '))
totalapst=aposta3+aposta2+aposta1
pct1=(100*aposta1)/totalapst

2=(100*aposta2)/totalapst
pct3=(100*aposta3)/totalapst
premio=float(input('Valor do premio é de : '))
rec1=(premio*pct1)/100
rec2=(premio*pct2)/100
rec3=(premio*pct3)/100
print("O valor a receber é de:")
print('Apostador 1: {:.2f}'.format(rec1))
print('Apostador 2: {:.2f}'.format(rec2))
print('Apostador 3: {:.2f}'.format(rec3))
#print(f'valor da porcentagem de cada um: 1={pct1} 2={pct2} 3={pct3}')