from uteis import login, arquivo


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
        if opcao == 1:
            print('ADICIONAR DOCUMENTO')
        elif opcao == 2:
            print('ANEXAR DOCUMENTO A PROCESSO')
        elif opcao == 3:
            arquivo.Arquivo().adicionar_estante()
        elif opcao == 4:
            print('PESQUISAR')


def mostrar_interface(interface):
    if interface == 'inicial':
        print('='*20)
        print('[1] Adicionar documento')
        print('[2] Anexar documento a processo')
        print('[3] Adicionar estante ao arquivo')
        print('[4] Pesquisar')
        print('[0] Sair')
        return int(input('Opcao: '))


if __name__ == '__main__':
    main()