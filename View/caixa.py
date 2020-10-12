from Model import caixa
import os


class Caixa:
    @staticmethod
    def adicionar():
        cx = caixa.Caixa(str(input('Estante da caixa: ')), str(input('Codigo da caixa: ')))

        if cx.verificar_existencia():
            raise Exception('Caixa ja existente!')

        cx.adicionar()
        print('Caixa adicionada ao arquivo!')
