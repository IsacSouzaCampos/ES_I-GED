import pandas as pd
import os
from Model import estante as est, caixa as cx, documento as doc
from Model import gerenciador_estantes as ge, gerenciador_caixas as gc, gerenciador_documentos as gd


class Arquivo:
    def carregar_arquivo(self):
        estantes = []
        caixas = []
        documentos = []
        tables = ['estante', 'caixa', 'documento']

        for table in tables:
            if not os.path.exists(f'data/arquivo/{table}.csv'):
                open(f'data/arquivo/{table}.csv', 'x').close()

            with open(f'data/arquivo/{table}.csv') as fin:
                if not fin.read():
                    continue

            df = pd.read_csv(f'data/arquivo/{table}.csv', encoding='utf-8')
            for index, row in df.iterrows():
                if table == 'estante':
                    cod = row['cod']
                    disponibilidade = row['disponibilidade']
                    estantes.append(self.carregar_estante(str(cod), int(disponibilidade)))

                elif table == 'caixa':
                    cod_est = row['cod_est'].astype(str)
                    for estante in estantes:
                        if cod_est == str(estante.get_codigo()):
                            caixas.append(cx.Caixa(row['cod'].astype(str), estante))
                            break
                else:
                    cod_cx = row['cod_cx']
                    for caixa in caixas:
                        if str(cod_cx) == str(caixa.get_codigo()):
                            documentos.append(
                                doc.Documento(row['protocolo'], caixa, row['assunto'], row['partes interessadas'],
                                              row['historico'], row['anexos']))
                            break

        return ge.GerenciadorEstantes(estantes), gc.GerenciadorCaixas(caixas), gd.GerenciadorDocumentos(documentos)

    @staticmethod
    def carregar_estante(cod, disponibilidade):
        estante = est.Estante(cod, disponibilidade)
        with open('data/arquivo/caixa.csv', 'r') as fin:
            if not fin.read():
                return estante

        df = pd.read_csv('data/arquivo/caixa.csv', encoding='utf-8')

        caixas = []
        for index, row in df.iterrows():
            if row['cod_est'].astype(str) == cod:
                caixa = cx.Caixa(row['cod'], estante)
                caixas.append(caixa)
        estante.set_caixas(caixas)
        return estante
