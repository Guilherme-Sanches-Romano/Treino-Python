from platform import release
from tkinter import *
from tkinter import ttk


color1 = '#45443f'  # cinza
color2 = '#fc03f4'  # roxo
color3 = '#fcec03'  # amarelo
color4 = '#a4a7ab'  #branco
color5 = '#ce65f7'  #pink
color6 = '#65a7f7'  #azul claro
# criando janela
janela = Tk()

# configurações básicas da janela
janela.title('Calculadora')
janela.geometry('235x310')
janela.config(bg=color3)

# criando frames(divisões) na janela
frame_cabeca = Frame(janela, width='235', height='50', bg=color5)
frame_cabeca.grid(row=0, column=0)

frame_corpo = Frame(janela, width='235', height='260')
frame_corpo.grid(row=1, column=0)

#variáveis
valores = ''
valor_texto = StringVar()

#Criando função

def entrada(event):

    global valores   
    valores = valores +  str(event)

    #passando texto pra tela
    valor_texto.set(valores)

#função de calcular 

def calcular():
    resultado = eval(valores)
    valor_texto.set(str(resultado))
    

#função limpar tela

def limpar():
    global valores
    valores = ''
    valor_texto.set('')


#criando label 

labelr = Label(frame_cabeca, textvariable=valor_texto, width=16, height=2, padx=7, anchor='e', font=('Ivy 18'), bg=color5, fg=color6)
labelr.place(x=0,y=0)

# criando botões

bc = Button(frame_corpo,command= limpar, text="C", width=11, height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bc.place(x=0, y=0)
br = Button(frame_corpo, command = lambda: entrada('%'), text='%',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
br.place(x= 120,y=0)
bd = Button(frame_corpo,command = lambda: entrada('/'), text='/',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bd.place(x= 180,y=0)
bm = Button(frame_corpo, command = lambda: entrada('*'),text='*',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bm.place(x= 180,y=52)
bme = Button(frame_corpo,command = lambda: entrada('-'), text='-',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bme.place(x=180 ,y=104)
bma = Button(frame_corpo,command = lambda: entrada('+'), text='+',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bma.place(x=180,y=156)

b0 = Button(frame_corpo,command = lambda: entrada('0'), text='0',width=11,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b0.place(x= 0,y=208)
bd = Button(frame_corpo,command = lambda: entrada('.'), text='.',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
bd.place(x=120,y=208 )
be = Button(frame_corpo,command = calcular, text='=',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
be.place(x=180,y=208 )

b7 = Button(frame_corpo,command = lambda: entrada('7'), text='7',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b7.place(x= 0,y=52)
b8 = Button(frame_corpo,command = lambda: entrada('8'), text='8',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b8.place(x= 60,y=52)
b9 = Button(frame_corpo,command = lambda: entrada('9'), text='9',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b9.place(x= 120,y=52)

b4 = Button(frame_corpo,command = lambda: entrada('4'), text='4',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b4.place(x= 0,y=104)
b5 = Button(frame_corpo,command = lambda: entrada('5'), text='5',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b5.place(x= 60,y=104)
b6 = Button(frame_corpo,command = lambda: entrada('6'), text='6',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b6.place(x= 120,y=104)

b1 = Button(frame_corpo,command = lambda: entrada('1'), text='1',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b1.place(x= 0,y=156)
b2 = Button(frame_corpo,command = lambda: entrada('2'),text='2',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b2.place(x= 60,y=156)
b3 = Button(frame_corpo,command = lambda: entrada('3'), text='3',width=5,height=2, bg=color6, fg=color5, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b3.place(x= 120,y=156)


janela.mainloop()
