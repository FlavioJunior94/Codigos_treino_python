#função na função
def funcao (num):
    num=str(num)
    tam=len(num)
    print('*','-'*tam,'*')
    print('|',num,'|')
    print('*','-' * tam,'*')
def funcao2 (num):
    num=int(num)
    x=num*2
    return(x)

n=funcao2(input("n: "))
funcao(n)

