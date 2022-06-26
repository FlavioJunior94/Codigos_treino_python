print('Confira se é palindromo.\n\n ')
while True:
    frase = input(" Digite sua frase: ")
    frase = frase.lower()
    frase = frase.replace('á', 'a')
    frase = frase.replace('é', 'e')
    frase = frase.replace('í', 'i')
    frase = frase.replace('ó', 'o')
    frase = frase.replace('ú', 'u')
    frase = frase.replace('â', 'a')
    frase = frase.replace('ê', 'e')
    frase = frase.replace('î', 'i')
    frase = frase.replace('ô', 'o')
    frase = frase.replace('û', 'u')
    tamfrase=len(frase)
    lista1=[]
    lista2=[]
    for i in range (0,tamfrase):
        if frase[i]!=' ' and frase[i]!='.' and frase[i]!='?' and frase[i]!='!' and frase[i]!='/'and frase[i]!='-':
            lista1.append(frase[i])
    for i in range (tamfrase-1,-1,-1):
    	if frase[i]!=' ' and frase[i]!='.' and frase[i]!='?' and frase[i]!='!' and frase[i]!='/'and frase[i]!='-':
    	    lista2.append(frase[i])

    #print('{}\n{}'.format(lista1,lista2))
    if (lista1==lista2):
    	print('\nÉ um palindromo!\n')
    else:
    	print('\nNão é um palindromo!\n')