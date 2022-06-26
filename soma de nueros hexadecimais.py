num = input('Digite seu numero hexagonal: ')
x = int(num, 16)
num2 = input('Digite seu numero hexagonal: ')
y = int(num2, 16)

soma=x+y
print(f"a soma dos numeros hexadecimais é de {hex(soma)[2:]}")
