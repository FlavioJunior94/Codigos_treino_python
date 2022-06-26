#Cadastro de alunos, treino Sorted, lambda lista de dicionarios.
alunos=[
    {'nome':'Joao','materia':'Matematica','nota': 10},
    {'nome':'Maria','materia':'Geografia','nota': 5},
    {'nome':'Bernardo','materia':'Ingles','nota': 12},
    {'nome':'Amelia','materia':'Zoologia','nota': 8},
    {'nome':'Joana','materia':'Fisica','nota': 6},
    {'nome':'Wilian','materia':'Quimica','nota': 7},
]
while True:
    nome=input('Nome: ')
    materia=input('Materia: ')
    nota=int(input('Nota: '))
    item={'nome':nome,'materia':materia,'nota':nota}
    print('\n')
    alunos.append(item)
    i=0
    alunos=sorted(alunos, key= lambda aluno: aluno['nota'],reverse=True )
    for item in alunos:
        print(f"Nome: {alunos[i]['nome']}| Materia: {alunos[i]['materia']}| Nota: {alunos[i]['nota']}")
        print('-'*50)
        i+=1