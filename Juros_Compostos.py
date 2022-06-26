#M = C . (1 + i)n
#=float(input(" Montante: "))
c=float(input(" Capital: "))
i=float(input(" taxa: "))
n=int(input(" periodo: "))
i=i/100
m=c*((1+i)**n)
print(f"Valor total: {m:.2f}\nLucro: {m-c:.2f}")