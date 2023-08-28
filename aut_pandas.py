import pandas as pd 

tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

# Atualizar o multiplicador

tabela.loc[tabela["Tipo"]=="Serviço", "Multiplicador Imposto"] = 1.5

# Fazer a conta do Preço Base Reais

tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

tabela.to_excel("ProdutosPandas.xlsx", index=False)