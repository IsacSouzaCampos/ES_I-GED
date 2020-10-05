from Model import caixa
import os


class Caixa:
    @staticmethod
    def adicionar_caixa():
        estante = str(input('Estante da caixa: '))
        codigo = str(input('Codigo da caixa: '))

        cx = caixa.Caixa(estante, codigo)

        if cx.verificar_existencia():
            raise Exception('Caixa ja existente!')

        cx.adicionar()
        print('Caixa adicionada ao arquivo!')
