import pandas as pd

# 1. Carrega a planilha para dentro de uma estrutura chamada DataFrame  (df)
# Se o seu arquivo for .csv, mude para: pd.read_csv('dados.csv')

df = pd.read_csv('Formulario de habitos alimentares.csv')

#print(df ) 

#print(df.info()) # mostra as informaçoes sobre o Dataframe, como número de linhas, colunas e tipo dados 

#print(df.head()) # mostra as primeiras linhas do dataframe 

#df.describe()   # mostra estatísticas descritivas das colunas numéricas do dataFrame

#print (df.describe()) # estatística descritivas das colunas numéricas do Data Frame

#print(df.drop_duplicates()) # Remove linhas duplicadas do data Frame e exibe o resultado

