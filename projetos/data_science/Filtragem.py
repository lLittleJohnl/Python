##########################################################################################################################
# Autor: João Vítor Correia Pessoa                                                                                       #
# Data:22/07/2022                                                                                                        #
# Objetivo: Filtragem e enriquecimento de dados dentro do Inventário.                                                    #
##########################################################################################################################

import pandas as pd

df = pd.read_csv('dados.csv', delimiter=',', encoding='utf-8')

Filtro_BTS = df[(df['CI_NAME'].str.contains("^(?![X])[A-Z]{4,7}\d{2,4}$", na=False)) & (df['EQUIPTYPE'] =='BTS')]
Filtro_BTS.to_csv("doc_filter.csv")
# print(df[(df['CI_NAME'].str.contains("^(?![X])[A-Z]{4,5}\d{2}$", na=False)) & (df['EQUIPTYPE'] =='BTS')])



