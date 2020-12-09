import pandas as pd

from Model import administrador, login
from View import interface_usuario_caixas
iu_cx = interface_usuario_caixas.InterfaceUsuarioCaixas()


class GerenciadorCaixas:
    def __init__(self, caixas):
        self.caixas = caixas

    def adicionar(self, caixa, usuario):
        try:
            if self.existe_caixa(caixa.get_codigo()):
                # Caixa já existente!
                return 1

            if type(usuario) is administrador.Administrador:
                self.atualizar_csv_adicionar(caixa)
                self.caixas.append(caixa)
            else:
                nome_admin, senha_admin = iu_cx.pedir_dados_administrador()

                admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
                if type(admin) is administrador.Administrador:
                    self.atualizar_csv_adicionar(caixa)
                    self.caixas.append(caixa)
                else:
                    # Informações de administrador incorretas!
                    return 2

        except Exception as e:
            raise e

        # Caixa adicionada com êxito!
        return 0

    def remover(self, caixa, usuario):
        if self.existe_documento_na_caixa(caixa):
            # A caixa precisa estar vazia para ser removida!
            return 1

        if type(usuario) is not administrador.Administrador:
            nome_admin, senha_admin = iu_cx.pedir_dados_administrador()
            admin = login.LogIn().verificar_hierarquia(nome_admin, senha_admin)
            if type(admin) is not administrador.Administrador:
                # Informações de administrador incorretas!
                return 2

        self.atualizar_csv_remover(caixa)
        index = self.caixas.index(caixa)
        del (self.caixas[index])

        # Caixa removida com êxito!
        return 0

    @staticmethod
    def existe_documento_na_caixa(caixa):
        df = pd.read_csv('data/arquivo/documento.csv', encoding='utf-8')
        for index, row in df.iterrows():
            if str(row['cod_cx']) == str(caixa.get_codigo()):
                return True
        return False

    def mudar_localizacao_caixa(self, caixa, estante):
        for _caixa in self.caixas:
            if _caixa == caixa:
                temp = caixa
                index = self.caixas.index(caixa)
                del(self.caixas[index])
                temp.set_estante(estante)
                self.caixas.append(temp)
                self.atualizar_csv_mudar_localizacao(caixa, estante)
                break

        # Localização da caixa modificada com êxito!
        return 0

    @staticmethod
    def atualizar_csv_adicionar(caixa):
        try:
            df = pd.DataFrame({'cod': [caixa.get_codigo()],
                               'cod_est': [caixa.get_estante().get_codigo()]})

            with open(f'data/arquivo/caixa.csv', encoding='utf-8') as fin:
                if not fin.read():
                    df.to_csv(f'data/arquivo/caixa.csv', index=False, encoding='utf-8')
                else:
                    df_caixa = pd.read_csv(f'data/arquivo/caixa.csv', encoding='utf-8')
                    pd.concat([df, df_caixa]).to_csv(f'data/arquivo/caixa.csv', index=False, encoding='utf-8')

        except Exception as e:
            raise Exception(f'Erro ao atualizar o banco de dados: {e}')

    @staticmethod
    def atualizar_csv_remover(caixa):
        df = pd.read_csv('data/arquivo/caixa.csv', encoding='utf-8')
        item = df.loc[df['cod'].astype(str) == str(caixa.get_codigo())]
        df = df.drop(item.index)

        df.to_csv('data/arquivo/caixa.csv', index=False, encoding='utf-8')

    @staticmethod
    def atualizar_csv_mudar_localizacao(caixa, estante):
        df = pd.read_csv('data/arquivo/caixa.csv', encoding='utf-8')
        item = df.loc[df['cod'].astype(str) == str(caixa.get_codigo())]
        df = df.drop(item.index)

        df_novo = pd.DataFrame({'cod': [caixa.get_codigo()],
                                'cod_est': [estante.get_codigo()]})

        pd.concat([df, df_novo]).to_csv('data/arquivo/caixa.csv', index=False, encoding='utf-8')

    def existe_caixa(self, codigo):
        try:
            self.get_caixa(codigo)
            return True
        except:
            return False

    def get_caixa(self, codigo):
        for caixa in self.caixas:
            if str(codigo) == str(caixa.get_codigo()):
                return caixa
        raise Exception('Caixa não encontrada!')
