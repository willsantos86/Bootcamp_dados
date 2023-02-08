import requests
import pandas as pd
import collections
import sys

url = 'https://servicebus2.caixa.gov.br/portaldeloterias/api/resultados?modalidade=Lotof%C3%A1cil'

r = requests.get(url, verify=False)


r.text
r_text = r.text

df = pd.read_html(r_text)

type(df)
df
type(df[0])
df =df[0].copy()
df

df=df[0].copy()

nr_pop = list(range(1, 26))
nr_pares = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]
nr_impares = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25]
nr_primos = [2, 3, 5, 7, , 11, 13, 17, 19, 23]
