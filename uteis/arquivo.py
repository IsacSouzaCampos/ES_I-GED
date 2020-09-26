from uteis import login, estante
import os
import getpass


class Arquivo:
    def adicionar_estante(self):
        codigo = str(input('Codigo da estante: '))
        nome = str(input('Autorizacao do administrador\nUsuario: '))
        senha = getpass.getpass('Senha: ').encode()
        with open('data/.data') as _usuarios:
            try:
                hierarquia = login.LogIn().verificar_conta(nome, senha,
                                                           _usuarios.read()).get_codigo_identificacao()[0]
            except Exception as e:
                return print(e)
            if hierarquia == 'A':
                if not os.path.exists(codigo):
                    os.system(f'mkdir data/arquivo/{codigo}')
                else:
                    print('Estante ja existente')

    def listar_secoes(self):
        for _secao in self.secoes:
            print(_secao.get_codigo())
