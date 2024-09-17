import pandas as pd

def carregar_dados(caminho_vias_cartao, caminho_transacoes):
    dados_via_cartao = pd.read_csv(caminho_vias_cartao)
    dados_transacoes = pd.read_csv(caminho_transacoes)
    return dados_via_cartao, dados_transacoes

def conciliacao(dados_via_cartao, dados_transacoes):
    transacoes_checadas = pd.merge(dados_transacoes, dados_via_cartao, on='STONE ID', how='left', indicator=True)

    transacoes_diferencas = transacoes_checadas[transacoes_checadas['_merge'] == 'left_only']
    transacoes_checadas = transacoes_checadas[transacoes_checadas['_merge'] == 'both']
    
    return transacoes_diferencas, transacoes_checadas
def gerar_relatorio(dados, nome_arquivo):
    dados.to_csv(nome_arquivo, index = False)
    print(f'Relatório gerado: {nome_arquivo}')

def main(caminho_vias_cartao, caminho_transacoes):
    dados_vias_cartao, dados_transacoes = carregar_dados(caminho_vias_cartao, caminho_transacoes)
    
