import getpass
import bcrypt
from builtins import staticmethod

from uteis import administrador, usuarioComum


class LogIn:
    def login(self):
        with open('data/.data', 'r') as _usuarios:
            usuarios = _usuarios.read()
            if not usuarios:
                return self.primeiro_acesso()
            else:
                try:
                    opcao = self.opcao_entrada()
                    if opcao == 1:
                        nome = str(input('Nome de usuario: '))
                        senha = getpass.getpass('Senha: ').encode()
                        return self.verificar_conta(nome, senha, usuarios)
                    elif opcao == 2:
                        self.criar_conta()
                except Exception as e:
                    return e

    @staticmethod
    def opcao_entrada():
        print('[1] Entrar')
        print('[2] Criar Conta')
        print('[0] Sair')
        return int(input('Opcao: '))

    @staticmethod
    def primeiro_acesso():
        print('=====PRIMEIRO ACESSO=====')
        print('Por ser o primeiro acesso no sistema, voce sera automaticamente\n'
              ' registrado como administrador. As proximas contas a serem adicionadas\n'
              ' precisarao de autorizacao de um administrador ja existente\n'
              ' do sistema para serem efetuadas.')
        nome = str(input('\nNome de usuario: '))
        senha = getpass.getpass('Senha: ').encode()
        codigo_identificacao = 'A0'

        with open('data/.data', 'w') as fout:
            hashed = bcrypt.hashpw(senha, bcrypt.gensalt(rounds=15))
            print(f'{nome}:{codigo_identificacao}:{hashed.decode()}', file=fout)

        return administrador.Administrador(nome, codigo_identificacao)

    @staticmethod
    def criar_conta():
        pass

    @staticmethod
    def verificar_conta(nome, senha, usuarios):
        for line in usuarios.splitlines():
            line_vec = line.split(':')
            if line_vec[0] == nome:
                if bcrypt.checkpw(senha, line_vec[2].encode()):
                    if line_vec[1][0] == 'A':
                        return administrador.Administrador(nome, line_vec[1])
                    elif line_vec[1][0] == 'C':
                        return usuarioComum.UsuarioComum(nome, line_vec[1])
        raise Exception('Erro ao tentar logar')
