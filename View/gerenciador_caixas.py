from Model import estante


class GerendiadorCaixas:
    @staticmethod
    def adicionar():
        try:
            codigo_estante = str(input('Código da estante: '))
            if True:  # est.existe_estante() ---> ARRUMAR DEPOIS QUE TERMINAR GERENCIADOR DE ESTANTES
                return str(input('Codigo da caixa: ')), codigo_estante
            else:
                raise Exception('Estante não encontrada!')

        except Exception as e:
            raise e
