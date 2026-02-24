from mabepy.core import GrauEvidencia
from mabepy.visual import plotar_quadrado_unitario

# Simulando as saídas de 3 redes neurais analisando a mesma imagem
modelo_A = GrauEvidencia(0.80, 0.20)  # Acha que é Verdade
modelo_B = GrauEvidencia(0.70, 0.40)  # Acha que é Verdade, mas com dúvida
modelo_C = GrauEvidencia(0.10, 0.90)  # Esse aqui surtou e acha que é Falso

# Juntando todo mundo numa lista
lista_modelos = [modelo_A, modelo_B, modelo_C]

# MABE CALCULANDO O CONSENSO!
consenso = GrauEvidencia.calcular_baricentro(lista_modelos)

print(f"Consenso Final calculado: {consenso}")
print(f"Estado Lógico do Consenso: {consenso.determinar_estado().value}")

# Preparando os dados para ver no gráfico
dados_grafico = {
    "Modelo A": modelo_A,
    "Modelo B": modelo_B,
    "Modelo C": modelo_C,
    "CONSENSO FINAL": consenso
}

# Plotando
plotar_quadrado_unitario(dados_grafico, titulo="MABE - Análise de Consenso (Visão Computacional)")