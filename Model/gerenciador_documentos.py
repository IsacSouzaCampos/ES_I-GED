import pandas as pd
from datetime import date

from Model import documento as doc


class GerenciadorDocumentos:
    def __init__(self, documentos):
        self.documentos = documentos

    def adicionar(self, documento, codigo_estante):
        if self.existe_documento(documento):
            raise Exception('O protocolo informado já existe no arquivo!')

        codigo_caixa = documento.get_codigo_caixa()
        try:
            data = date.today()
            documento.set_historico_tramitacao(f'Inserção: {data.day}-{data.month}-{data.year}\n'
                                               f'Localizacao: estante_{codigo_estante}-caixa_{codigo_caixa}')
            self.atualizar_csv_adicionar(documento, codigo_estante, codigo_caixa)
            self.documentos.append(documento)
        except Exception as e:
            raise Exception(e)

        print('Finalizado')

    def anexar(self, d1, d2, nome_usuario):
        try:
            data = date.today()
            data_atual = f'{data.day}-{data.month}-{data.year}'
            nova_localizacao = f'estante_{d2.get_codigo_caixa().get_codigo_estante()}-caixa_{d2.get_codigo_caixa()}'
            motivo = f'anexado ao documento {d2.get_protocolo()}'

            ht_d1 = f'\n*********\nData: {data_atual}\nLocalizacao: {nova_localizacao}\nMotivo: ' \
                      f'{motivo}\nUsuario: {nome_usuario}'

            novos_anexos_d1 = [d2.get_protocolo(), d2.get_anexos()]
            novos_anexos_d2 = [d1.get_protocolo(), d1.get_anexos()]

            self.atualizar_csv_tramitar(d1, d2, ht_d1, novos_anexos_d1, novos_anexos_d2)

            d1.set_codigo_caixa(d2.get_codigo_caixa())
            d1.set_historico_tramitacao(d1.get_historico_tramitacao() + ht_d1)
            d1.set_anexos(list(d1.get_anexos()).append(novos_anexos_d1))

            d2.set_anexos(list(d2.get_anexos()).append(novos_anexos_d2))

            cont = 0
            for i in range(len(self.documentos)):
                if str(self.documentos[i].get_protocolo()) == str(d1.get_protocolo()):
                    self.documentos[i] = d1
                    cont += 1
                if str(self.documentos[i].get_protocolo()) == str(d2.get_protocolo()):
                    self.documentos[i] = d2
                    cont += 1
                if cont == 2:
                    break

        except Exception as e:
            raise e

    @staticmethod
    def atualizar_csv_adicionar(documento, codigo_estante, codigo_caixa):
        try:
            df = pd.DataFrame({'protocolo': [documento.get_protocolo()],
                               'cod_cx': [codigo_caixa],
                               'assunto': [documento.get_assunto()],
                               'partes interessadas': [documento.get_partes_interessadas()],
                               'anexos': [' '],
                               'historico de tramitacao': [documento.get_historico_tramitacao()]})

            with open(f'data/arquivo/documento.csv', encoding='utf-8') as fin:
                print(f'estante {codigo_estante}\ncaixa {codigo_caixa}')
                if not fin.read():
                    df.to_csv(f'data/arquivo/documento.csv', index=False, encoding='utf-8')
                else:
                    df_documento = pd.read_csv(f'data/arquivo/documento.csv', encoding='utf-8')
                    pd.concat([df, df_documento]).to_csv(f'data/arquivo/documento.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar banco de dados: {e}')

    @staticmethod
    def atualizar_csv_tramitar(d1, d2, ht_d1, novos_anexos_d1, novos_anexos_d2):
        df = pd.read_csv(f'data/arquivo/documento.csv', encoding='utf-8')

        df.loc[df['protocolo'].astype(str) == d1.get_protocolo(), df['historico de tramitacao']] += ht_d1
        list(df.loc[df['protocolo'].astype(str) == d1.get_protocolo(), df['anexos']]).append(novos_anexos_d1)
        list(df.loc[df['protocolo'].astype(str) == d2.get_protocolo(), df['anexos']]).append(novos_anexos_d2)

    def pesquisar(self, forma_pesquisa, dado_pesquisado):
        lista_documentos = []

        if forma_pesquisa == 'partes interessadas':
            for documento in self.documentos:
                if dado_pesquisado in documento.get_partes_interessadas():
                    lista_documentos.append(documento)

        elif forma_pesquisa == 'data de insercao':
            d = dado_pesquisado.split('-')
            if d[0][0] == '0':
                dado_pesquisado = f'{d[0][1]}-{d[1]}-{d[2]}'
            if d[1][0] == '0':
                dado_pesquisado = f'{d[0]}-{d[1][1]}-{d[2]}'
            for documento in self.documentos:
                for line in documento.get_historico_tramitacao():
                    if f'Inserção: {dado_pesquisado}' in line:
                        lista_documentos.append(documento)

        elif forma_pesquisa == 'assunto':
            for documento in self.documentos:
                if dado_pesquisado in documento.get_assunto():
                    lista_documentos.append(documento)

        elif forma_pesquisa == 'protocolo':
            for documento in self.documentos:
                if dado_pesquisado in documento.get_protocolo():
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
