import getpass
import bcrypt

from Model import administrador, usuarioComum, usuario


class LogIn:
    def login(self) -> usuario.Usuario:
        """
        Faz as verificações necessárias antes de inicializar o sistema
        :return: instância de Usuario referente ao usuário solicitante do LogIn
        """
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
    def opcao_entrada() -> int:
        """
        Verifica o que o usuário deseja fazer antes de inicializar o sistema
        :return: inteiro referente à opção escolhida
        """
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
    def primeiro_acesso() -> administrador.Administrador:
        """
        Cria uma conta de administrador no caso de o sistema estar sendo iniciado pela primeira vez
        :return: instância de Administrador
        """
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

    def criar_conta(self) -> usuario.Usuario:
        """
        Solicita o tipo de conta a ser criada
        :return: instancia da subclasse de Usuario (Administrador / UsuarioComum) escolhida
        """
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
    def criar_conta_comum() -> usuarioComum.UsuarioComum:
        """
        Cria uma nova conta comum
        :return: instancia de UsuarioComum
        """
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
    def criar_conta_administrador() -> administrador.Administrador:
        """
        Cria uma nova conta de administrador
        :return: instancia de Administrador
        """
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
    def verificar_hierarquia(nome: str, senha: str, usuarios: str) -> usuario.Usuario:
        """
        Verifica se a conta do usuário passado como parâmetro é de um administrador ou comum.
        :param nome: nome do usuário a ser verificado
        :param senha: senha do usuário a ser verificado
        :param usuarios: string do documento que possui registro de usuários do sistema
        :return: instância da subclasse de Usuario (Administrador / UsuarioComum) a qual os valores verificados
        pertencem
        :raise: Conta não existente ou senha incorreta
        """
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
