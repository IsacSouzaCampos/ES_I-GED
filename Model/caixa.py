import os


class Caixa:
    def __init__(self, codigo, estante=None, documentos=[]):
        self.codigo = codigo
        self.estante = estante
        self.documentos = documentos

    def adicionar_documento(self, documento):
        self.documentos.append(documento)

    def numero_documentos(self):
        return len(self.documentos)

    def get_estante(self):
        return self.estante

    def set_estante(self, estante):
        self.estante = estante

    def get_codigo(self):
        return self.codigo

    def set_codigo(self, codigo):
        self.codigo = codigo

    def get_documentos(self):
        return self.documentos

    def set_documentos(self, documentos):
        self.documentos = documentos
