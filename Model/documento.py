class Documento:
    def __init__(self, protocolo, codigo_caixa, assunto, partes_interessadas, historico_tramitacao, anexos=None):
        self.protocolo = protocolo
        self.codigo_caixa = codigo_caixa
        self.assunto = assunto
        self.partes_interessadas = partes_interessadas
        self.historico_tramitacao = historico_tramitacao
        self.anexos = anexos

    def imprimir(self, codigo_estante=None):
        print('*'*20)
        print(f'Estante: {codigo_estante}  -   '
              f'Caixa: {self.get_codigo_caixa()}')
        print('*' * 20)
        print(f'assunto: {self.get_assunto()}')
        print(f'partes interessadas: {self.get_partes_interessadas()}')
        print(f'protocolo: {self.get_protocolo()}')
        print(f'anexos: {self.get_anexos()}')
        print(f'Historico de Tramitacao: {self.get_historico_tramitacao()}')
        print('*' * 20)

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

    def get_protocolo(self):
        return self.protocolo

    def set_protocolo(self, protocolo):
        self.protocolo = protocolo

    def get_anexos(self):
        return self.anexos

    def set_anexos(self, anexos):
        self.anexos = anexos

    def get_historico_tramitacao(self):
        return self.historico_tramitacao

    def set_historico_tramitacao(self, historico):
        self.historico_tramitacao = historico
