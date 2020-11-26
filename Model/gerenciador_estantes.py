import pandas as pd

from Model import estante as est


class GerenciadorEstantes:
    def __init__(self, estantes):
        self.estantes = estantes

    def adicionar(self, codigo, disponibilidade):
        try:
            if not self.existe_estante(codigo):
                self.atualizar_banco_dados(codigo, disponibilidade)
                self.estantes.append(est.Estante(codigo, disponibilidade))
            else:
                raise Exception('Estante ja existente!')
        except Exception as e:
            raise e

    def existe_estante(self, codigo):
        try:
            self.get_estante(codigo)
            return True
        except:
            return False

    def possui_disponibilidade(self, codigo):
        if int(self.get_estante(codigo).get_disponibilidade()) > 0:
            return True
        return False

    def atualizar_disponibilidade(self, codigo):
        for estante in self.estantes:
            if estante.get_codigo() == codigo:
                disponibilidade = estante.get_disponibilidade()
                estante.set_disponibilidade(disponibilidade - 1)

        # TODO
        # df = pd.read_csv('data/arquivo/estante.csv', encoding='utf-8')
        # df[]

    @staticmethod
    def atualizar_banco_dados(codigo, disponibilidade):
        try:
            df = pd.DataFrame({'cod': [codigo],
                               'disponibilidade': [disponibilidade]})

            with open(f'data/arquivo/estante.csv', encoding='utf-8') as fin:
                if not fin.read():
                    df.to_csv(f'data/arquivo/estante.csv', index=False, encoding='utf-8')
                else:
                    df_caixa = pd.read_csv(f'data/arquivo/estante.csv', encoding='utf-8')
                    pd.concat([df, df_caixa]).to_csv(f'data/arquivo/estante.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar o banco de dados: {e}')

    def get_estante(self, codigo):
        for estante in self.estantes:
            if codigo == estante.get_codigo():
                return estante
        raise Exception('Estante não encontrada!')
