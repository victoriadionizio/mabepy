import pandas as pd
from mabepy.core import GrauEvidencia, TomadaDecisao
from mabepy.analise import processar_dataframe

print("MABE - MÓDULOS AVANÇADOS\n")

# 1. TESTE DE DISTÂNCIA (O quão divergentes são dois modelos de IA?)
modelo_resnet = GrauEvidencia(0.9, 0.1) # Acha que a ave está comendo
modelo_yolo = GrauEvidencia(0.2, 0.8)   # Acha que a ave NÃO está comendo

distancia = modelo_resnet.distancia_ate(modelo_yolo)
print(f"Divergência matemática entre ResNet e YOLO: {distancia:.2f}")
print("-" * 40)

# 2. TESTE DO PANDAS + LIMIARES RÍGIDOS
# Simulando um dataset com 5 frames do vídeo da câmera
dados = {
    'frame_id': [1, 2, 3, 4, 5],
    'mu_rede_neural': [0.90, 0.60, 0.40, 0.10, 0.80],
    'lambda_rede_neural': [0.05, 0.40, 0.60, 0.85, 0.80]
}
df_frames = pd.DataFrame(dados)

# Criando um decisor ultra-exigente (Só é Verdade se certeza for maior que 0.75!)
decisor_rigido = TomadaDecisao(limiar_verdade=0.75, limiar_falsidade=-0.75)

print("\nProcessando Dataset de Frames em Lote (com critério rígido)...")
df_processado = processar_dataframe(
    df=df_frames, 
    col_mu='mu_rede_neural', 
    col_lambda='lambda_rede_neural', 
    analisador=decisor_rigido
)

print(df_processado.to_string(index=False))
