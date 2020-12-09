import getpass


class InterfaceUsuarioDocumentos:
    @staticmethod
    def adicionar():
        print('='*20)

        protocolo = str(input('protocolo: '))
        codigo_caixa = str(input('Codigo da Caixa: '))
        assunto = str(input('assunto: '))
        partes_interessadas_temp = str(input('partes interessadas (ex.: nome1 sobrenome1, nome2 sobrenome2): '))

        partes_interessadas_temp = partes_interessadas_temp.split(',')
        partes_interessadas = ''
        for p in partes_interessadas_temp:
            p = p.strip()
            while '  ' in p:
                p = p.replace('  ', ' ')
            partes_interessadas += f'{p}/'

        return protocolo, codigo_caixa, assunto, partes_interessadas, ''

    @staticmethod
    def msg_saida_adicionar(cod_msg):
        if cod_msg == 0:
            print('Documento adicionado com êxito!')
        elif cod_msg == 1:
            print('O protocolo informado já existe no arquivo!')

    @staticmethod
    def remover():
        return str(input('Protocolo: '))

    @staticmethod
    def msg_saida_remover(cod_msg):
        if cod_msg == 0:
            print('Documento removido com êxito!')
        elif cod_msg == 1:
            print('Informações de administrador incorretas!')

    @staticmethod
    def anexar():
        print('*'*20)
        protocolo1 = str(input('protocolo do documento 1: '))
        protocolo2 = str(input('protocolo do documento 2: '))

        return protocolo1, protocolo2

    @staticmethod
    def msg_saida_anexar(cod_msg):
        if cod_msg == 0:
            print('Anexação feita com êxito!')

    @staticmethod
    def listar_documentos_caixa():
        return str(input('Codigo da caixa: '))

    @staticmethod
    def pesquisar():
        """
        Pesquisa por um documento em todo o arquivo, levando em conta o dado informado pelo usuário
        """
        print('*'*20)
        print('PESQUISAR POR: (dê preferência pelo número de protocolo)')
        print('[1] assunto')
        print('[2] partes interessadas')
        print('[3] protocolo')
        print('[4] data de insercao')
        opcao = int(input('Opcao: '))

        if opcao == 1:
            return 'assunto', str(input('assunto: '))
        elif opcao == 2:
            return 'partes interessadas', str(input('partes interessadas: '))
        elif opcao == 3:
            return 'protocolo', str(input('protocolo: '))
        elif opcao == 4:
            print('Insira a data no formato: dd-mm-aaaa')
            return 'data de insercao', str(input('data de insercao: '))
        elif opcao == 0:
            return '', ''
        else:
            raise Exception('Opcao nao existente')

    @staticmethod
    def imprimir_documento(documento, codigo_estante=None):
        print('*'*20)
        print(f'Estante: {codigo_estante}  -   '
              f'Caixa: {documento.get_caixa().get_codigo()}')
        print('*' * 20)
        print(f'assunto: {documento.get_assunto()}')
        print(f'partes interessadas: {documento.get_partes_interessadas()}')
        print(f'protocolo: {documento.get_protocolo()}')
        print(f'anexos: {documento.get_anexos()}')
        print(f'historico: {documento.get_historico()}')
        print('*' * 20)

    @staticmethod
    def tramitar():
        print('*' * 20)
        protocolo = str(input('Protocolo do documento: '))
        codigo_caixa = str(input('Codigo da caixa destino: '))
        motivo = str(input('Motivo da tramitacao: '))
        return protocolo, codigo_caixa, motivo

    @staticmethod
    def msg_saida_tramitar(cod_msg):
        if cod_msg == 0:
            print('Tramitação feita com êxito!')

    @staticmethod
    def pedir_dados_administrador():
        print('Autorização do Administrador:')
        nome_admin = str(input('Usuario: '))
        senha_admin = getpass.getpass('Senha: ').encode()

        return nome_admin, senha_admin
