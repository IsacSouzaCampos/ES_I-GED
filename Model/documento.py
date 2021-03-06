class Documento:
    def __init__(self, protocolo, caixa, assunto, partes_interessadas, historico, anexos=''):
        self.protocolo = protocolo
        self.caixa = caixa
        self.assunto = assunto
        self.partes_interessadas = partes_interessadas
        self.historico = historico
        self.anexos = anexos

    def get_caixa(self):
        return self.caixa

    def set_caixa(self, caixa):
        self.caixa = caixa

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

    def get_historico(self):
        return self.historico

    def set_historico(self, historico):
        self.historico = historico
