from PySimpleGUI import PySimpleGUI as sg

# layout
sg.theme('reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login ?')],
    [sg.Button('Entrar')]
]

# Janela
Janela = sg.Window('Tela de login', layout)

# Ler os eventos
while True:
    eventos, valores = Janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usario'] == 'Guilherme' and valores['senha'] == '123456':
            print('Bem vindo')
