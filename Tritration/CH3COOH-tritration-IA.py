import numpy as np
def calcular_media(volumes):
      return np.mean(volumes)

def calcular_desvio_padrao(volumes):
      return np.std(volumes, ddof=1)

def calcular_desvio_relativo(desvio_padrao, media):
      return (desvio_padrao / media) * 100

def calcular_conc_CH3COOH_diluido(media, conc_NaOH, volume_total):
      return (media * conc_NaOH) / volume_total

def calcular_conc_CH3COOH_puro(conc_CH3COOH_diluido, volume_total, volume_aliquota):
      return (conc_CH3COOH_diluido * volume_total) / volume_aliquota

def calcular_conc_mass(conc_CH3COOH_puro, mm_CH3COOH):
      return conc_CH3COOH_puro * mm_CH3COOH

def calcular_titulo(conc_mass, densidade_CH3COOH):
      return (conc_mass / (densidade_CH3COOH * 1000)) * 100

# Dados
volumes = np.array([13.1, 13.4, 13.2, 13.1, 13.0, 13.2])  # Em mL
conc_NaOH = 0.113  # mol/L
mm_CH3COOH = 60.052  # g/mol
volume_total = 27  # Em mL
volume_aliquota = 2  # Em mL
densidade_CH3COOH = 1.05  # Em g/cm^3

# Cálculos
media = calcular_media(volumes)
desvio_padrao = calcular_desvio_padrao(volumes)
desvio_relativo = calcular_desvio_relativo(desvio_padrao, media)
conc_CH3COOH_diluido = calcular_conc_CH3COOH_diluido(media, conc_NaOH, volume_total)
conc_CH3COOH_puro = calcular_conc_CH3COOH_puro(conc_CH3COOH_diluido, volume_total, volume_aliquota)
conc_mass = calcular_conc_mass(conc_CH3COOH_puro, mm_CH3COOH)
titulo = calcular_titulo(conc_mass, densidade_CH3COOH)

print(f"Média de volumes: {np.round(media, decimals=1)} mL \n"
        f"Desvio padrão dos volumes: {np.round(desvio_padrao, decimals=2)} \n"
        f"Desvio relativo dos volumes: {np.round(desvio_relativo, decimals=2)}% \n"
        f"Concentração de CH3COOH: {np.round(conc_CH3COOH_puro, decimals=2)} mol/L \n"
        f"Título: {np.round(titulo, decimals=2)}%")
# Dados
