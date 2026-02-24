import math
from enum import Enum

class Estado(Enum):
    VERDADEIRO = "Verdadeiro"
    FALSO = "Falso"
    INCONSISTENTE = "Inconsistente"
    PARACOMPLETO = "Paracompleto"
    NAO_DEFINIDO = "Não Definido (Fronteira)"

class GrauEvidencia:
    """
    Representa a anotação paraconsistente (MABE) com graus de crença (mu) e descrença (lambda).
    Suporta operações lógicas: OU (|), E (&), NÃO (~).
    """
    def __init__(self, mu: float, lambda_: float):
        # Garante que os valores fiquem entre 0 e 1 (clamping) para evitar erros de arredondamento
        self.mu = max(0.0, min(1.0, mu))
        self.lambda_ = max(0.0, min(1.0, lambda_))

    def __repr__(self):
        return f"GrauEvidencia(μ={self.mu:.2f}, λ={self.lambda_:.2f})"
    
    @property
    def grau_certeza(self) -> float:
        """Calcula o Grau de Certeza Normalizado (Gcc = mu - lambda). Intervalo [-1, 1]."""
        return self.mu - self.lambda_
    
    @property
    def grau_contradicao(self) -> float:
        """Calcula o Grau de Contradição Normalizado (Gct = mu + lambda - 1). Intervalo [-1, 1]."""
        return self.mu + self.lambda_ - 1.0

    def determinar_estado(self, valor_controle: float = 0.5) -> Estado:
        """Determina o estado lógico no reticulado padrão."""
        gcc = self.grau_certeza
        gct = self.grau_contradicao

        if gcc >= valor_controle: return Estado.VERDADEIRO
        if gcc <= -valor_controle: return Estado.FALSO
        if gct >= valor_controle: return Estado.INCONSISTENTE
        if gct <= -valor_controle: return Estado.PARACOMPLETO
        return Estado.NAO_DEFINIDO

    # --- OPERADORES LÓGICOS (A Mágica da MABE) ---

    def __or__(self, other):
        """Operador OU (Maximização): Pega a maior crença e a menor descrença."""
        if not isinstance(other, GrauEvidencia): return NotImplemented
        return GrauEvidencia(max(self.mu, other.mu), min(self.lambda_, other.lambda_))

    def __and__(self, other):
        """Operador E (Minimização): Pega a menor crença e a maior descrença."""
        if not isinstance(other, GrauEvidencia): return NotImplemented
        return GrauEvidencia(min(self.mu, other.mu), max(self.lambda_, other.lambda_))

    def __invert__(self):
        """Operador NÃO (Complemento): Inverte crença com descrença."""
        return GrauEvidencia(self.lambda_, self.mu)

    def distancia_ate(self, outra: 'GrauEvidencia') -> float:
        """Calcula a Distância Euclidiana entre duas anotações no reticulado."""
        if not isinstance(outra, GrauEvidencia):
            return NotImplemented
        delta_gcc = self.grau_certeza - outra.grau_certeza
        delta_gct = self.grau_contradicao - outra.grau_contradicao
        return math.sqrt(delta_gcc**2 + delta_gct**2)

    @staticmethod
    def calcular_baricentro(evidencias: list['GrauEvidencia']) -> 'GrauEvidencia':
        """
        Calcula o centro de gravidade (baricentro) de uma lista de anotações.
        Retorna uma nova evidência que representa o consenso do grupo.
        """
        if not evidencias:
            raise ValueError("A lista de evidências não pode estar vazia.")
        
        N = len(evidencias)
        media_mu = sum(e.mu for e in evidencias) / N
        media_lambda = sum(e.lambda_ for e in evidencias) / N
        
        return GrauEvidencia(media_mu, media_lambda)


class TomadaDecisao:
    """
    Motor de inferência com limiares (thresholds) customizáveis para sistemas críticos.
    Ideal para quando o valor de controle padrão de 0.5 não é suficiente.
    """
    def __init__(self, limiar_verdade: float = 0.5, limiar_falsidade: float = -0.5, 
                 limiar_inconsistencia: float = 0.5, limiar_paracompletude: float = -0.5):
        self.lv = limiar_verdade
        self.lf = limiar_falsidade
        self.li = limiar_inconsistencia
        self.lp = limiar_paracompletude

    def analisar(self, evidencia: GrauEvidencia) -> Estado:
        """Avalia uma evidência aplicando os limiares de exigência configurados."""
        gcc = evidencia.grau_certeza
        gct = evidencia.grau_contradicao

        if gcc >= self.lv: return Estado.VERDADEIRO
        if gcc <= self.lf: return Estado.FALSO
        if gct >= self.li: return Estado.INCONSISTENTE
        if gct <= self.lp: return Estado.PARACOMPLETO
        return Estado.NAO_DEFINIDO