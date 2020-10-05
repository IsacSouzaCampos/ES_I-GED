from View import login
from Model import estante
import os
import getpass

class Estante:
    def __init__(self, codigo=None):
        self.codigo = codigo

    def adicionar_estante(self):
        codigo = str(input('Codigo da estante: '))
        nome = str(input('Autorizacao do administrador\nUsuario: '))
        senha = getpass.getpass('Senha: ').encode()
        with open('data/.data') as _usuarios:
            try:
                hierarquia = login.LogIn().verificar_hierarquia(nome, senha,
                                                                _usuarios.read()).get_codigo_identificacao()[0]
            except Exception as e:
                return print(e)
            if hierarquia == 'A':
                if not self.existe_estante(codigo):
                    os.system(f'mkdir data/arquivo/{codigo}')
                else:
                    raise Exception('Estante ja existente')
            else:
                print('Conta de administrador incorreta')
