import pandas as pd

def carregar_dados(caminho_vias_cartao, caminho_transacoes):
    dados_via_cartao = pd.read_csv(caminho_vias_cartao)
    dados_transacoes = pd.read_csv(caminho_transacoes)
    return dados_via_cartao, dados_transacoes

def conciliacao(dados_via_cartao, dados_transacoes):
    transacoes_checadas = pd.merge(dados_transacoes, dados_via_cartao, on='STONE_ID', how='left', indicator=True)

    transacoes_diferencas = transacoes_checadas[transacoes_checadas['_merge'] == 'left_only']
    transacoes_checadas = transacoes_checadas[transacoes_checadas['_merge'] == 'both']
    
    return transacoes_diferencas, transacoes_checadas
def gerar_relatorio(dados, nome_arquivo):
    dados.to_csv(nome_arquivo, index = False)
    print(f'Relatório gerado: {nome_arquivo}')

def main(caminho_vias_cartao, caminho_transacoes):
    dados_vias_cartao, dados_transacoes = carregar_dados(caminho_vias_cartao, caminho_transacoes)
    transacoes_diferencas, transacoes_checadas = conciliacao(dados_vias_cartao, dados_transacoes)
    gerar_relatorio(transacoes_diferencas, 'transacoes_diferencas.csv')
    gerar_relatorio(transacoes_checadas, 'transacoes_checadas.csv')
    print(f'Diferencas encontradas: {transacoes_diferencas}')
    print(f'\nTransações concialiadas com sucesso: {transacoes_checadas}')

if __name__ == '__main__':
    caminho_vias_cartao = "C:\\Users\\jpara\\Desktop\\Lista de vendas 01-08-2024 - 31-08-2024.csv"
    caminho_transacoes = "C:\\Users\\jpara\\Downloads\\relatorio-recebimentos-20240801-20240831-39d7a1cdff834cb2a7a8885d77576c9500f74f96.csv"
    main(caminho_vias_cartao, caminho_transacoes)