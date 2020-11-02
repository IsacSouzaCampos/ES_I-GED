from Model import caixa, estante, administrador


class Caixa:
    @staticmethod
    def adicionar(usuario):
        try:
            est = estante.Estante(str(input('Estante da caixa: ')))
            if est.existe_estante():
                cx = caixa.Caixa(est.get_codigo(), str(input('Codigo da caixa: ')))
                cx.adicionar(usuario)
            else:
                raise Exception('Estante não encontrada!')

            print(f'Caixa {cx.get_codigo()} adicionada à estante {cx.get_estante()}!')

        except Exception as e:
            raise e
