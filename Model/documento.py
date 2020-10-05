from Model import estante
import os
class Documento:
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
