from View import login, caixa, documento, estante


def main():
    try:
        usuario_atual = login.LogIn().login()
    except Exception as e:
        print(e)
        return

    opcao = -1
    interface = 'inicial'
    while opcao != 0:
        opcao = mostrar_interface(interface)
        try:
            if opcao == 1:
                documento.Documento().adicionar()
            elif opcao == 2:
                caixa.Caixa().adicionar()
            elif opcao == 3:
                documento.Documento().anexar()
            elif opcao == 4:
                estante.Estante().adicionar(usuario_atual)
            elif opcao == 5:
                documento.Documento().listar()
            elif opcao == 6:
                documento.Documento().pesquisar()
        except Exception as e:
            print(e)


def mostrar_interface(interface):
    if interface == 'inicial':
        print('='*20)
        print('[1] Adicionar documento')
        print('[2] Adicionar caixa ao arquivo')
        print('[3] Anexar documento a processo')
        print('[4] Adicionar estante ao arquivo')
        print('[5] Listar documentos de uma caixa')
        print('[6] Pesquisar documento')
        print('[0] Sair')
        return int(input('Opcao: '))


if __name__ == '__main__':
    main()
