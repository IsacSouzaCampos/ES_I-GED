from View import login, interface_usuario_caixas, interface_usuario_documentos, interface_usuario_estantes
from Model import arquivo as arq, administrador, estante as est, caixa as cx, documento as doc

import os

os.system('rm data/arquivo/*.csv')

usuario = administrador.Administrador()
ger_est, ger_cx, ger_doc = arq.Arquivo().carregar_arquivo()
iu_est = interface_usuario_estantes.InterfaceUsuarioEstantes()
iu_cx = interface_usuario_caixas.InterfaceUsuarioCaixas()
iu_doc = interface_usuario_documentos.InterfaceUsuarioDocumentos()

for i in range(3):
    estante = est.Estante(str(i), 15)
    ger_est.adicionar(estante)
    for j in range(3):
        caixa = cx.Caixa(str(j + (i * 3)), estante)
        ger_cx.adicionar(caixa, usuario)
        for k in range(3):
            s = str(k + ((j + (i * 3)) * 3))
            ger_doc.adicionar(doc.Documento(s, caixa, s, s, '', ''))


def main():
    opcao = -1
    while opcao != 0:
        opcao = mostrar_interface()
        try:
            if opcao == 1:
                adicionar_estante()
            elif opcao == 2:
                remover_estante()
            elif opcao == 3:
                adicionar_caixa()
            elif opcao == 4:
                remover_caixa()
            elif opcao == 5:
                mudar_localizacao_caixa()
            elif opcao == 6:
                adicionar_documento()
            elif opcao == 7:
                remover_documento()
            elif opcao == 8:
                anexar_documentos()
            elif opcao == 9:
                listar_documentos_caixa()
            elif opcao == 10:
                pesquisar_documento()
            elif opcao == 11:
                tramitar()
        except Exception as e:
            print(e)


def mostrar_interface() -> int:
    print('=' * 20)
    print('[1] Adicionar estante')
    print('[2] Remover estante')
    print('[3] Adicionar caixa')
    print('[4] Remover caixa')
    print('[5] Mudar localização de uma caixa')
    print('[6] Adicionar documento')
    print('[7] Remover documento')
    print('[8] Anexar documentos')
    print('[9] Listar documentos de uma caixa')
    print('[10] Pesquisar documento')
    print('[11] Tramitar')
    print('[0] Sair')
    return int(input('Opcao: '))


def adicionar_estante():
    codigo, disponibilidade = iu_est.adicionar(usuario)
    estante = est.Estante(codigo, disponibilidade)
    ger_est.adicionar(estante)


def remover_estante():
    codigo = iu_est.remover()
    estante = ger_est.get_estante(codigo)
    ger_est.remover(estante, usuario)


def adicionar_caixa():
    codigo, codigo_estante = iu_cx.adicionar()
    if ger_est.existe_estante(codigo_estante):
        estante = ger_est.get_estante(codigo_estante)
        if int(estante.get_disponibilidade()) > 0:
            caixa = cx.Caixa(codigo, estante)
            ger_cx.adicionar(caixa, usuario)
            disponibilidade = ger_est.get_estante(codigo_estante).get_disponibilidade() - 1
            ger_est.atualizar_csv_disponibilidade(codigo_estante, disponibilidade)
        else:
            print('Estante indisponivel no momento!')
    else:
        print('Estante nao encontrada!')


def remover_caixa():
    codigo = iu_cx.remover()
    caixa = ger_cx.get_caixa(codigo)
    ger_cx.remover(caixa, usuario)
    estante = caixa.get_estante()
    codigo_estante = estante.get_codigo()
    disponibilidade = estante.get_disponibilidade() + 1
    ger_est.atualizar_csv_disponibilidade(codigo_estante, disponibilidade)


def mudar_localizacao_caixa():
    codigo, cod_proxima_estante = iu_cx.mudar_localizacao_caixa()

    caixa = ger_cx.get_caixa(codigo)
    proxima_estante = ger_est.get_estante(cod_proxima_estante)

    estante_anterior = caixa.get_estante()
    cod_estante_anterior = estante_anterior.get_codigo()

    ger_cx.mudar_localizacao_caixa(caixa, proxima_estante)

    disponibilidade_estante_anterior = estante_anterior.get_disponibilidade() + 1
    disponibilidade_proxima_estante = proxima_estante.get_disponibilidade() - 1

    ger_est.atualizar_csv_disponibilidade(cod_estante_anterior, disponibilidade_estante_anterior)
    ger_est.atualizar_csv_disponibilidade(cod_proxima_estante, disponibilidade_proxima_estante)


def adicionar_documento():
    protocolo, codigo_caixa, assunto, partes_interessadas, historico = iu_doc.adicionar()
    caixa = ger_cx.get_caixa(codigo_caixa)
    documento = doc.Documento(protocolo, caixa, assunto, partes_interessadas, historico)
    ger_doc.adicionar(documento)


def remover_documento():
    protocolo = iu_doc.remover()
    documento = ger_doc.pesquisar('protocolo', protocolo)[0]
    ger_doc.remover(documento, usuario)


def anexar_documentos():
    protocolo1, protocolo2 = iu_doc.anexar()
    documento1 = ger_doc.pesquisar('protocolo', protocolo1)[0]
    documento2 = ger_doc.pesquisar('protocolo', protocolo2)[0]
    codigo_caixa_d2 = documento2.get_caixa().get_codigo()
    caixa_d2 = ger_cx.get_caixa(codigo_caixa_d2)
    codigo_estante_d2 = caixa_d2.get_estante().get_codigo()
    nome_usuario = usuario.get_nome()
    ger_doc.anexar(documento1, documento2, codigo_estante_d2, nome_usuario)


def listar_documentos_caixa():
    codigo_caixa = iu_doc.listar_documentos_caixa()
    try:
        ger_cx.get_caixa(codigo_caixa)
    except Exception as e:
        print(e)
    documentos = ger_doc.listar_documentos_caixa(codigo_caixa)
    for documento in documentos:
        caixa = ger_cx.get_caixa(documento.get_caixa().get_codigo())
        codigo_estante = caixa.get_estante().get_codigo()
        documento.imprimir(codigo_estante)


def pesquisar_documento():
    forma_pesquisa, dado_pesquisado = iu_doc.pesquisar()
    documentos = ger_doc.pesquisar(forma_pesquisa, dado_pesquisado)
    for documento in documentos:
        codigo_estante = documento.get_caixa().get_estante().get_codigo()
        documento.imprimir(codigo_estante)


def tramitar():
    protocolo, codigo_caixa, motivo = iu_doc.tramitar()
    caixa = ger_cx.get_caixa(codigo_caixa)
    estante = caixa.get_estante()
    nome_usuario = usuario.get_nome()
    ger_doc.tramitar(protocolo, caixa, estante, motivo, nome_usuario)


if __name__ == '__main__':
    main()
