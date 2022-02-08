from tkinter import *
from tkinter import ttk


janela = Tk()
janela.title('Cliente')
janela.geometry('250x270')
janela.configure(background='#212529')

txt = 'Faça seu cadastro!'

cadastro = Label(janela, text=txt, bg='#212529', foreground='#fff', anchor='center').place(x=75, y=10, width=100, height=20)


Label(janela, text='Digite seu login',bg='#212529', foreground='#FFC107', anchor='center').place(x=65, y=60, width=120, height=20)
login = StringVar()
entry1 = ttk.Entry(janela, textvariable=login, background='#6C757D')
entry1.place(x=65, y=90, width=120, height=25)


Label(janela, text='Digite sua senha', bg='#212529', foreground='#FFC107', anchor='center').place(x=65, y=120, width=120, height=20)
senha = StringVar()
entry2 = ttk.Entry(janela, textvariable=senha, background='#6C757D')
entry2.place(x=65, y=150, width=120, height=25)


botao = Button(janela, text='Enviar', bg='#0D6EFD', foreground='#fff', anchor='center', command='''inserir aqui função com comando''').place(x=85, y=190, width=80, height=25)


janela.mainloop()