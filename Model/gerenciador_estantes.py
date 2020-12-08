import pandas as pd

from Model import estante as est


class GerenciadorEstantes:
    def __init__(self, estantes):
        self.estantes = estantes

    def adicionar(self, estante):
        try:
            if not self.existe_estante(estante.get_codigo()):
                self.atualizar_csv_adicionar(estante)
                self.estantes.append(estante)
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

    def inserir_caixa_na_estante(self, estante, caixa):
        for _estante in self.estantes:
            if estante == _estante:
                temp = _estante
                index = self.estantes.index(_estante)
                del(self.estantes[index])
                break
        temp.adicionar_caixa(caixa)
        self.estantes.append(temp)

    def atualizar_csv_disponibilidade(self, codigo):
        disponibilidade = int()
        for estante in self.estantes:
            if str(estante.get_codigo()) == str(codigo):
                disponibilidade = int(estante.get_disponibilidade())
                estante.set_disponibilidade(disponibilidade - 1)

        df = pd.read_csv('data/arquivo/estante.csv', encoding='utf-8')
        df.loc[df['cod'].astype(str) == str(codigo), ['disponibilidade']] = disponibilidade - 1
        df.to_csv('data/arquivo/estante.csv', index=False, encoding='utf-8')

    @staticmethod
    def atualizar_csv_adicionar(estante):
        try:
            df = pd.DataFrame({'cod': [estante.get_codigo()],
                               'disponibilidade': [estante.get_disponibilidade()]})

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
            if str(codigo) == str(estante.get_codigo()):
                return estante
        raise Exception('Estante não encontrada!')
