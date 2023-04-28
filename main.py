from tkinter import *

# cor
cor1 = "#202120"  # Cinza escuro
cor2 = "#feffff"  # Branco
cor3 = "#38576b"  # Azul carrengando
cor4 = "#ECEFF1"  # Cinzza
cor5 = "#ffab40"  # Laranja

# Criando frames
janela = Tk()
janela.title("Calculadora")
janela.geometry("320x402")
janela.config(bg=cor1)

frame_tela = Frame(janela, width=320, height=150, bg=cor3)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=320, height=350)
frame_corpo.grid(row=1, column=0)

# Variaveis todos valores

todos_valores = ''

valor_texto = StringVar()

# Criando função


def entrar_valores(event):
    global todos_valores

    todos_valores = todos_valores + str(event)

# passando p/tela
    valor_texto.set(todos_valores)

# Função p/ calcular


def calcular():
    global todos_valores
    resultado = eval(todos_valores)

    # Passando valor p/ tela
    valor_texto.set(str(resultado))

# Função p/ limpar tela


def limpar_tela():
    global todos_valores
    todos_valores = ""
    valor_texto.set("")


# Criando Label
app_label = Label(frame_tela, textvariable=valor_texto,
                  width=13, height=5, padx=5, relief=FLAT, anchor="e", justify=RIGHT, font="Roboto 31", bg=cor3, fg=cor2)
app_label.place(x=0, y=0)


# criando os botões

# Botão clear
b_1 = Button(frame_corpo, command=limpar_tela, text="C", width=11, height=2, bg=cor4,
             font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)

# botão porcentamge
b_2 = Button(frame_corpo, command=lambda: entrar_valores('%'), text="%", width=11, height=2, bg=cor4,
             font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)

# botão / (dividir)
b_3 = Button(frame_corpo, command=lambda: entrar_valores('/'), text="/", width=8, height=2, bg=cor5, fg=cor2,
             font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=235, y=0)


# botão numeros 1 llinha
b_4 = Button(frame_corpo, command=lambda: entrar_valores('7'), text="7", width=7, height=2, bg=cor4, fg=cor1,
             font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=51)

b_4_1 = Button(frame_corpo, command=lambda: entrar_valores('8'), text="8", width=7, height=2, bg=cor4, fg=cor1,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4_1.place(x=80, y=51)

b_4_3 = Button(frame_corpo, command=lambda: entrar_valores('9'), text="9", width=7, height=2, bg=cor4, fg=cor1,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4_3.place(x=160, y=51)

b_4_4 = Button(frame_corpo, command=lambda: entrar_valores('*'), text="X", width=8, height=2, bg=cor5, fg=cor2,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4_4.place(x=235, y=51)

# botão numeros 2 llinha
b_5 = Button(frame_corpo, command=lambda: entrar_valores('4'), text="4", width=7, height=2, bg=cor4, fg=cor1,
             font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=0, y=101)

b_5_1 = Button(frame_corpo, command=lambda: entrar_valores('5'), text="5", width=7, height=2, bg=cor4, fg=cor1,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5_1.place(x=80, y=101)

b_5_3 = Button(frame_corpo, command=lambda: entrar_valores('6'), text="6", width=7, height=2, bg=cor4, fg=cor1,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5_3.place(x=160, y=101)

b_5_4 = Button(frame_corpo, command=lambda: entrar_valores('-'), text="-", width=8, height=2, bg=cor5, fg=cor2,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5_4.place(x=235, y=101)

# botão numeros 3 llinha
b_6 = Button(frame_corpo, command=lambda: entrar_valores('1'), text="1", width=7, height=2, bg=cor4, fg=cor1,
             font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=0, y=151)

b_6_1 = Button(frame_corpo, command=lambda: entrar_valores('2'), text="2", width=7, height=2, bg=cor4, fg=cor1,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6_1.place(x=80, y=151)

b_6_3 = Button(frame_corpo, command=lambda: entrar_valores('3'), text="3", width=7, height=2, bg=cor4, fg=cor1,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6_3.place(x=160, y=151)

b_6_4 = Button(frame_corpo, command=lambda: entrar_valores('+'), text="+", width=8, height=2, bg=cor5, fg=cor2,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6_4.place(x=235, y=151)


# botão numeros 4 llinha
b_7 = Button(frame_corpo, command=lambda: entrar_valores('0'), text="0", width=15, height=2, bg=cor4,
             font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=0, y=202)

b_8_3 = Button(frame_corpo, command=lambda: entrar_valores('.'), text=".", width=7, height=2, bg=cor4, fg=cor1,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8_3.place(x=160, y=202)

b_8_4 = Button(frame_corpo, command=calcular, text="=", width=8, height=2, bg=cor5, fg=cor2,
               font=('Roboto 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8_4.place(x=235, y=202)

janela.mainloop()
