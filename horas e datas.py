import datetime

datahoje= datetime.datetime.now()
dataontem= datahoje - datetime.timedelta(days=1)
dataamanha= datahoje + datetime.timedelta(days=1)
print('Hoje:', datahoje.strftime("%d/%m/%Y"))
print('Ontem:', dataontem.strftime("%d/%m/%Y"))
print('Amanha:',dataamanha.strftime("%d/%m/%Y"))
hoje=datahoje.strftime('%d/%m/%Y')
ontem=dataontem.strftime("%d/%m/%Y")

print("\n\n")
print("__"*80)
print(f'''
Bom dia!

este é o teste do dia {hoje}, obrigado até aqui!


Ah !! e só para você saber, ontem foi {ontem}.

''')