from datetime import datetime

from datetime import date
data=datetime.now()
datahoje=data.strftime('%d/%m/%Y %H:%M')
print(datahoje)
dia=int(data.strftime('%d'))
diaant=dia-1
dataontem=data.strftime('/%m/%Y')
print(diaant,dataontem)

#teste item por item
diah=data.strftime('%d')
mesh=data.strftime('%m')
anosh=data.strftime('%Y')
print(f'O dia de hoje é {diah}, do mes {mesh}, do ano de {anosh}. \n O dia de ontem é {diaant}, do mes {mesh} do ano de {anosh}')
print( f'Hoje: {diah}/{mesh}/{anosh}\nOntem: {diaant}/{mesh}/{anosh}')

#teste datadelta
'''
Não deu certo usando o from datetime import date time
apenas o importe datetime


print("-"*30)
z=data.strftime('%d/%m/%Y')
print(f' Hoje: {z}')
dataanterior=timedelta(-1)
y=dataanterior.strftime('%d/%m/%Y')
print(f' Ontem: {y}')
'''