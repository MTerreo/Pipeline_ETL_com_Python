# -*- coding: utf-8 -*-
"""API_py.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13vil26NmB9T30Ez6XjQ3jRMh3USLj1WW
"""

import numpy as np
import pandas as pd
np.random.seed(12345)
import matplotlib.pyplot as plt

"""Neste exemplo vou utilizar uma API publica que vai gerar um retorno no formato JSON com os "issues" e/ou propostas de melhoria do python:

Primeiro passo é preparar o acesso, para isso vou usar o pacote "requests"
"""

import requests

url = "https://api.github.com/repos/pandas-dev/pandas/issues"

resp = requests.get(url)

resp.raise_for_status()

resp

"""É uma boa prática sempre chamar raise_for_status depois de usar requests.get para verificar se há erros de HTTP.

O método json do objeto de resposta retornará um objeto Python contendo os dados JSON analisados como um dicionário ou lista (dependendo de qual JSON é retornado):
"""

data = resp.json()

"""Vamos ver o primeiro elemento do JSON, que neste caso será um dicionário com muitas informações:"""

data[0]

"""Importante nota que os resultados recuperados são baseados em dados em tempo real, os dados que você vai obter ao executar esse código serão diferentes dos mostrados nest exemplo!!!

Podemos passar o JSON para um dataframe de forma a facilitar a leitura dos dados:
"""

df = pd.DataFrame(data)

"""Explorando os dados obtidos:"""

df.head(6)

df.tail(3)

df.shape

df.columns

"""Vamos supor que para a análise vamos precisar somente de algumas colunas, podemos criar um daframe somente com elas:"""

issues = pd.DataFrame(data, columns=["id", "number", "title", "labels", "state", 'created_at'])

issues.head()

"""E para exportar este dataframe para um arquivo .csv :"""

issues.to_csv("/content/issues.csv", encoding = 'utf-8')