%%writefile gasolina.csv
dia,venda
1,5.11
2,4.99
3,5.02
4,5.21
5,5.07
6,5.09
7,5.13
8,5.12
9,4.94
10,5.03

import pandas as pd
import seaborn as sns

dados = pd.read_csv("gasolina.csv",sep=",")

with sns.axes_style('whitegrid'):
  grafico = sns.lineplot(data=dados, x="dia",y="venda",palette="colorblind")
  grafico.set(title='Price per day',xlabel='Day',ylabel='Price');