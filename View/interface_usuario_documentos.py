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
    def anexar():
        print('*'*20)
        protocolo1 = str(input('protocolo do documento 1: '))
        protocolo2 = str(input('protocolo do documento 2: '))

        return protocolo1, protocolo2

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
    def tramitar():
        print('*' * 20)
        protocolo = str(input('Protocolo do documento: '))
        codigo_caixa = str(input('Codigo da caixa destino: '))
        motivo = str(input('Motivo da tramitacao: '))
        return protocolo, codigo_caixa, motivo
