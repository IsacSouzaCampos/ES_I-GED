class Documento:
    def __init__(self, numero_protocolo=None):
        self.numero_protocolo = numero_protocolo

    def get_numero_protocolo(self):
        return self.numero_protocolo

    def set_numero_protocolo(self, numero_protocolo):
        self.numero_protocolo = numero_protocolo
