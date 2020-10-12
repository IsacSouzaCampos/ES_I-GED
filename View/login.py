import getpass
import bcrypt
from builtins import staticmethod

from Model import administrador, usuarioComum


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
                        return self.verificar_hierarquia(nome, senha, usuarios)
                    elif opcao == 2:
                        return self.criar_conta()
                except Exception as e:
                    raise e

    @staticmethod
    def opcao_entrada():
        print('[1] Entrar')
        print('[2] Criar Conta')
        print('[0] Sair')
        opcao = int(input('Opcao: '))

        if 0 < opcao < 3:
            return opcao
        elif opcao == 0:
            raise Exception()
        raise Exception('Opcao nao existente')

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
            hashed = bcrypt.hashpw(senha, bcrypt.gensalt())
            info_usuario = f'{nome}:{codigo_identificacao}:{hashed.decode()}'
            fout.write(f'usuario_comum:0;administrador:1\n{info_usuario}')

        return administrador.Administrador(nome, codigo_identificacao)

    def criar_conta(self):
        print('[1] Usuario Comum')
        print('[2] Administrador')
        opcao = int(input('Opcao: '))

        if opcao == 1:
            return self.criar_conta_comum()
        elif opcao == 2:
            return self.criar_conta_administrador()
        else:
            raise Exception('Opcao nao existente')

    @staticmethod
    def criar_conta_comum():
        nome = str(input('Nome do usuario: '))
        senha = getpass.getpass('Senha: ').encode()

        with open('data/.data', 'r') as fin:
            text = fin.readlines()
            for v in text[0].split(';'):
                if 'usuario_comum' in v:
                    n_usuarios_comuns = int(v.split(':')[1])+1
                    codigo_identificacao = 'C' + str(n_usuarios_comuns)
                else:
                    n_administradores = int(v.split(':')[1])
            hashed = bcrypt.hashpw(senha, bcrypt.gensalt())
            text[0] = f'usuario_comum:{n_usuarios_comuns};administrador:{n_administradores}\n'
            info_usuario = f'{nome}:{codigo_identificacao}:{hashed.decode()}'
            text.append('\n' + info_usuario)

        with open('data/.data', 'w') as fout:
            fout.writelines(text)

        return usuarioComum.UsuarioComum(nome, codigo_identificacao)

    @staticmethod
    def criar_conta_administrador():
        nome = str(input('Nome do usuario: '))
        senha = getpass.getpass('Senha: ').encode()

        with open('data/.data', 'r') as fin:
            text = fin.readlines()
            for v in text[0].split(';'):
                if 'usuario_comum' in v:
                    n_usuarios_comuns = int(v.split(':')[1])
                else:
                    n_administradores = int(v.split(':')[1])+1
                    codigo_identificacao = 'A' + str(n_administradores)
            hashed = bcrypt.hashpw(senha, bcrypt.gensalt(rounds=15))
            text[0] = f'usuario_comum:{n_usuarios_comuns};administrador:{n_administradores}\n'
            info_usuario = f'{nome}:{codigo_identificacao}:{hashed.decode()}'
            text.append('\n' + info_usuario)

        with open('data/.data', 'w') as fout:
            fout.writelines(text)

        return administrador.Administrador(nome, codigo_identificacao)

    @staticmethod
    def verificar_hierarquia(nome, senha, usuarios):
        for line in usuarios.splitlines():
            try:
                line_vec = line.split(':')
                if line_vec[0] == nome:
                    if bcrypt.checkpw(senha, line_vec[2].encode()):
                        if line_vec[1][0] == 'A':
                            return administrador.Administrador(nome, line_vec[1])
                        elif line_vec[1][0] == 'C':
                            return usuarioComum.UsuarioComum(nome, line_vec[1])
            except:
                continue
        raise Exception('Erro ao tentar logar')