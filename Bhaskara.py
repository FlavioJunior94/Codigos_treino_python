from tkinter import *
bb=int(0)
x1=int(0)
x2=int(0)
def but():
    va=float(a.get())
    vb=float(b.get())
    vc=float(c.get())
    n1 = 4*va*vc
    n2 = (vb)**2
    n3 = 2 * va
    n4 = (n2) - (n1)
    raiz = (n4 ** (1 / 2))
    bb = -1 * vb
    x1 = (bb + raiz) / n3
    x2 = (bb - raiz) / n3
    texto_final["text"]=f'x1= {x1:.2f} e x2= {x2 :.2f}'
janela = Tk()
janela.title("Calculadora de bhaskara.")
janela.geometry("400x400")
janela.configure(background="#dde")
text_inicio=Label(janela,font="Arial",text="Digite os valores")
text_inicio.grid(column=0,row=0,padx=20,pady=20)

text_a=Label(janela, text="digite valor de a: ")
text_a.grid(column=0,row=1,padx=20,pady=5)
a=Entry(janela)
a.grid(column=1,row=1)
text_b=Label(janela, text="digite valor de b: ")
text_b.grid(column=0,row=2,padx=20,pady=5)
b=Entry(janela)
b.grid(column=1,row=2)
text_c=Label(janela, text="digite valor de c: ")
text_c.grid(column=0,row=3,padx=20,pady=5)
c=Entry(janela)
c.grid(column=1,row=3)


botao= Button(janela, text="Resolver", command=but)
botao.grid(column=0,row=4,padx=20,pady=20)


texto_final = Label(janela, text="")
texto_final.grid(column=1, row=4,padx=20,pady=20)
text_rodape=Label(janela, text="este programa foi desenvolvido por:\nFlavio dos Santos Junior")
text_rodape.grid(column=0,row=5,padx=20,pady=20)
janela.mainloop()