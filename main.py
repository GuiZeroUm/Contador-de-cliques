import tkinter as tk

root = tk.Tk()

root.geometry('600x600') #mudando o tamanho da janela
root.title ('Contador de clicks') #mudando o titulo do app
root.configure (background='#1d1d1d') #adicionando cor de fundo

margem = tk.Canvas(root, height=300, background='#1d1d1d', highlightthickness=0,  relief='flat')
margem.pack() #fazendo com que a margem do botão apareça
botao__foda = tk.Button(root, bg='#FFFFFF', text='Bota vai',) #criando o botão
botao__foda.pack() #fazendo com que o botão apareça

root.mainloop() #fazendo com que nossa janela não feche