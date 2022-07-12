import PySimpleGUI as sg
import getpass

sg.theme("DarkTanBlue")
Tela = [
    [sg.Text('Usuário')],
    [sg.Input(key='usuario')],
    [sg.Text('Senha')],
    [sg.Input(key='senha')],
    [sg.Button('login')],
    [sg.Text('', key=('mensagem'))],
]

window = sg.Window('Login', layout = Tela)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'login':
        usuario_correto = 'Flavio'
        senha_correta = '123456'
        usuario = values['usuario']
        senha = values['senha']
        if senha == senha_correta and usuario == usuario_correto:
            window['mensagem'].update('Login feito com sucesso')
        else:
            window['mensagem'].update('Longin ou senha errada')


