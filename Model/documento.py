import pandas as pd
from datetime import date

from Model import estante, caixa


class Documento:
    def __init__(self, protocolo, codigo_caixa, assunto, partes_interessadas, historico_tramitacao, anexos=None):
        self.protocolo = protocolo
        self.codigo_caixa = codigo_caixa
        self.assunto = assunto
        self.partes_interessadas = partes_interessadas
        self.historico_tramitacao = historico_tramitacao
        self.anexos = anexos

    def tramitar(self, caixa_destino, motivo, usuario):
        estante_origem = self.get_codigo_caixa().get_estante().get_codigo()
        caixa_origem = self.get_codigo_caixa().get_codigo()

        estante_destino = caixa_destino.get_estante().get_codigo()
        try:
            df1 = pd.read_csv(f'data/arquivo/{estante_origem}/{caixa_origem}.csv', encoding='utf-8')
            df2 = pd.read_csv(f'data/arquivo/{estante_destino}/{caixa_destino.get_codigo()}.csv', encoding='utf-8')

            item = df1.loc[df1['Protocolo'].astype(str) == self.get_protocolo()]
            df1 = df1.drop(item.index)
            df1.to_csv(f'data/arquivo/{estante_origem}/{caixa_origem}.csv', index=False, encoding='utf-8')

            data = date.today()
            item['Historico de Tramitacao'] += '\n***********************\n' \
                                               f'Data: {data.day}-{data.month}-{data.year}\n' \
                                               f'Localizacao: estante_{estante_destino}-caixa_' \
                                               f'{caixa_destino.get_codigo()}\n' \
                                               f'Motivo: {motivo}\n' \
                                               f'Usuario: {usuario.get_nome()}'

            pd.concat([df2, item]).to_csv(f'data/arquivo/{estante_destino}/{caixa_destino.get_codigo()}.csv',
                                          index=False, encoding='utf-8')

        except Exception as e:
            raise e

    def get_codigo_caixa(self):
        return self.codigo_caixa

    def set_codigo_caixa(self, codigo_caixa):
        self.codigo_caixa = codigo_caixa

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
