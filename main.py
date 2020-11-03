from View import login, caixa, documento, estante
from Model import administrador
import pandas as pd


def main():
    # df = pd.read_csv('data/arquivo/A/0.csv', encoding='utf-8')
    # for index, row in df.iterrows():
    #     print(row['Historico de Tramitacao'])
    try:
        usuario_atual = login.LogIn().login()
    except Exception as e:
        print(e)
        return

    opcao = -1
    while opcao != 0:
        opcao = mostrar_interface()
        try:
            if opcao == 1:
                documento.Documento().adicionar()
            elif opcao == 2:
                caixa.Caixa().adicionar(usuario_atual)
            elif opcao == 3:
                documento.Documento().anexar(usuario_atual)
            elif opcao == 4:
                estante.Estante().adicionar(usuario_atual)
            elif opcao == 5:
                documento.Documento().listar()
            elif opcao == 6:
                documento.Documento().pesquisar()
            elif opcao == 7:
                documento.Documento().tramitar(usuario_atual)
        except Exception as e:
            print(e)


def mostrar_interface() -> int:
    print('=' * 20)
    print('[1] Adicionar documento')
    print('[2] Adicionar caixa ao arquivo')
    print('[3] Anexar documentos')
    print('[4] Adicionar estante ao arquivo')
    print('[5] Listar documentos de uma caixa')
    print('[6] Pesquisar documento')
    print('[7] Tramitar')
    print('[0] Sair')
    return int(input('Opcao: '))


if __name__ == '__main__':
    main()
