from Model import estante, documento
import os


class Documento:
    @staticmethod
    def adicionar_documento():
        print('='*20)
        assunto = str(input('Assunto: '))
        partes_interessadas_temp = str(input('Partes Interessadas (ex.: nome1 sobrenome1, nome2 sobrenome2): '))
        numero_protocolo = str(input('Numero de Protocolo: '))
        codigo_estante = str(input('Codigo da Estante: '))
        codigo_caixa = str(input('Codigo da Caixa: '))

        partes_interessadas_temp = partes_interessadas_temp.split(',')
        partes_interessadas = []
        for p in partes_interessadas_temp:
            partes_interessadas.append(p.strip().replace(' ', '_'))
        try:
            with open(f'data/arquivo/{codigo_estante}/{codigo_caixa}', 'r') as fin:
                dados_documentos = fin.readlines()
            dados_documentos.append(f'{assunto}:{partes_interessadas}:{numero_protocolo}\n')
            with open(f'data/arquivo/{codigo_estante}/{codigo_caixa}', 'w') as fout:
                fout.writelines(dados_documentos)
        except Exception:
            raise Exception('Nao foi possivel adicionar o documento')

        print('Finalizado')

    @staticmethod
    def anexar():
        print('*'*20)
        print('\nDADOS DO DOCUMENTO')
        protocolo_documento = str(input('Protocolo: '))
        estante_documento = str(input('Estante: '))
        caixa_documento = str(input('Caixa: '))

        print('\nDADOS DO PROCESSO')
        protocolo_processo = str(input('Protocolo: '))
        estante_processo = str(input('Estante: '))
        caixa_processo = str(input('Caixa: '))

        dados_documento = (protocolo_documento, estante_documento, caixa_documento)
        dados_processo = (protocolo_processo, estante_processo, caixa_processo)
        try:
            documento.Documento().anexar(dados_documento, dados_processo)
        except Exception as e:
            print(e)

    @staticmethod
    def listar_documentos():
        codigo_estante = str(input('Codigo da estante: '))
        codigo_caixa = str(input('Codigo da caixa: '))
        if not estante.Estante().existe_estante(codigo_estante):
            raise Exception('Estante nao existente')
        if codigo_caixa not in os.listdir(f'data/arquivo/{codigo_estante}'):
            raise Exception('Caixa nao existente')

        print('*'*20)
        print(f'Documentos [Estante: {codigo_estante}; Caixa: {codigo_caixa}]')
        with open(f'data/arquivo/{codigo_estante}/{codigo_caixa}', 'r') as fin:
            for line in fin.readlines():
                infos = line.split(':')
                print('*'*20)
                print(f'Assunto: {infos[0]}')
                partes_interessadas = infos[1].replace('[', '').replace(']', '').replace('\'', '').replace('_', ' ')\
                    .split(',')
                print('Partes Interessadas: ' + ','.join(partes_interessadas))
                print(f'Protocolo: {infos[2]}')
