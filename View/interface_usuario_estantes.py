import getpass

from Model import estante, administrador, usuario, login


class InterfaceUsuarioEstantes:
    def adicionar(self, usuario: usuario.Usuario):
        codigo = str(input('Codigo da estante: '))
        disponibilidade = str(input('Disponibilidade da estante: '))
        try:
            if type(usuario) is administrador.Administrador:
                return codigo, disponibilidade
            else:
                nome_admin = str(input('Autorizacao do administrador:\nUsuario: '))
                senha_admin = getpass.getpass('Senha: ').encode()

                admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
                if type(admin) is administrador.Administrador:
                    return codigo, disponibilidade
                else:
                    raise Exception('Erro na autorização do administrador')

        except Exception as e:
            raise e

    @staticmethod
    def msg_saida_adicionar(cod_msg):
        if cod_msg == 0:
            print('Estante adicionada com êxito!')
        elif cod_msg == 1:
            print('Estante já existente!')

    @staticmethod
    def remover():
        return str(input('Código da estante: '))

    @staticmethod
    def msg_saida_remover(cod_msg):
        if cod_msg == 0:
            print('Estante removida com êxito!')
        elif cod_msg == 1:
            print('A estante precisa estar vazia para ser removida!')
        elif cod_msg == 2:
            print('Informações de administrador incorretas!')

    @staticmethod
    def pedir_dados_administrador():
        print('Autorização do Administrador:')
        nome_admin = str(input('Usuario: '))
        senha_admin = getpass.getpass('Senha: ').encode()

        return nome_admin, senha_admin
