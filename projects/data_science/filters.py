##########################################################################################################################
# Autor: João Vítor Correia Pessoa                                                                                       #
# Data:22/07/2022 (Criação)                                                                                                       #
# Objetivo: Filtragem de dados para detecção de equipamentos cadastrados de forma incorreta                              #
##########################################################################################################################

# Bibliotecas:
import pandas as pd

# Abrindo os arquivos
df = pd.read_csv(r'C:\Users\joaov\Documentos\VSCODE\Python\projects\data_science\dados\base_elementos.CSV', delimiter=',', encoding='utf-8')

# Filtros:
F_AAA = df[(df['CI_NAME'].str.contains("^AAA", regex=True)) & (df['EQUIPTYPE'] =='AAA')]
F_ACCP = df[(df['CI_NAME'].str.contains("^[A-Z]{2,5}|^ap", regex=True)) & (df['EQUIPTYPE'] =='Access Point')]
F_ACW = df[(df['CI_NAME'].str.contains("^ACW|^ASW", regex=True)) & (df['EQUIPTYPE'] =='ACW')]
F_AGR = df[(df['CI_NAME'].str.contains("^AGR", regex=True)) & (df['EQUIPTYPE'] =='ACW')]
F_AP = df[(df['CI_NAME'].str.contains("^[A-Z]{2}-[A-Z]{3}-[A-Z]{3}", regex=True)) & (df['EQUIPTYPE'] =='AP')]
F_APPLICATION = df[(df['CI_NAME'].str.contains("^sne", regex=True)) & (df['EQUIPTYPE'] =='APPLICATION')]
F_APR = df[(df['CI_NAME'].str.contains("^APR", regex=True)) & (df['EQUIPTYPE'] =='APR')]
F_ATS = df[(df['CI_NAME'].str.contains("^[A-Z]{4}\d{2}|^[A-Z]{5}\d{1}|^IN-ATS", regex=True)) & (df['EQUIPTYPE'] =='ATS')]
F_BDPR = df[(df['CI_NAME'].str.contains("^[A-Z]{4}\d{2}|^[A-Z]{5}\d{1}", regex=True)) & (df['EQUIPTYPE'] =='BDPR')]
F_BRAS = df[(df['CI_NAME'].str.contains("^RTBA", regex=True)) & (df['EQUIPTYPE'] =='BRAS')]
F_BSC = df[(df['CI_NAME'].str.contains("^[A-Z]{4}\d{2}", regex=True)) & (df['EQUIPTYPE'] =='BSC')]
F_BSF = df[(df['CI_NAME'].str.contains("^IA", regex=True)) & (df['EQUIPTYPE'] =='BSF')]
F_BSP = df[(df['CI_NAME'].str.contains("^HB", regex=True)) & (df['EQUIPTYPE'] =='BSP')] 
F_BTS = df[(df['CI_NAME'].str.contains("^(?![X])[A-Z]{4,7}\d{2,3}$", regex=True)) & (df['EQUIPTYPE'] =='BTS')]
F_CCDM = df[(df['CI_NAME'].str.contains("^CCDM", regex=True)) & (df['EQUIPTYPE'] =='CCDM')]
F_CCF = df[(df['CI_NAME'].str.contains("^IC", regex=True)) & (df['EQUIPTYPE'] =='CCF')]
F_CCPC = df[(df['CI_NAME'].str.contains("^CCPC", regex=True)) & (df['EQUIPTYPE'] =='CCPC')]
F_CCSM = df[(df['CI_NAME'].str.contains("^CCSM", regex=True)) & (df['EQUIPTYPE'] =='CCSM')]
F_GC = df[(df['CI_NAME'].str.contains("^GC", regex=True)) & (df['EQUIPTYPE'] =='Charging Gateway')]


F_NODEB = df[(df['CI_NAME'].str.contains("^[A-Z]{2}\d{4}$", na=False)) & (df['EQUIPTYPE'] =='NODEB')]
F_4G = df[(df['CI_NAME'].str.contains("^[A-Z]{2}\d{4}$", na=False)) & (df['EQUIPTYPE'] =='LTE')]
F_5G = df[(df['CI_NAME'].str.contains("^[A-Z]{2}\d{4}$", na=False)) & (df['EQUIPTYPE'] =='GNODEB')]
F_MWE = df[(df['CI_NAME'].str.contains("^[A-Z]{2}\d{4}$", na=False)) & (df['EQUIPTYPE'] =='MWE')]

# F_AMR = sem padrão
# F_ANTI_SPAM_SMSC = sem padrão
# F_BLADE = sem padrão

# nome_da_variavel.to_csv("nome_do_arquivo.csv")
