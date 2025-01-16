import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats
import streamlit as st

st.title("Meu Projeto sobre Analise de vendas de jogos")
st.header('Descrição do projeto')

st.write('Você trabalha para a loja online Ice, que vende videogames no mundo todo. As avaliações de usuários e especialistas, gêneros, plataformas (por exemplo, Xbox ou PlayStation) e dados históricos sobre vendas de jogos estão disponíveis em fontes abertas. Você precisa identificar padrões que determinam se um jogo tem sucesso ou não. Isso vai permitir que você identifique possíveis sucessos e planeje campanhas publicitárias.')
st.write('Os dados disponibilizados remontam a 2016. Vamos imaginar que estamos em dezembro de 2016 e você está planejando uma campanha para 2017.')
st.write('O conjunto de dados contém uma coluna de "rating" (classificação) que armazena a classificação ESRB de cada jogo. O Entertainment Software Rating Board avalia o conteúdo de um jogo e atribui uma classificação etária, como Teen (Adolescente) ou Mature (Adulto).')


st.header("Lendo as 10 primeiras linhas do DF")

df_games = pd.read_csv('games.csv')
print(df_games.head(10))

st.header("Deixando todas as letras iniciais das colunas em minusculas")

df_games.columns = df_games.columns.str.lower()
print(df_games)

st.header("Alterando os tipo de dados das colunas e substituindo valores ausentes")


df_games['user_score'] = df_games['user_score'].replace('tbd', '0')
df_games['user_score'] = df_games['user_score'].astype(float)
df_games['year_of_release'] = df_games['year_of_release'].astype('Int64').astype(str)
df_games['year_of_release'] = df_games['year_of_release'].fillna('desconhecido')
df_games['year_of_release'] = pd.to_numeric(df_games['year_of_release'], errors='coerce')
df_games = df_games.dropna(subset=['year_of_release'])
df_games

st.header("Verificando valores nulos e somando-os")

df_games.isna().sum()


st.header("Substituindo os valores ausentes das colunas categoricas")

df_games.dropna(subset=['name', 'genre'], inplace=True)
df_games.fillna({'rating': 'desconhecido'}, inplace=True)


df_games['total_sales'] = df_games[['na_sales',  'eu_sales', 'jp_sales', 'other_sales']].sum(axis=1)
df_games['total_sales'] = df_games['total_sales'].astype('int64')
df_games


games_per_year = df_games['year_of_release'].value_counts().sort_index()

print(games_per_year)


#Visualizando os dados em grafico.


plt.figure(figsize=(12, 6))
games_per_year.plot(kind='bar', color='skyblue')
plt.title('Número de Jogos Lançados por Ano')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Quantidade de Jogos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


