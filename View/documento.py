from Model import estante, documento, caixa
import os
import pandas as pd


class Documento:
    @staticmethod
    def adicionar():
        print('='*20)
        doc = documento.Documento()
        doc.set_assunto(str(input('Assunto: ')))
        partes_interessadas_temp = str(input('Partes Interessadas (ex.: nome1 sobrenome1, nome2 sobrenome2): '))
        doc.set_protocolo(str(input('Protocolo: ')))
        codigo_estante = str(input('Codigo da Estante: '))
        codigo_caixa = str(input('Codigo da Caixa: '))
        doc.set_caixa(caixa.Caixa(estante.Estante(codigo_estante), codigo_caixa))

        partes_interessadas_temp = partes_interessadas_temp.split(',')
        partes_interessadas = []
        for p in partes_interessadas_temp:
            p = p.strip()
            while '  ' in p:
                p = p.replace('  ', ' ')
            partes_interessadas.append(p)
        doc.set_partes_interessadas(partes_interessadas)
        try:
            doc.adicionar()
        except Exception as e:
            raise e

    @staticmethod
    def anexar(usuario):
        print('*'*20)
        protocolo1 = str(input('Protocolo do documento a ser anexado: '))

        protocolo2 = str(input('Protocolo do documento a receber o anexo: '))

        try:
            documento.Documento().anexar(protocolo1, protocolo2, usuario)
        except Exception as e:
            print(e)

    @staticmethod
    def listar():
        """
        Lista todos os documentos de uma dada caixa do arquivo
        """
        codigo_estante = str(input('Codigo da estante: '))
        codigo_caixa = str(input('Codigo da caixa: '))
        if not estante.Estante(codigo_estante).existe_estante():
            raise Exception('Estante nao existente')
        if f'{codigo_caixa}.csv' not in os.listdir(f'data/arquivo/{codigo_estante}'):
            raise Exception('Caixa nao existente')

        print('*'*20)
        print(f'Documentos [Estante: {codigo_estante}; Caixa: {codigo_caixa}]')

        df = pd.read_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', encoding='utf-8')
        for index, row in df.iterrows():
            print('*' * 20)
            print(f'Assunto: {row["Assunto"]}')
            print(f'Partes Interessadas: {row["Partes Interessadas"]}')
            print(f'Protocolo: {row["Protocolo"]}')
            print(f'Anexos: {row["Anexos"][:-1]}')
            print(f'Historico de Tramitacao: {row["Historico de Tramitacao"]}')
        print('*' * 20)

    @staticmethod
    def pesquisar():
        """
        Pesquisa por um documento em todo o arquivo, levando em conta o dado informado pelo usuário
        """
        print('*'*20)
        print('PESQUISAR POR: (dê preferência pelo número de protocolo)')
        print('[1] Assunto')
        print('[2] Partes Interessadas')
        print('[3] Protocolo')
        print('[4] Data de Insercao')
        opcao = int(input('Opcao: '))

        if opcao == 1:
            results = documento.Documento().pesquisar('Assunto', str(input('Assunto: ')))
        elif opcao == 2:
            results = documento.Documento().pesquisar('Partes Interessadas', str(input('Partes Interessadas: ')))
        elif opcao == 3:
            results = documento.Documento().pesquisar('Protocolo', str(input('Protocolo: ')))
        elif opcao == 4:
            print('Insira a data no formato: dd-mm-aaaa')
            results = documento.Documento().pesquisar('Data de Insercao', str(input('Data de Insercao: ')))
        elif opcao == 0:
            return
        else:
            raise Exception('Opcao nao existente')

        if not results:
            raise Exception('Documento não encontrado!')

        for doc in results:
            print('*'*20)
            print(f'Estante: {doc.get_caixa().get_estante().get_codigo()}  -   '
                  f'Caixa: {doc.get_caixa().get_codigo()}')
            print('*' * 20)
            print(f'Assunto: {doc.get_assunto()}')
            print(f'Partes Interessadas: {doc.get_partes_interessadas()}')
            print(f'Protocolo: {doc.get_protocolo()}')
            print(f'Anexos: {doc.get_anexos()}')
            print(f'Historico de Tramitacao: {doc.get_historico_tramitacao()}')
        print('*' * 20)

    @staticmethod
    def tramitar(usuario):
        print('*' * 20)
        doc = documento.Documento().pesquisar('Protocolo', str(input('Protocolo do documento a ser tramitado: ')))[0]
        print('Localização de destino:')
        destino_estante = str(input('Estante: '))
        destino_caixa = str(input('Caixa: '))
        motivo = str(input('Motivo da tramitação: '))

        cx = caixa.Caixa(estante.Estante(destino_estante), destino_caixa)
        doc.tramitar(cx, motivo, usuario)
