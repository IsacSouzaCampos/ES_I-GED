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
        except Exception as e:
            raise Exception(e)

        print('Finalizado')

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
