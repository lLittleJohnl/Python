##########################################################################################################################
# Autor: João Vítor Correia Pessoa                                                                                       #
# Data:22/07/2022                                                                                                        #
# Objetivo: Filtragem de dados para detecção de equipamentos cadastrados de forma incorreta                              #
##########################################################################################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\joaov\Documentos\VSCODE\Python\projects\data_science\dados\base_elementos.CSV', delimiter=',', encoding='utf-8')

Filtro_BTS = df[(df['CI_NAME'].str.contains("^(?![X])[A-Z]{4,7}\d{2,4}$", na=False)) & (df['EQUIPTYPE'] =='BTS')]
print(Filtro_BTS)
#Filtro_BTS.to_csv("doc_filter.csv")
# print(df[(df['CI_NAME'].str.contains("^(?![X])[A-Z]{4,5}\d{2}$", na=False)) & (df['EQUIPTYPE'] =='BTS')])



