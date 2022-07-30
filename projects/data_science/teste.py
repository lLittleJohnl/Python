##########################################################################################################################
# Autor: João Vítor Correia Pessoa                                                                                       #
# Data:22/07/2022                                                                                                        #
# Objetivo: Filtragem de dados para detecção de equipamentos cadastrados que estão fora do padrão                              #
##########################################################################################################################

import pandas as pd

df = pd.read_csv(r'C:\Users\joaov\Documentos\VSCODE\Python\projects\data_science\dados\base_elementos.CSV', delimiter=',', encoding='utf-8')

F_AAA = df[(df['CI_NAME'].str.contains("^AAA", regex=True)) & (df['EQUIPTYPE'] =='AAA')]
print(F_AAA)
#F_Acess_Point.to_excel("teste.xlsx")