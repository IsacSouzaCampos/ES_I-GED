from Model import gerenciador_estantes
ger_est = gerenciador_estantes.GerenciadorEstantes()


class InterfaceUsuarioCaixas:
    @staticmethod
    def adicionar():
        try:
            codigo_estante = str(input('Código da estante: '))
            if ger_est.existe_estante(codigo_estante):
                return str(input('Codigo da caixa: ')), codigo_estante
            else:
                raise Exception('Estante não encontrada!')

        except Exception as e:
            raise e
