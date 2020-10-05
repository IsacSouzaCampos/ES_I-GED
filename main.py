from Model import estante, documento
from View import login


def main():
    try:
        login.LogIn().login()
    except Exception as e:
        print(e)
        return

    opcao = -1
    interface = 'inicial'
    while opcao != 0:
        opcao = mostrar_interface(interface)
        try:
            if opcao == 1:
                documento.Documento().adicionar_documento()
            elif opcao == 2:
                print('ANEXAR DOCUMENTO')
            elif opcao == 3:
                estante.Estante().adicionar_estante()
            elif opcao == 4:
                documento.Documento().listar_documentos()
            elif opcao == 5:
                print('PESQUISAR')
        except Exception as e:
            print(e)


def mostrar_interface(interface):
    if interface == 'inicial':
        print('='*20)
        print('[1] Adicionar documento')
        print('[2] Anexar documento a processo')
        print('[3] Adicionar estante ao arquivo')
        print('[4] Listar documentos de uma caixa')
        print('[5] Pesquisar')
        print('[0] Sair')
        return int(input('Opcao: '))


if __name__ == '__main__':
    main()
