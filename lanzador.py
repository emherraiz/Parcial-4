import pandas as pd


n = 100
media = 200
desviacion = 30

df = pd.read_csv('EXAMENES/Parcial-4/tabla.csv')

print(df['valor'].sum())
