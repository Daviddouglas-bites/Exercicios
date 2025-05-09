import pandas as pd
import re
import os
from collections import Counter

# Caminho do arquivo Excel
caminho_arquivo = r'C:\Users\Usuario\Downloads\destino\xls'

# Verifica se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print(f"Arquivo não encontrado: {caminho_arquivo}")
else:
    try:
        # Lê todas as planilhas
        xls = pd.ExcelFile(caminho_arquivo)

        # Expressão regular para valores monetários
        regex_monetario = re.compile(r'R?\$?\s?\d{1,3}(?:\.\d{3})*(?:,\d{2})')

        valores_encontrados = []

        # Itera por todas as planilhas e células
        for nome_planilha in xls.sheet_names:
            df = pd.read_excel(xls, sheet_name=nome_planilha, dtype=str)
            for coluna in df.columns:
                for valor in df[coluna].dropna():
                    matches = regex_monetario.findall(str(valor))
                    valores_encontrados.extend(matches)

        # Converte os valores para um formato numérico para ordenar
        def converte_valor(valor):
            # Remove 'R$', espaços e substitui '.' por '' e ',' por '.'
            valor = valor.replace('R$', '').replace(' ', '').replace('.', '').replace(',', '.')
            try:
                return float(valor)
            except ValueError:
                return 0.0  # Caso ocorra algum erro de conversão

        # Conta a quantidade de vezes que cada valor monetário apareceu
        valores_contados = Counter(valores_encontrados)

        # Ordena os valores do menor para o maior
        valores_ordenados = sorted(valores_contados.items(), key=lambda x: converte_valor(x[0]))

        # Exibe os resultados ordenados
        print("Valores monetários encontrados e suas contagens (ordenados do menor para o maior):")
        for valor, quantidade in valores_ordenados:
            print(f'{valor}: {quantidade} vez(es)')

    except Exception as e:
        print("Ocorreu um erro ao ler o arquivo:", e)
