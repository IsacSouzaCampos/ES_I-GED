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
            data = date.today()
            documento.set_historico(f'Insercao: {data.day}-{data.month}-{data.year}\n'
                                               f'Localizacao: estante_{codigo_estante}-caixa_{codigo_caixa}')
            self.atualizar_csv_adicionar(documento, codigo_estante, codigo_caixa)
            self.documentos.append(documento)
        except Exception as e:
            raise Exception(e)

        print('Finalizado')

    def anexar(self, d1, d2, codigo_estante_d2, nome_usuario):
        try:
            documento_mais_antigo = self.documento_mais_antigo(d1, d2)
            if documento_mais_antigo.get_protocolo() == d1.get_protocolo():
                index = self.documentos.index(d2)
                del(self.documentos[index])
                documento_remover = d2
                documento_alterar = d1
            else:
                index = self.documentos.index(d1)
                del(self.documentos[index])
                documento_remover = d1
                documento_alterar = d2

            data = date.today()
            data_atual = f'{data.day}-{data.month}-{data.year}'
            nova_localizacao = f'estante_{codigo_estante_d2}-caixa_{d2.get_codigo_caixa()}'
            motivo = f'recebeu {documento_remover.get_protocolo()} como anexo'

            historico = d1.get_historico()
            historico += f'\n*********\nData: {data_atual}\nLocalizacao: {nova_localizacao}\nMotivo: ' \
                         f'{motivo}\nUsuario: {nome_usuario}'

            anexos = f'{d2.get_anexos()}/{d1.get_anexos()}/{d1.get_protocolo()}/'.replace(' ', '').replace('//', '/')
            print(f'anexos = {anexos}')

            partes_interessadas = ''
            for pi in d1.get_partes_interessadas().split('/'):
                partes_interessadas += f'{pi}/'
            for pi in d2.get_partes_interessadas().split('/'):
                partes_interessadas += f'{pi}/'
            partes_interessadas = partes_interessadas.replace(' ', '').replace('//', '/')
            print(f'partes interessadas: {partes_interessadas}')

            documento_alterar.set_codigo_caixa(d2.get_codigo_caixa())
            documento_alterar.set_partes_interessadas(partes_interessadas)
            documento_alterar.set_historico(historico)
            documento_alterar.set_anexos(anexos)

            self.atualizar_csv_anexar(documento_remover, documento_alterar)

        except Exception as e:
            raise e

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
                for line in documento.get_historico().splitlines():
                    if f'Insercao: {dado_pesquisado}' in line:
                        lista_documentos.append(documento)
                        break

        elif forma_pesquisa == 'assunto':
            for documento in self.documentos:
                if dado_pesquisado in str(documento.get_assunto()):
                    lista_documentos.append(documento)
                    break

        elif forma_pesquisa == 'protocolo':
            for documento in self.documentos:
                if dado_pesquisado in str(documento.get_protocolo()):
                    lista_documentos.append(documento)
                    break

        if not lista_documentos:
            raise Exception('Documento não encontrado!')

        return lista_documentos

    def listar_documentos_caixa(self, codigo_caixa):
        lista_documentos = []

        for documento in self.documentos:
            if str(documento.get_codigo_caixa()) == codigo_caixa:
                lista_documentos.append(documento)

        return lista_documentos

    def tramitar(self, protocolo, codigo_caixa, codigo_estante, motivo, nome_usuario):
        data = date.today()
        doc = self.pesquisar('protocolo', protocolo)[0]

        doc.set_codigo_caixa(codigo_caixa)
        historico = doc.get_historico()
        historico += '\n' + '*'*20 + f'\nData: {data.day}-{data.month}-{data.year}' \
                                     f'\nLocalizacao: estante_{codigo_estante}-caixa_{codigo_caixa}' \
                                     f'\nMotivo: {motivo}' \
                                     f'\nUsuario: {nome_usuario}'
        doc.set_codigo_caixa(codigo_caixa)
        doc.set_historico(historico)
        self.atualizar_csv_tramitar(doc)

        for documento in self.documentos:
            if documento.get_protocolo() == protocolo:
                index = self.documentos.index(documento)
                del(self.documentos[index])
                self.documentos.append(doc)
                break

    def existe_documento(self, documento):
        try:
            self.pesquisar('protocolo', documento.get_protocolo())
            return True
        except:
            return False

    @staticmethod
    def documento_mais_antigo(doc1, doc2):
        data_doc1 = ''
        data_doc2 = ''
        for line in doc1.get_historico().splitlines():
            if 'Insercao' in line:
                data_doc1 += line.split(': ')[-1]
                break
        for line in doc2.get_historico().splitlines():
            if 'Insercao' in line:
                data_doc2 += line.split(': ')[-1]
                break

        ano_doc1 = data_doc1.split('-')[2]
        ano_doc2 = data_doc2.split('-')[2]
        mes_doc1 = data_doc1.split('-')[1]
        mes_doc2 = data_doc2.split('-')[1]
        dia_doc1 = data_doc1.split('-')[0]
        dia_doc2 = data_doc2.split('-')[0]
        if ano_doc1 != ano_doc2:
            if ano_doc1 > ano_doc2:
                doc_mais_antigo = doc2
            else:
                doc_mais_antigo = doc1
        elif mes_doc1 != mes_doc2:
            if mes_doc1 > mes_doc2:
                doc_mais_antigo = doc2
            else:
                doc_mais_antigo = doc1
        elif dia_doc1 != dia_doc2:
            if dia_doc1 > dia_doc2:
                doc_mais_antigo = doc2
            else:
                doc_mais_antigo = doc1
        else:
            doc_mais_antigo = doc2

        return doc_mais_antigo

    @staticmethod
    def atualizar_csv_adicionar(documento, codigo_estante, codigo_caixa):
        try:
            df = pd.DataFrame({'protocolo': [documento.get_protocolo()],
                               'cod_cx': [codigo_caixa],
                               'assunto': [documento.get_assunto()],
                               'partes interessadas': [documento.get_partes_interessadas()],
                               'anexos': [' '],
                               'historico': [documento.get_historico()]})

            with open(f'data/arquivo/documento.csv') as fin:
                print(f'estante {codigo_estante}\ncaixa {codigo_caixa}')
                if not fin.read():
                    df.to_csv(f'data/arquivo/documento.csv', index=False, encoding='utf-8')
                else:
                    df_documento = pd.read_csv(f'data/arquivo/documento.csv', encoding='utf-8')
                    pd.concat([df, df_documento]).to_csv(f'data/arquivo/documento.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar banco de dados: {e}')

    def atualizar_csv_anexar(self, documento_remover, documento_alterar):
        df = pd.read_csv('data/arquivo/documento.csv', encoding='utf-8')
        item = df.loc[df['protocolo'].astype(str) == str(documento_remover.get_protocolo())]
        df = df.drop(item.index)
        item = df.loc[df['protocolo'].astype(str) == documento_alterar.get_protocolo()]
        df = df.drop(item.index)

        df_novo_documento = pd.DataFrame({'protocolo': [documento_alterar.get_protocolo()],
                                          'cod_cx': [documento_alterar.get_codigo_caixa()],
                                          'assunto': [documento_alterar.get_assunto()],
                                          'partes interessadas': [documento_alterar.get_partes_interessadas()],
                                          'anexos': [documento_alterar.get_anexos()],
                                          'historico': [documento_alterar.get_historico()]})

        pd.concat([df, df_novo_documento]).to_csv('data/arquivo/documento.csv', index=False, encoding='utf-8')

    @staticmethod
    def atualizar_csv_tramitar(doc):
        df = pd.read_csv('data/arquivo/documento.csv', encoding='utf-8')
        item = df.loc[df['protocolo'].astype(str) == doc.get_protocolo()]
        df = df.drop(item.index)

        df_novo = pd.DataFrame({'protocolo': [doc.get_protocolo()],
                                'cod_cx': [doc.get_codigo_caixa()],
                                'assunto': [doc.get_assunto()],
                                'partes interessadas': [doc.get_partes_interessadas()],
                                'anexos': [doc.get_anexos()],
                                'historico': [doc.get_historico()]})

        pd.concat([df, df_novo]).to_csv('data/arquivo/documento.csv', index=False, encoding='utf-8')
