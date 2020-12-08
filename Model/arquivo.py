import pandas as pd
import os
from Model import estante as est, caixa as cx, documento as doc
from Model import gerenciador_estantes as ge, gerenciador_caixas as gc, gerenciador_documentos as gd


class Arquivo:
    def carregar_arquivo(self):
        estantes = self.carregar_estantes()
        caixas = self.carregar_caixas()
        documentos = self.carregar_documentos()

        caixas, documentos = self.inserir_documentos_nas_caixas(caixas, documentos)
        estantes, caixas = self.inserir_caixas_nas_estantes(estantes, caixas)

        return ge.GerenciadorEstantes(estantes), gc.GerenciadorCaixas(caixas), gd.GerenciadorDocumentos(documentos)

    @staticmethod
    def carregar_estantes():
        estantes = []
        if not os.path.exists('data/arquivo/estante.csv'):
            open('data/arquivo/estante.csv', 'x').close()

        with open('data/arquivo/estante.csv') as fin:
            if fin.read():
                df = pd.read_csv('data/arquivo/estante.csv', encoding='utf-8')
                for index, row in df.iterrows():
                    estantes.append(est.Estante(row['cod'], row['disponibilidade']))

        return estantes

    @staticmethod
    def carregar_caixas():
        caixas = []
        if not os.path.exists('data/arquivo/caixa.csv'):
            open('data/arquivo/caixa.csv', 'x').close()

        with open('data/arquivo/caixa.csv') as fin:
            if fin.read():
                df = pd.read_csv('data/arquivo/caixa.csv', encoding='utf-8')
                for index, row in df.iterrows():
                    caixas.append(cx.Caixa(row['cod'], row['cod_est']))

        return caixas

    @staticmethod
    def carregar_documentos():
        documentos = []
        if not os.path.exists('data/arquivo/documento.csv'):
            open('data/arquivo/documento.csv', 'x').close()

        with open('data/arquivo/documento.csv') as fin:
            if fin.read():
                df = pd.read_csv('data/arquivo/documento.csv', encoding='utf-8')
                for index, row in df.iterrows():
                    documentos.append(doc.Documento(row['protocolo'], assunto=row['assunto'],
                                                    partes_interessadas=row['partes interessadas'],
                                                    historico=row['historico'], anexos=row['anexos']))

        return documentos

    @staticmethod
    def inserir_documentos_nas_caixas(caixas, documentos):
        df_documentos = pd.read_csv('data/arquivo/documento.csv', encoding='utf-8')
        for index, row in df_documentos.iterrows():
            for documento in documentos:
                if str(documento.get_protocolo()) == str(row['protocolo']):
                    for caixa in caixas:
                        if str(caixa.get_codigo()) == str(row['cod_cx']):
                            caixa.adicionar_documento(documento)
                            documento.set_caixa(caixa)

        return caixas, documentos

    @staticmethod
    def inserir_caixas_nas_estantes(estantes, caixas):
        df_caixas = pd.read_csv('data/arquivo/caixa.csv', encoding='utf-8')
        for index, row in df_caixas.iterrows():
            for caixa in caixas:
                if str(caixa.get_codigo()) == str(row['cod']):
                    for estante in estantes:
                        if str(estante.get_codigo()) == str(row['cod_est']):
                            estante.adicionar_caixa(caixa)
                            caixa.set_estante(estante)

        return estantes, caixas
