class Documento:
    def __init__(self, numero_protocolo=None, assunto=None, partes_interessadas=None):
        self.numero_protocolo = numero_protocolo
        self.assunto = assunto
        self.partes_interessadas = partes_interessadas

    @staticmethod
    def adicionar_documento():
        print('='*20)
        assunto = str(input('Assunto: '))
        partes_interessadas_temp = str(input('Partes Interessadas (ex.: nome1 sobrenome1, nome2 sobrenome2): '))
        numero_protocolo = str(input('Numero de Protocolo: '))
        codigo_estante = str(input('Codigo da Estante: '))
        codigo_caixa = str(input('Codigo da Caixa: '))

        partes_interessadas_temp = partes_interessadas_temp.split(',')
        partes_interessadas = []
        for p in partes_interessadas_temp:
            partes_interessadas.append(p.strip().replace(' ', '_'))
        try:
            with open(f'data/arquivo/{codigo_estante}/{codigo_caixa}', 'r') as fin:
                dados_documentos = fin.readlines()
            dados_documentos.append(f'{assunto}:{partes_interessadas}:{numero_protocolo}\n')
            with open(f'data/arquivo/{codigo_estante}/{codigo_caixa}', 'w') as fout:
                fout.writelines(dados_documentos)
        except Exception:
            raise Exception('Nao foi possivel adicionar o documento')

        print('Finalizado')

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
