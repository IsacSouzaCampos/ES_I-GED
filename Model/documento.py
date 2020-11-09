import os
import pandas as pd
from datetime import date

from Model import estante, caixa


class Documento:
    def __init__(self, caixa=None, assunto=None, partes_interessadas=None, protocolo=None, anexos=None,
                 historico_tramitacao=''):
        self.caixa = caixa
        self.assunto = assunto
        self.partes_interessadas = partes_interessadas
        self.protocolo = protocolo
        self.anexos = anexos
        self.historico_tramitacao = historico_tramitacao

    def adicionar(self):
        try:
            self.pesquisar('Protocolo', self.get_protocolo())
            raise Exception('O protocolo informado já existe no arquivo!')
        except:
            pass

        codigo_estante = self.get_caixa().get_estante().get_codigo()
        codigo_caixa = self.get_caixa().get_codigo()
        try:
            data = date.today()
            historico_tramitacao = f'Data: {data.day}-{data.month}-{data.year}\n' \
                                   f'Localizacao: estante_{codigo_estante}-caixa_{codigo_caixa}'

            df2 = pd.DataFrame({'Assunto': [self.get_assunto()],
                                'Partes Interessadas': [self.get_partes_interessadas()],
                                'Protocolo': [self.get_protocolo()],
                                'Anexos': [' '],
                                'Historico de Tramitacao': [historico_tramitacao]})

            with open(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', encoding='utf-8') as fin:
                print(f'estante {codigo_estante}\ncaixa {codigo_caixa}')
                if not fin.read():
                    df2.to_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', index=False, encoding='utf-8')
                else:
                    df = pd.read_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', encoding='utf-8')
                    pd.concat([df, df2]).to_csv(f'data/arquivo/{codigo_estante}/{codigo_caixa}.csv', index=False,
                                                encoding='utf-8')

        except Exception as e:
            raise Exception(e)

        print('Finalizado')

    def anexar(self, protocolo1, protocolo2, usuario):
        """
        Anexa um documento a outro
        :param item1: contem os dados do documento a ser anexado (estante, caixa, protocolo)
        :param item2: contem os dados do documento a receber o anexo
        """
        documento1 = self.pesquisar('Protocolo', protocolo1)[0]
        documento2 = self.pesquisar('Protocolo', protocolo2)[0]

        estante1 = documento1.get_caixa().get_estante().get_codigo()
        caixa1 = documento1.get_caixa().get_codigo()
        estante2 = documento2.get_caixa().get_estante().get_codigo()
        caixa2 = documento2.get_caixa().get_codigo()

        try:
            df1 = pd.read_csv(f'data/arquivo/{estante1}/{caixa1}.csv', encoding='utf-8')
            df2 = pd.read_csv(f'data/arquivo/{estante2}/{caixa2}.csv', encoding='utf-8')

            data = date.today()
            df_documento1 = df1.loc[df1['Protocolo'].astype(str) == documento1.get_protocolo()]

            df1 = df1.drop(df_documento1.index)
            df1.to_csv(f'data/arquivo/{estante1}/{caixa1}.csv', index=False,
                       encoding='utf-8')

            df_documento1['Historico de Tramitacao'] += '\n***********************\n' \
                                                   f'Data: {data.day}-{data.month}-{data.year}\n' \
                                                   f'Localizacao: estante_{estante2}-caixa_{caixa2}\n' \
                                                   f'Motivo: anexado ao documento [{documento2.get_protocolo()}]\n' \
                                                   f'Usuario: {usuario.get_nome()}'

            df_documento2 = df2.loc[df2['Protocolo'].astype(str) == documento2.get_protocolo()]
            df_documento2['Anexos'] += f'[{documento1.get_protocolo()}]\n'.replace(' ', '')

            df2 = df2.drop(df_documento2.index)

            pd.concat([df2, df_documento1, df_documento2]).to_csv(f'data/arquivo/{estante2}/{caixa2}.csv', index=False,
                                                                  encoding='utf-8')
        except Exception as e:
            raise e

    @staticmethod
    def pesquisar(opcao: str, dado_pesquisa: str):
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
                    if dado_pesquisa.lower() in row[opcao].lower():
                        vec = f.split('/')
                        results.append([vec[-2], vec[-1].replace('.csv', ''), row['Assunto'],
                                        row['Partes Interessadas'], row['Protocolo'], row['Anexos'],
                                        row['Historico de Tramitacao']])

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
                            results.append([vec[-2], vec[-1].replace('.csv', ''), row['Assunto'],
                                            row['Partes Interessadas'], row['Protocolo'], row['Anexos'],
                                            row['Historico de Tramitacao']])
                        elif 'Localizacao' in line:
                            break

            else:
                for index, row in df.iterrows():
                    if str(row[opcao]) == dado_pesquisa:
                        vec = f.split('/')
                        results.append([vec[-2], vec[-1].replace('.csv', ''), row['Assunto'],
                                        row['Partes Interessadas'], row['Protocolo'], row['Anexos'],
                                        row['Historico de Tramitacao']])
        documentos = []
        for r in results:
            cx = caixa.Caixa(estante.Estante(r[0]), r[1])
            documentos.append(Documento(cx, r[2], r[3], r[4], r[5], r[6]))
        return documentos

    def tramitar(self, caixa_destino, motivo, usuario):
        origem_estante = self.get_caixa().get_estante().get_codigo()
        origem_caixa = self.get_caixa().get_codigo()

        destino_estante = caixa_destino.get_estante().get_codigo()
        try:
            df1 = pd.read_csv(f'data/arquivo/{origem_estante}/{origem_caixa}.csv', encoding='utf-8')
            df2 = pd.read_csv(f'data/arquivo/{destino_estante}/{caixa_destino.get_codigo()}.csv', encoding='utf-8')

            item = df1.loc[df1['Protocolo'].astype(str) == self.get_protocolo()]
            df1 = df1.drop(item.index)
            df1.to_csv(f'data/arquivo/{origem_estante}/{origem_caixa}.csv', index=False, encoding='utf-8')

            data = date.today()
            item['Historico de Tramitacao'] += '\n***********************\n' \
                                               f'Data: {data.day}-{data.month}-{data.year}\n' \
                                               f'Localizacao: estante_{destino_estante}-caixa_' \
                                               f'{caixa_destino.get_codigo()}\n' \
                                               f'Motivo: {motivo}\n' \
                                               f'Usuario: {usuario.get_nome()}'

            pd.concat([df2, item]).to_csv(f'data/arquivo/{destino_estante}/{caixa_destino.get_codigo()}.csv',
                                          index=False, encoding='utf-8')

        except Exception as e:
            raise e

    def get_caixa(self):
        return self.caixa

    def set_caixa(self, caixa):
        self.caixa = caixa

    def get_assunto(self):
        return self.assunto

    def set_assunto(self, assunto):
        self.assunto = assunto

    def get_partes_interessadas(self):
        return self.partes_interessadas

    def set_partes_interessadas(self, partes_interessadas):
        self.partes_interessadas = partes_interessadas

    def set_protocolo(self, protocolo):
        self.protocolo = protocolo

    def get_protocolo(self):
        return self.protocolo

    def get_anexos(self):
        return self.anexos

    def get_historico_tramitacao(self):
        return self.historico_tramitacao
