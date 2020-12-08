class InterfaceUsuarioCaixas:
    @staticmethod
    def adicionar():
        codigo_estante = str(input('Código da estante: '))
        return str(input('Codigo da caixa: ')), codigo_estante

    @staticmethod
    def remover():
        return str(input('Código da caixa: '))

    @staticmethod
    def mudar_localizacao_caixa():
        return str(input('Código da caixa: ')), str(input('Nova estante: '))
