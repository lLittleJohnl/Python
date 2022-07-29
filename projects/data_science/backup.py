# Filtro: Technology = NODE-B
# print(df[df['CI_NAME'].str.contains("^[A-Z]{2}\d{4}$", na=False)])
# Filtro: Technology = ENODE-B
# print(df[df['CI_NAME'].str.contains("^(?![X])[A-Z]{4}\d{2}.$", na=False)])
# Filtro: Technology = GNODE-B
# print(df[df['CI_NAME'].str.contains("^5G$", na=False)])

# Enriquecimento: BTS
# df.loc[df.["ictEntityEquipType"]=='BTS', 'Technology'] = 'GSM'
# df.loc[df.["ictEntityEquipType"]=='BTS', 'ictEntityTier1'] = 'iSOC A&I'
# df.loc[df.["ictEntityEquipType"]=='BTS', 'ictEntityTier2'] = 'BSS'
# df.loc[df.["ictEntityEquipType"]=='BTS', 'ictEntityTier3'] = 'Acesso'
# # Enriquecimento: NODE-B
# df.loc[df.["ictEntityEquipType"]=='NODE-B', 'Technology'] = 'UMTS'
# df.loc[df.["ictEntityEquipType"]=='NODE-B', 'ictEntityTier1'] = 'iSOC A&I'
# df.loc[df.["ictEntityEquipType"]=='NODE-B', 'ictEntityTier2'] = 'BSS'
# df.loc[df.["ictEntityEquipType"]=='NODE-B', 'ictEntityTier3'] = 'Acesso'
# # Enriquecimento: ENODE-B
# df.loc[df.["ictEntityEquipType"]=='ENODE-B', 'Technology'] = 'LTE'
# df.loc[df.["ictEntityEquipType"]=='ENODE-B', 'ictEntityTier1'] = 'iSOC A&I'
# df.loc[df.["ictEntityEquipType"]=='ENODE-B', 'ictEntityTier2'] = 'BSS'
# df.loc[df.["ictEntityEquipType"]=='ENODE-B', 'ictEntityTier3'] = 'Acesso'
# # Enriquecimento: GNODE-B
# df.loc[df.["ictEntityEquipType"]=='GNODE-B', 'Technology'] = '5G'
# df.loc[df.["ictEntityEquipType"]=='GNODE-B', 'ictEntityTier1'] = 'iSOC A&I'
# df.loc[df.["ictEntityEquipType"]=='GNODE-B', 'ictEntityTier2'] = 'BSS'
# df.loc[df.["ictEntityEquipType"]=='GNODE-B', 'ictEntityTier3'] = 'Acesso'
# Enriquecimento: MWE