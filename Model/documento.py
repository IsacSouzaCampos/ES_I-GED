import os
import pandas as pd
from datetime import date


class Documento:
    def __init__(self, assunto=None, partes_interessadas=None, numero_protocolo=None):
        self.assunto = assunto
        self.partes_interessadas = partes_interessadas
        self.numero_protocolo = numero_protocolo

    def adicionar(self, codigo_estante: str, codigo_caixa: str):
        """
        Adiciona um documento no arquivo
        :param codigo_estante: estante a receber o documento
        :param codigo_caixa: caixa a receber o documento
        """
        try:
            data = date.today()
            historico_tramitacao = f'Data: {data.day}-{data.month}-{data.year}\n' \
                                   f'Localizacao: estante_{codigo_estante}-caixa_{codigo_caixa}'

            df2 = pd.DataFrame({'Assunto': [self.get_assunto()],
                                'Partes Interessadas': [self.get_partes_interessadas()],
                                'Numero de Protocolo': [self.get_numero_protocolo()],
                                'Anexos': [' '],
                                'Historico de Tramitacao': [historico_tramitacao]})

            with open(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', encoding='utf-8') as fin:
                if not fin.read():
                    df2.to_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', index=False, encoding='utf-8')
                else:
                    df = pd.read_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', encoding='utf-8')
                    pd.concat([df, df2]).to_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', index=False,
                                                encoding='utf-8')

        except Exception as e:
            raise Exception(e)

        print('Finalizado')

    @staticmethod
    def anexar(item1, item2):
        """
        Anexa um documento a outro
        :param item1: contem os dados do documento a ser anexado (estante, caixa, protocolo)
        :param item2: contem os dados do documento a receber o anexo
        """
        # dados[0] = estante; dados[1] = caixa; dados[2] = protocolo;
        try:
            df1 = pd.read_csv(f'data/arquivo/{item1[0]}/{item1[1]}.csv', encoding='utf-8')
            df2 = pd.read_csv(f'data/arquivo/{item2[0]}/{item2[1]}.csv', encoding='utf-8')

            data = date.today()
            df_item1 = df1.loc[df1['Numero de Protocolo'].astype(str) == item1[2]]

            df1 = df1.drop(df_item1.index)
            df1.to_csv(f'data/arquivo/{item1[0]}/{item1[1]}.csv', index=False, encoding='utf-8')

            df_item1['Historico de Tramitacao'] += '\n***********************\n' \
                                                   f'Data: {data.day}-{data.month}-{data.year}\n' \
                                                   f'Localizacao: estante_{item2[0]}-caixa_{item2[1]}\n' \
                                                   f'Anexado ao documento: [{item2[2]}]'

            df_item2 = df2.loc[df2['Numero de Protocolo'].astype(str) == item2[2]]
            df_item2['Anexos'] += f'[{item1[2]}]\n'

            df2 = df2.drop(df_item2.index)

            pd.concat([df2, df_item1, df_item2]).to_csv(f'data/arquivo/{item2[0]}/{item2[1]}.csv', index=False,
                                                        encoding='utf-8')
        except Exception as e:
            raise e

    @staticmethod
    def pesquisar(opcao: str, dado_pesquisa: str) -> list:
        """
        Pesquisa por um documento em todo o arquivo, levando em conta o dado informado pelo usuário
        :param opcao: dado que será levado em conta para a pesquisa
        :param dado_pesquisa: valor do dado a ser pesquisado no arquivo
        :return: tupla contendo a estante e a caixa onde está localizado o documento
        """
        path = 'data/arquivo/'
        dirs = [(path + d) for d in os.listdir(path) if os.path.isdir(path + d)]

        files = []
        for d in dirs:
            for f in os.listdir(d):
                if os.path.isfile(d + '/' + f):
                    files.append(d + '/' + f)

        results = []
        for f in files:
            with open(f, 'r') as fin:
                if fin.read():
                    df = pd.read_csv(f, encoding='utf-8')
                else:
                    continue

            if opcao == 'Partes Interessadas':
                dado_pesquisa = dado_pesquisa.strip()
                while '  ' in dado_pesquisa:
                    dado_pesquisa = dado_pesquisa.replace('  ', ' ')
                for index, row in df.iterrows():
                    if dado_pesquisa in row[opcao]:
                        vec = f.split('/')
                        results.append([vec[-2], vec[-1], row['Assunto'], row['Partes Interessadas'],
                                        row['Numero de Protocolo'], row['Anexos'], row['Historico de Tramitacao']])

            elif opcao == 'Data de Insercao':
                d = dado_pesquisa.split('-')
                if d[0][0] == '0':
                    dado_pesquisa = f'{d[0][1]}-{d[1]}-{d[2]}'
                if d[1][0] == '0':
                    dado_pesquisa = f'{d[0]}-{d[1][1]}-{d[2]}'
                for index, row in df.iterrows():
                    for line in row['Historico de Tramitacao'].splitlines():
                        if dado_pesquisa in line:
                            vec = f.split('/')
                            results.append([vec[-2], vec[-1], row['Assunto'], row['Partes Interessadas'],
                                            row['Numero de Protocolo'], row['Anexos'], row['Historico de Tramitacao']])
                        elif 'Localizacao' in line:
                            break

            else:
                for index, row in df.iterrows():
                    if str(row[opcao]) == dado_pesquisa:
                        vec = f.split('/')
                        results.append([vec[-2], vec[-1], row['Assunto'], row['Partes Interessadas'],
                                        row['Numero de Protocolo'], row['Anexos'], row['Historico de Tramitacao']])

        if not results:
            raise Exception('Nenhum documento encontrado!')
        return results

    def get_numero_protocolo(self):
        return self.numero_protocolo

    def set_numero_protocolo(self, numero_protocolo):
        self.numero_protocolo = numero_protocolo

    def get_assunto(self):
        return self.assunto

    def set_assunto(self, assunto):
        self.assunto = assunto

    def get_partes_interessadas(self):
        return self.partes_interessadas

    def set_partes_interessadas(self, partes_interessadas):
        self.partes_interessadas = partes_interessadas
