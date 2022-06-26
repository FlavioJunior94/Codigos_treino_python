nome=input("Digite o nome: ")
salario=float(input("Digite o salario: "))
if(salario<=1903.98):
    aliquota=0
elif(salario>1903.98 and salario<=2826.65):
    aliquota=7.50
elif(salario>2826.65 and salario<=3751.03):
    aliquota=15.00
elif(salario>3751.03 and salario<=4664.68):
    aliquota=22.50
else:
    aliquota=27.50
x=(salario*aliquota)/100
print('\n\nDados do Funcionario:\n')
print(f'Nome do Funcionario: {nome}\nAliquota: {aliquota:.2f}%\nO valor a ser deduzido do salario: {x:.2f}')