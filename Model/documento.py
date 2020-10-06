import os


class Documento:
    def __init__(self, numero_protocolo=None, assunto=None, partes_interessadas=None):
        self.numero_protocolo = numero_protocolo
        self.assunto = assunto
        self.partes_interessadas = partes_interessadas

    @staticmethod
    def anexar(dados_documento, dados_processo):
        # dados[0] = protocolo; dados[1] = estante; dados[2] = caixa;
        try:
            with open(f'data/arquivo/{dados_processo[1]}/{dados_processo[2]}', 'r') as fin1,\
                    open(f'data/arquivo/{dados_documento[1]}/{dados_documento[2]}', 'r') as fin2:
                processos = [(p.replace('\n', '') + f':{dados_documento[0]}\n')
                             if p.split(':')[2].replace('\n', '') == dados_processo[0] else p for p in fin1.readlines()]
                documentos = [d for d in fin2.readlines() if d.split(':')[2].replace('\n', '') != dados_documento[0]]

            with open(f'data/arquivo/{dados_processo[1]}/{dados_processo[2]}', 'w') as fout1,\
                    open(f'data/arquivo/{dados_documento[1]}/{dados_documento[2]}', 'w') as fout2:
                fout1.writelines(processos)
                fout2.writelines(documentos)
        except Exception as e:
            raise e

    @staticmethod
    def pesquisar(i, valor_pesquisado):
        path = 'data/arquivo/'
        dirs = [(path + d) for d in os.listdir(path) if os.path.isdir(path + d)]

        file = []
        for d in dirs:
            for f in os.listdir(d):
                if os.path.isfile(d + '/' + f):
                    file.append(d + '/' + f)

        for f in file:
            with open(f, 'r') as fin:
                for line in fin.readlines():
                    if valor_pesquisado in line.split(':')[i].replace('\n', ''):
                        vec = f.split('/')
                        return vec[-2], vec[-1]

        raise Exception('Documento nao encontrado')

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
