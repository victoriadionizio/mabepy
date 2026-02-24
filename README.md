# MABE - Motor de Análise Baseado em Evidências

Uma biblioteca em Python dedicada à **Lógica Paraconsistente Anotada de Dois Valores (LPA2v)**. 

A MABE foi desenvolvida para facilitar a modelagem matemática e a tomada de decisão em sistemas que lidam com incerteza, dados conflituosos e paracompletude. É uma ferramenta ideal para agregar saídas de múltiplos modelos de Inteligência Artificial (como redes neurais e sistemas de visão computacional), extraindo o consenso matemático através do cálculo do baricentro.

---

## Como Instalar

Você pode instalar a MABE diretamente deste repositório do GitHub utilizando o `pip`. No seu terminal, rode o comando:

```bash
pip install git+[https://github.com/victoriadionizio/mabepy.git](https://github.com/victoriadionizio/mabepy.git)
```
## Módulo Principal (mabepy.core)
O coração da biblioteca, responsável pela álgebra paraconsistente.

GrauEvidencia(mu: float, lambda_: float): Cria a anotação paraconsistente.

.grau_certeza e .grau_contradicao: Propriedades que calculam os eixos do reticulado.

.determinar_estado(): Classifica a anotação no reticulado padrão (limiar 0.5).

.distancia_ate(outra_evidencia): Calcula a Distância Euclidiana entre duas anotações (mede a divergência matemática entre dois modelos).

## Operadores Lógicos: Suporta as operações de Maximização (|), Minimização (&) e Negação (~).

calcular_baricentro(evidencias: list): Calcula o Centro de Gravidade (Consenso) de uma lista de evidências.

Tomada de Decisão Avançada
TomadaDecisao(limiar_verdade, limiar_falsidade, ...): Permite criar instâncias com níveis de exigência personalizados (thresholds) para sistemas críticos que não podem depender do valor padrão de 0.5.

## Processamento em Lote (mabepy.analise)
Integração nativa com a biblioteca Pandas para processamento vetorial de grandes volumes de dados (ex: análise de milhares de frames de um vídeo).

processar_dataframe(df, col_mu, col_lambda, analisador): Recebe um DataFrame, os nomes das colunas de evidência e (opcionalmente) um motor de TomadaDecisao. Retorna o DataFrame enriquecido com os cálculos e o estado lógico final de cada linha.

## Módulo de Visualização (mabepy.visual)
Ferramentas gráficas integradas com matplotlib para gerar representações visuais acadêmicas.

plotar_quadrado_unitario(pontos, titulo): Plota o gráfico base (Crença vs Descrença).

plotar_reticulado_hasse(pontos, titulo): Plota o gráfico em formato de losango (Contradição vs Certeza).

Exemplo de Uso Prático (Visão Computacional)
Exemplo de como utilizar a MABE para processar saídas de uma rede neural analisando a alimentação de aves em lote com critérios rígidos:
```
Python
import pandas as pd
from mabepy.core import TomadaDecisao
from mabepy.analise import processar_dataframe

# 1. Simulando um dataset com frames analisados por IA
dados = {
    'frame_id': [1, 2, 3],
    'mu_ia': [0.90, 0.60, 0.10],
    'lambda_ia': [0.05, 0.40, 0.85]
}
df_frames = pd.DataFrame(dados)

# 2. Criando um decisor exigente (Certeza tem que ser > 0.75)
decisor_rigido = TomadaDecisao(limiar_verdade=0.75, limiar_falsidade=-0.75)

# 3. Processando o Dataset inteiro de uma vez
df_processado = processar_dataframe(
    df=df_frames, 
    col_mu='mu_ia', 
    col_lambda='lambda_ia', 
    analisador=decisor_rigido
)

print(df_processado)
```
