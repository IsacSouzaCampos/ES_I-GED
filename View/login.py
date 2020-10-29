import getpass

from Model import administrador, usuario_comum, usuario, login


class LogIn:
    def login(self) -> usuario.Usuario:
        """
        Faz as verificações necessárias antes de inicializar o sistema
        :return: instância de Usuario referente ao usuário solicitante do LogIn
        """
        while True:
            with open('data/.data.csv', 'r') as _usuarios:
                usuarios = _usuarios.read()
                if not usuarios:
                    return self.primeiro_acesso()
            try:
                opcao = self.opcao_entrada()
                if opcao == 1:
                    nome = str(input('Usuario: '))
                    senha = getpass.getpass('Senha: ').encode()
                    return login.LogIn().verificar_hierarquia(nome, senha)
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

        return login.LogIn().opcao_entrada(opcao)

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
        nome = str(input('\nUsuario: '))
        senha = getpass.getpass('Senha: ').encode()
        tipo_conta = 'administrador'

        return login.LogIn().primeiro_acesso(nome, senha, tipo_conta)

    def criar_conta(self) -> usuario.Usuario:
        """
        Solicita o tipo de conta a ser criada
        :return: instancia da subclasse de Usuario (Administrador / UsuarioComum) escolhida
        """
        print('[1] Usuario Comum')
        print('[2] Administrador')
        opcao = int(input('Opcao: '))

        return login.LogIn().criar_conta(opcao)

    @staticmethod
    def criar_conta_comum() -> usuario_comum.UsuarioComum:
        """
        Cria uma nova conta comum
        :return: instancia de UsuarioComum
        """
        nome = str(input('Usuario: '))
        senha = getpass.getpass('Senha: ').encode()

        return login.LogIn().criar_conta_comum(nome, senha, 'conta_comum')

    @staticmethod
    def criar_conta_administrador() -> administrador.Administrador:
        """
        Cria uma nova conta de administrador
        :return: instancia de Administrador
        """
        nome = str(input('Usuario: '))
        senha = getpass.getpass('Senha: ').encode()


        return login.LogIn().criar_conta_administrador(nome, senha, 'administrador')
