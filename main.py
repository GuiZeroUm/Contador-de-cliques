import tkinter as tk

root = tk.Tk()

root.geometry('600x600') #mudando o tamanho da janela
root.title ('Contador de clicks') #mudando o titulo do app
root.configure (background='#1d1d1d') #adicionando cor de fundo

numero = 0

def acrescentar():
    global numero
    numero+= 1
    contando__as__botada.configure(text=numero)

def diminuir():
    global numero
    numero-= 1
    contando__as__botada.configure(text=numero)

margem = tk.Canvas(root, height=300, background='#1d1d1d', highlightthickness=0,  relief='flat')
margem.pack() #fazendo com que a margem do botão apareça
botao__acrescentar = tk.Button(root, bg='#FFFFFF', text='Bota vai', font=('Montserrat', 16, 'bold'), padx=10, command=acrescentar) #criando o botão
botao__acrescentar.pack() #fazendo com que o botão apareça
contando__as__botada = tk.Label(root, text=numero, fg='#FFFFFF',bg='#1d1d1d', font=('Montserrat', 16, 'bold'))
contando__as__botada.pack()

botao__diminuir = tk.Button(root, bg='#FFFFFF', text='Tira vai', font=('Montserrat', 16, 'bold'), padx=10, command=diminuir) #criando o botão
botao__diminuir.pack() #fazendo com que o botão apareça

root.mainloop() #fazendo com que nossa janela não feche