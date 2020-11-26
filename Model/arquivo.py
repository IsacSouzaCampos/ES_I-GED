import pandas as pd
import os
from Model import estante as est, caixa as cx, documento as doc
from Model import gerenciador_estantes as ge, gerenciador_caixas as gc, gerenciador_documentos as gd


class Arquivo:
    @staticmethod
    def carregar_arquivo():
        estantes = []
        caixas = []
        documentos = []
        tables = ['estante', 'caixa', 'documento']

        for table in tables:
            if not os.path.exists(f'data/arquivo/{table}.csv'):
                os.mknod(f'data/arquivo/{table}.csv')

            with open(f'data/arquivo/{table}.csv') as fin:
                if not fin.read():
                    continue

            df = pd.read_csv(f'data/arquivo/{table}.csv', encoding='utf-8')
            for index, row in df.iterrows():
                if table == 'estante':
                    estantes.append(est.Estante(row['cod'], row['disponibilidade']))
                elif table == 'caixa':
                    caixas.append(cx.Caixa(row['cod'], row['cod_est']))
                else:
                    documentos.append(
                        doc.Documento(row['protocolo'], row['cod_cx'], row['assunto'], row['partes interessadas'],
                                      row['historico de tramitacao'], row['anexos']))

        return ge.GerenciadorEstantes(estantes), gc.GerenciadorCaixas(caixas), gd.GerenciadorDocumentos(documentos)
