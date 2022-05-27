import os

diretorio = os.listdir()
pedidos = list()

for arquivo in diretorio:
    if arquivo.startswith('PHL'):
        pedidos.append(arquivo)
    else:
        None

def pharlab_pedido(file: str) -> str:
    with open(file, mode='r', encoding='utf8', errors='ignore') as arquivo:
        linha = arquivo.readline()

        while linha:

            if linha.startswith('01'):
                layout = linha[2:5]
                cnpj = linha[5:19]

            if linha.startswith('02'):
                pedido = linha[5:15]

            if linha.startswith('03'):
                tipoPagamento = linha[2:4]
                if tipoPagamento == '03':
                    condicao = ' - Prazo Especial.'
                elif tipoPagamento == '02':
                    condicao = ' - A prazo.'
                elif tipoPagamento == '01':
                    condicao = ' - A vista'
                else:
                    None
            linha = arquivo.readline()
        print('-' * 76)
        if len(file) == 47:
            print(f'Pedido: {pedido} Arquivo:  {file}|')
        else:
            print(f'Pedido: {pedido} Arquivo:  {file}    |')
        print('-' * 76)
        print(f'CNPJ: {cnpj}')
        print(f'Layout: {layout}')
        print(f'TpPagamento {tipoPagamento} {condicao}')


for pedido in arquivos:
    pharlab_pedido(pedido)