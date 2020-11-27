from Model import estante as est, documento as doc, caixa as cx
import os
import pandas as pd


class GerenciadorDocumentos:
    @staticmethod
    def adicionar():
        print('='*20)

        protocolo = str(input('protocolo: '))
        caixa = str(input('Codigo da Caixa: '))
        assunto = str(input('assunto: '))
        partes_interessadas_temp = str(input('partes interessadas (ex.: nome1 sobrenome1, nome2 sobrenome2): '))

        partes_interessadas_temp = partes_interessadas_temp.split(',')
        partes_interessadas = []
        for p in partes_interessadas_temp:
            p = p.strip()
            while '  ' in p:
                p = p.replace('  ', ' ')
            partes_interessadas.append(p)

        documento = doc.Documento(protocolo, caixa, assunto, partes_interessadas, '')

        return documento

    @staticmethod
    def anexar():
        print('*'*20)
        protocolo1 = str(input('protocolo do documento a ser anexado: '))
        protocolo2 = str(input('protocolo do documento a receber o anexo: '))

        return protocolo1, protocolo2

    # @staticmethod
    # def listar():
    #     """
    #     Lista todos os documentos de uma dada caixa do arquivo
    #     """
    #     codigo_estante = str(input('Codigo da estante: '))
    #     codigo_caixa = str(input('Codigo da caixa: '))
    #     if not estante.Estante(codigo_estante).existe_estante():
    #         raise Exception('Estante nao existente')
    #     if f'{codigo_caixa}.csv' not in os.listdir(f'data/arquivo/{codigo_estante}'):
    #         raise Exception('Caixa nao existente')
    #
    #     print('*'*20)
    #     print(f'Documentos [Estante: {codigo_estante}; Caixa: {codigo_caixa}]')
    #
    #     df = pd.read_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', encoding='utf-8')
    #     for index, row in df.iterrows():
    #         print('*' * 20)
    #         print(f'assunto: {row["assunto"]}')
    #         print(f'partes interessadas: {row["partes interessadas"]}')
    #         print(f'protocolo: {row["protocolo"]}')
    #         print(f'anexos: {row["anexos"][:-1]}')
    #         print(f'Historico de Tramitacao: {row["Historico de Tramitacao"]}')
    #     print('*' * 20)

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

    # @staticmethod
    # def tramitar(usuario):
    #     print('*' * 20)
    #     doc = documento.Documento().pesquisar('protocolo', str(input('protocolo do documento a ser tramitado: ')))[0]
    #     print('Localização de destino:')
    #     estante_destino = str(input('Estante: '))
    #     destino_caixa = str(input('Caixa: '))
    #     motivo = str(input('Motivo da tramitação: '))
    #
    #     cx = caixa.Caixa(estante.Estante(estante_destino), destino_caixa)
    #     doc.tramitar(cx, motivo, usuario)
