import tkinter as tk
#Criando função para Mostrar
def somar():
    numero1=int(e1.get())
    numero2=int(e2.get())
    resultado=numero1+numero2
    print(resultado)
def sub():
    numero1=int(e1.get())
    numero2=int(e2.get())
    resultado=numero1-numero2
    print(resultado)
def mult():
    numero1=int(e1.get())
    numero2=int(e2.get())
    resultado=numero1*numero2
    print(resultado)
def div():
    numero1=int(e1.get())
    numero2=int(e2.get())
    resultado=numero1/numero2
    print(resultado)
#Instanciando o TK
janela=tk.Tk()
#Construindo Label
tk.Label(janela,text="Insira o Primeiro número:").grid(row=0)
tk.Label(janela,text="Insira o Segundo Número:").grid(row=1)

#Construindo entradas
e1=tk.Entry(janela)
e2=tk.Entry(janela)

#Configurações no Label
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
#Criado Botões
tk.Button(janela,text="Quit",command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela,text="Somar",command=somar).grid(row=3,column=1,sticky=tk.W,pady=0)
tk.Button(janela,text="Subtrair",command=sub).grid(row=3,column=2,sticky=tk.W,pady=0)
tk.Button(janela,text="Multiplicar",command=mult).grid(row=3,column=3,sticky=tk.W,pady=0)
tk.Button(janela,text="Dividir",command=div).grid(row=3,column=4,sticky=tk.E,pady=0)
#Executando Aplicação
janela.mainloop()
