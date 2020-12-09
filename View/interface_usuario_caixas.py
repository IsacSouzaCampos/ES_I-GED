import getpass


class InterfaceUsuarioCaixas:
    @staticmethod
    def adicionar():
        codigo_estante = str(input('Código da estante: '))
        return str(input('Codigo da caixa: ')), codigo_estante

    @staticmethod
    def msg_saida_adicionar(cod_msg):
        if cod_msg == 0:
            print('Caixa adicionada com êxito!')
        elif cod_msg == 1:
            print('Caixa já existente!')
        elif cod_msg == 2:
            print('Informações de administrador incorretas!')
        elif cod_msg == 3:
            print('Estante indisponivel no momento!')
        elif cod_msg == 4:
            print('Estante não encontrada!')

    @staticmethod
    def remover():
        return str(input('Código da caixa: '))

    @staticmethod
    def msg_saida_remover(cod_msg):
        if cod_msg == 0:
            print('Caixa removida com êxito!')
        elif cod_msg == 1:
            print('A caixa precisa estar vazia para ser removida!')
        elif cod_msg == 2:
            print('Informações de administrador incorretas!')

    @staticmethod
    def mudar_localizacao_caixa():
        return str(input('Código da caixa: ')), str(input('Nova estante: '))

    @staticmethod
    def msg_saida_mudar_localizacao(cod_msg):
        if cod_msg == 0:
            print('Localização da caixa modificada com êxito!')

    @staticmethod
    def pedir_dados_administrador():
        print('Autorização do Administrador:')
        nome_admin = str(input('Usuario: '))
        senha_admin = getpass.getpass('Senha: ').encode()

        return nome_admin, senha_admin
