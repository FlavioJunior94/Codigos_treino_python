frase = input('Digite o que você quer criptografar: ') #MANDA O USUARIO DIGITAR A MENSAGEM.
chave = '3574402' #CHAVE ESCOLHIDA (MINHA RU)
frasecodificada=[] #LISTA PARA SALVAR CADA CARACTER CODIFICADO
i = 0
while i < len(frase): #LOOP PARA RODAR O NUMERO DE VEZES O TAMANHO DA FRASE E TROCAR OS CARACTERES.
    c_frase = ord(frase[i])#FUNÇÃO ORD RETORNA O VALOR DO CARACTER ASCII
    c_chave = ord(chave[i % len(chave)]) #O CALCULO PARA OS VALORES DA CHAVE
    frasecodificada.append(chr(c_frase ^ c_chave)) #SUBSTITUI O CARACTER E ADICIONA NA LISTA
    i += 1 #CONDIÇÃO DO LOOP.
print("\nPalavra criptografada: ")
print(*frasecodificada, sep='') #IMPRIME A LISTA, OU SEJA, A NOVA PALAVRA OU FRASE, CODIFICADA.
