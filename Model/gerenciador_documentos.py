import pandas as pd
from datetime import date


class GerenciadorDocumentos:
    def __init__(self, documentos):
        self.documentos = documentos

    def adicionar(self, documento, codigo_estante):
        if self.existe_documento(documento):
            raise Exception('O protocolo informado já existe no arquivo!')

        codigo_caixa = documento.get_codigo_caixa()
        try:
            self.atualizar_banco_dados(documento, codigo_estante, codigo_caixa)
            self.documentos.append(documento)
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
    def atualizar_banco_dados(documento, codigo_estante, codigo_caixa):
        try:
            data = date.today()
            historico_tramitacao = f'Data: {data.day}-{data.month}-{data.year}\n' \
                                   f'Localizacao: estante_{codigo_estante}-caixa_{codigo_caixa}'

            df = pd.DataFrame({'protocolo': [documento.get_protocolo()],
                               'cod_cx': [codigo_caixa],
                               'assunto': [documento.get_assunto()],
                               'partes interessadas': [documento.get_partes_interessadas()],
                               'anexos': [' '],
                               'historico de tramitacao': [historico_tramitacao]})

            with open(f'data/arquivo/documento.csv', encoding='utf-8') as fin:
                print(f'estante {codigo_estante}\ncaixa {codigo_caixa}')
                if not fin.read():
                    df.to_csv(f'data/arquivo/documento.csv', index=False, encoding='utf-8')
                else:
                    df_documento = pd.read_csv(f'data/arquivo/documento.csv', encoding='utf-8')
                    pd.concat([df, df_documento]).to_csv(f'data/arquivo/documento.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar banco de dados: {e}')

    def pesquisar(self, opcao: str, dado_pesquisa: str):
        lista_documentos = []

        if opcao == 'Partes Interessadas':
            for documento in self.documentos:
                if dado_pesquisa in documento.get_partes_interessadas():
                    lista_documentos.append(documento)

        elif opcao == 'Data de Insercao':
            d = dado_pesquisa.split('-')
            if d[0][0] == '0':
                dado_pesquisa = f'{d[0][1]}-{d[1]}-{d[2]}'
            if d[1][0] == '0':
                dado_pesquisa = f'{d[0]}-{d[1][1]}-{d[2]}'
            for documento in self.documentos:
                for line in documento.get_historico_tramitacao():
                    if f'Inserção: {dado_pesquisa}' in line:
                        lista_documentos.append(documento)

        elif opcao == 'Assunto':
            for documento in self.documentos:
                if dado_pesquisa in documento.get_assunto():
                    lista_documentos.append(documento)

        elif opcao == 'Protocolo':
            for documento in self.documentos:
                if dado_pesquisa in documento.get_protocolo():
                    lista_documentos.append(documento)

        if not lista_documentos:
            raise Exception('Documento não encontrado!')

        return lista_documentos

    def existe_documento(self, documento):
        try:
            self.pesquisar('protocolo', documento.get_protocolo())
            return True
        except:
            return False
