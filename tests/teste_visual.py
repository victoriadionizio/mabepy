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
