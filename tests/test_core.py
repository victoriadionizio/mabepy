from mabepy.core import GrauEvidencia
from mabepy.visual import plotar_quadrado_unitario, plotar_reticulado_hasse

print("INICIANDO MABE - SISTEMA DE LÓGICA PARACONSISTENTE")

# 1. Criando evidências base
evidencia_A = GrauEvidencia(0.8, 0.1) # Forte tendência à Verdade
evidencia_B = GrauEvidencia(0.2, 0.9) # Forte tendência à Falsidade

# 2. Testando a MATEMÁTICA (Operadores Mágicos)
evidencia_OU = evidencia_A | evidencia_B  # Maximização
evidencia_E  = evidencia_A & evidencia_B  # Minimização
evidencia_NAO = ~evidencia_A              # Negação

print(f"\nMatemática da MABE:")
print(f"A: {evidencia_A} -> {evidencia_A.determinar_estado().value}")
print(f"B: {evidencia_B} -> {evidencia_B.determinar_estado().value}")
print(f"A ou B: {evidencia_OU} (Esperado crença alta)")
print(f"A e B : {evidencia_E} (Esperado crença baixa)")
print(f"Não A : {evidencia_NAO} (Inverteu A)")

# 3. Preparando os dados para os gráficos
dados_para_plotar = {
    "Ponto A": evidencia_A,
    "Ponto B": evidencia_B,
    "A ou B": evidencia_OU,
    "A e B": evidencia_E,
    "Não A": evidencia_NAO,
    "Inconsistente Puro": GrauEvidencia(1.0, 1.0)
}

# 4. Gerando os Visuais
print("\nGerando Gráfico 1: Quadrado Unitário...")
plotar_quadrado_unitario(dados_para_plotar, titulo="MABE - Análise de Operadores")

print("Gerando Gráfico 2: Reticulado de Hasse (Losango)...")
plotar_reticulado_hasse(dados_para_plotar, titulo="MABE - Visão no Reticulado")

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