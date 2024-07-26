import pandas as pd 
import matplotlib.pyplot as plt
from tqdm import tqdm
import matplotlib
df = pd.read_csv(r'17_06_2023_18_48RESULTADOS.csv')

passagem = []

df = df.loc[(df['x']>49.493) & (df['x']<(49.493+24))]

RPM = list(df['rpm'])
t = [i-49.43 for i in list(df['x'])]


plt.plot(t,RPM)
plt.xlabel('t(s)')
plt.ylabel('RPM')
plt.show()
