from View import login
from Model import estante, administrador
import os
import getpass


class Estante:
    def adicionar(self, usuario):
        est = estante.Estante(str(input('Codigo da estante: ')))

        try:
            if type(usuario) is administrador.Administrador:
                est.adicionar()
            else:
                nome = str(input('Autorizacao do administrador\nUsuario: '))
                senha = getpass.getpass('Senha: ').encode()

                with open('data/.data') as _usuarios:
                    usuario_autorizacao = login.LogIn().verificar_hierarquia(nome, senha, _usuarios.read())
                    if type(usuario_autorizacao) is administrador.Administrador:
                        if not est.existe_estante():
                            os.system(f'mkdir data/arquivo/{est.get_codigo()}')
                        else:
                            raise Exception('Estante ja existente')
                    else:
                        print('Conta de administrador incorreta')
        except Exception as e:
            raise e
