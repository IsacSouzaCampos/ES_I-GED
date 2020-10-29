import bcrypt
import pandas as pd
import getpass

from Model import administrador, usuario_comum, usuario
from View import login


class LogIn:
    @staticmethod
    def opcao_entrada(opcao: int) -> int:
        """
        Verifica o que o usuário deseja fazer antes de inicializar o sistema
        :return: inteiro referente à opção escolhida
        """
        if 0 < opcao < 3:
            return opcao
        elif opcao == 0:
            exit()
        raise Exception('Opcao nao existente')

    @staticmethod
    def primeiro_acesso(nome: str, senha: bytes, tipo_conta: str) -> administrador.Administrador:
        """
        Cria uma conta de administrador no caso de o sistema estar sendo iniciado pela primeira vez
        :return: instância de Administrador
        """
        hashed = bcrypt.hashpw(senha, bcrypt.gensalt())
        # creating data frame
        df = pd.DataFrame({'Usuario': [nome],
                           'Senha': [hashed.decode()],
                           'Tipo da Conta': [tipo_conta]})
        df.to_csv('data/.data.csv', index=False, encoding='utf-8')

        return administrador.Administrador(nome)

    def criar_conta(self, opcao: int) -> usuario.Usuario:
        """
        :param opcao: opcao de conta a ser criada
        :return: instancia da subclasse de Usuario (Administrador / UsuarioComum) escolhida
        """
        if opcao == 1:
            return login.LogIn().criar_conta_comum()
        elif opcao == 2:
            return login.LogIn().criar_conta_administrador()
        else:
            raise Exception('Opcao nao existente')

    def criar_conta_comum(self, nome: str, senha: bytes, tipo_conta: str) -> usuario_comum.UsuarioComum:
        """
        Cria uma nova conta comum
        :return: instancia de UsuarioComum
        """
        if self.existe_usuario(nome):
            raise Exception('Nome de usuario já existente!')

        hashed = bcrypt.hashpw(senha, bcrypt.gensalt())

        df = pd.read_csv('data/.data.csv', encoding='utf-8')
        df2 = pd.DataFrame({'Usuario': [nome],
                            'Senha': [hashed.decode()],
                            'Tipo da Conta': [tipo_conta]})

        pd.concat([df, df2]).to_csv('data/.data.csv', index=False, encoding='utf-8')

        return usuario_comum.UsuarioComum(nome)

    def criar_conta_administrador(self, nome: str, senha: bytes, tipo_conta: str) -> administrador.Administrador:
        """
        Cria uma nova conta de administrador
        :return: instancia de Administrador
        """
        print('Autorização do Administrador:')
        nome_admin = str(input('Usuario: '))
        senha_admin = getpass.getpass('Senha: ').encode()
        if type(self.verificar_hierarquia(nome_admin, senha_admin)) is not administrador.Administrador:
            raise Exception('Informações de administrador incorretas!')

        hashed = bcrypt.hashpw(senha, bcrypt.gensalt())

        df = pd.read_csv('data/.data.csv', encoding='utf-8')
        df2 = pd.DataFrame({'Usuario': [nome],
                            'Senha': [hashed.decode()],
                            'Tipo da Conta': [tipo_conta]})

        pd.concat([df, df2]).to_csv('data/.data.csv', index=False, encoding='utf-8')

        return administrador.Administrador(nome)

    @staticmethod
    def verificar_hierarquia(nome: str, senha: bytes) -> usuario.Usuario:
        """
        Verifica se a conta do usuário passado como parâmetro é de um administrador ou comum.
        :param nome: nome do usuário a ser verificado
        :param senha: senha do usuário a ser verificado
        :return: instância da subclasse de Usuario (Administrador / UsuarioComum) a qual os valores verificados
        pertencem
        :raise: Conta não existente ou senha incorreta
        """
        df = pd.read_csv('data/.data.csv', encoding='utf-8')

        for index, row in df.iterrows():
            if row['Usuario'] == nome and bcrypt.checkpw(senha, row['Senha'].encode()):
                if row['Tipo da Conta'] == 'administrador':
                    return administrador.Administrador(nome)
                else:
                    return usuario_comum.UsuarioComum(nome)

        raise Exception('Erro ao tentar logar')

    @staticmethod
    def existe_usuario(nome: str) -> bool:
        """
        Verifica existência do nome pesquisado na tabela de usuários
        :param nome: Nome a ser pesquisado no dataframe
        :return: bool
        """
        df = pd.read_csv('data/.data.csv', encoding='utf-8')
        for index, row in df.iterrows():
            if row['Usuario'] == nome:
                return True
        return False
