from Model import estante, documento
import os
import pandas as pd


class Documento:
    @staticmethod
    def adicionar():
        print('='*20)
        assunto = str(input('Assunto: '))
        partes_interessadas_temp = str(input('Partes Interessadas (ex.: nome1 sobrenome1, nome2 sobrenome2): '))
        numero_protocolo = str(input('Numero de Protocolo: '))
        codigo_estante = str(input('Codigo da Estante: '))
        codigo_caixa = str(input('Codigo da Caixa: '))

        partes_interessadas_temp = partes_interessadas_temp.split(',')
        partes_interessadas = []
        for p in partes_interessadas_temp:
            p = p.strip()
            while '  ' in p:
                p = p.replace('  ', ' ')
            partes_interessadas.append(p)
        try:
            documento.Documento(assunto, partes_interessadas, numero_protocolo).adicionar(codigo_estante, codigo_caixa)
        except Exception as e:
            raise e

    @staticmethod
    def anexar():
        print('*'*20)
        print('\nDADOS DO ITEM A SER ANEXADO')
        item1_estante = str(input('Estante: '))
        item1_caixa = str(input('Caixa: '))
        item1_protocolo = str(input('Protocolo: '))

        print('\nDADOS DO ITEM A RECEBER O ANEXO')
        item2_estante = str(input('Estante: '))
        item2_caixa = str(input('Caixa: '))
        item2_protocolo = str(input('Protocolo: '))

        dados_item1 = (item1_estante, item1_caixa, item1_protocolo)
        dados_item2 = (item2_estante, item2_caixa, item2_protocolo)
        try:
            documento.Documento().anexar(dados_item1, dados_item2)
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
            print(f'Numero de Protocolo: {row["Numero de Protocolo"]}')
            print(f'Anexos: {row["Anexos"]}')
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
        print('[3] Numero de Protocolo')
        print('[4] Data de Insercao')
        opcao = int(input('Opcao: '))

        if opcao == 1:
            results = documento.Documento().pesquisar('Assunto', str(input('Assunto: ')))
        elif opcao == 2:
            results = documento.Documento().pesquisar('Partes Interessadas', str(input('Partes Interessadas: ')))
        elif opcao == 3:
            results = documento.Documento().pesquisar('Numero de Protocolo', str(input('Numero de Protocolo: ')))
        elif opcao == 4:
            print('Insira a data no formato: dd-mm-aaaa')
            results = documento.Documento().pesquisar('Data de Insercao', str(input('Data de Insercao: ')))
        elif opcao == 0:
            return
        else:
            raise Exception('Opcao nao existente')

        for dados in results:
            print('*'*20)
            print(f'Estante: {dados[0]}  -   Caixa: {dados[1]}')
            print('*' * 20)
            print(f'Assunto: {dados[2]}')
            print(f'Partes Interessadas: {dados[3]}')
            print(f'Numero de Protocolo: {dados[4]}')
            print(f'Anexos: {dados[5]}')
            print(f'Historico de Tramitacao: {dados[6]}')
        print('*' * 20)
