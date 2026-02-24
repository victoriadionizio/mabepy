import pandas as pd
from .core import GrauEvidencia, Estado, TomadaDecisao

def processar_dataframe(df: pd.DataFrame, col_mu: str, col_lambda: str, analisador: TomadaDecisao = None) -> pd.DataFrame:
    """
    Lê um DataFrame do Pandas e processa a lógica paraconsistente em lote.
    Adiciona colunas com o Grau de Certeza, Contradição e o Estado Lógico final.
    """
    df_result = df.copy()
    
    def classificar(mu, lam):
        ev = GrauEvidencia(mu, lam)
        if analisador:
            return analisador.analisar(ev).value
        return ev.determinar_estado().value

    # Aplicando as fórmulas da LPA2v de forma vetorizada no DataFrame
    df_result['Gcc'] = df_result[col_mu] - df_result[col_lambda]
    df_result['Gct'] = df_result[col_mu] + df_result[col_lambda] - 1.0
    
    # Aplicando a classificação lógica
    df_result['Estado_LPA2v'] = df_result.apply(lambda row: classificar(row[col_mu], row[col_lambda]), axis=1)
    
    return df_result
