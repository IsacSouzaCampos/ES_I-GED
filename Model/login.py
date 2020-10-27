import bcrypt

from Model import administrador, usuarioComum, usuario
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
            raise Exception()
        raise Exception('Opcao nao existente')

    @staticmethod
    def primeiro_acesso(nome: str, senha: bytes, codigo_identificacao: str) -> administrador.Administrador:
        """
        Cria uma conta de administrador no caso de o sistema estar sendo iniciado pela primeira vez
        :return: instância de Administrador
        """
        with open('data/.data', 'w') as fout:
            hashed = bcrypt.hashpw(senha, bcrypt.gensalt())
            info_usuario = f'{nome}:{codigo_identificacao}:{hashed.decode()}'
            fout.write(f'usuario_comum:0;administrador:1\n{info_usuario}')

        return administrador.Administrador(nome, codigo_identificacao)

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

    @staticmethod
    def criar_conta_comum(nome: str, senha: bytes) -> usuarioComum.UsuarioComum:
        """
        Cria uma nova conta comum
        :return: instancia de UsuarioComum
        """
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
    def criar_conta_administrador(nome: str, senha: bytes) -> administrador.Administrador:
        """
        Cria uma nova conta de administrador
        :return: instancia de Administrador
        """
        with open('data/.data', 'r') as fin:
            text = fin.readlines()
            for v in text[0].split(';'):
                if 'usuario_comum' in v:
                    n_usuarios_comuns = int(v.split(':')[1])
                else:
                    n_administradores = int(v.split(':')[1])+1
                    codigo_identificacao = 'A' + str(n_administradores)
            hashed = bcrypt.hashpw(senha, bcrypt.gensalt())
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
