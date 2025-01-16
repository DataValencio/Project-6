import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


df_games = pd.read_csv('games.csv')
print(df_games.head(10))


#Alterando os tipo de dados das colunas e substituindo valores ausentes.


df_games['user_score'] = df_games['user_score'].replace('tbd', '0')
df_games['user_score'] = df_games['user_score'].astype(float)
df_games['year_of_release'] = df_games['year_of_release'].astype('Int64').astype(str)
df_games['year_of_release'] = df_games['year_of_release'].fillna('desconhecido')
df_games['year_of_release'] = pd.to_numeric(df_games['year_of_release'], errors='coerce')
df_games = df_games.dropna(subset=['year_of_release'])
df_games

df_games.isna().sum()


#Substituindo os valores ausentes das colunas categoricas.

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


