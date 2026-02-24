import matplotlib.pyplot as plt
import numpy as np
from .core import GrauEvidencia

def _configurar_estilo(ax, titulo):
    ax.set_title(titulo, fontsize=18, fontweight='bold', pad=20)
    ax.grid(True, linestyle='--', color='gray', alpha=0.6)
    ax.set_facecolor('#eafff5')

def plotar_quadrado_unitario(pontos: dict = None, titulo: str = 'MABE - Quadrado Unitário (LPA2v)'):
    """Plota o quadrado unitário resgatando o design limpo original."""
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_aspect('equal', adjustable='box')
    _configurar_estilo(ax, titulo)
    
    # Design de linhas e fronteiras
    ax.axhline(y=0.5, color='blue', linestyle='-', lw=2, label='Linhas limites')
    ax.axvline(x=0.5, color='blue', linestyle='-', lw=2)
    ax.plot([0, 1], [0, 1], color='blue', linestyle='-', lw=2)
    ax.plot([1, 0], [0, 1], color='blue', linestyle='-', lw=2)
    
    vertices_fronteira = np.array([[0.5, 1], [1, 0.5], [0.5, 0], [0, 0.5], [0.5, 1]])
    ax.plot(vertices_fronteira[:, 0], vertices_fronteira[:, 1], color='red', lw=2, label='Fronteiras')

    ax.set_xlabel('Grau de Evidência Favorável (μ)', fontsize=14)
    ax.set_ylabel('Grau de Evidência Contrário (λ)', fontsize=14)
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.05, 1.05)

    if pontos:
        _plotar_pontos(ax, pontos, modo='quadrado')

    # Legenda para não poluir o gráfico
    ax.legend(loc='upper right', fontsize=11, title="Anotações", title_fontsize='12')
    plt.tight_layout()
    plt.show()

def plotar_reticulado_hasse(pontos: dict = None, titulo: str = 'MABE - Reticulado de Hasse'):
    """Plota o Reticulado (Losango). Eixo X=Contradição, Eixo Y=Certeza."""
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title(titulo, fontsize=18, fontweight='bold', pad=20)
    ax.grid(True, linestyle='--', color='gray', alpha=0.3)
    ax.set_facecolor('#f8f9fa')

    # Desenhar o Losango Principal
    losango = np.array([[0, 1], [1, 0], [0, -1], [-1, 0], [0, 1]])
    ax.plot(losango[:,0], losango[:,1], 'k-', lw=2)
    ax.axhline(0, color='gray', lw=1); ax.axvline(0, color='gray', lw=1)
    
    # Rótulos dos vértices extremos (mais limpos)
    ax.text(0, 1.08, 'Verdadeiro (V)', ha='center', fontsize=12, color='green', fontweight='bold')
    ax.text(0, -1.13, 'Falso (F)', ha='center', fontsize=12, color='red', fontweight='bold')
    ax.text(1.13, 0, 'Inconsistente (T)', va='center', fontsize=12, color='purple', fontweight='bold')
    ax.text(-1.13, 0, 'Paracompleto (⊥)', va='center', ha='right', fontsize=12, color='orange', fontweight='bold')

    ax.set_xlabel('Grau de Contradição (Gct)', fontsize=14)
    ax.set_ylabel('Grau de Certeza (Gcc)', fontsize=14)
    ax.set_xlim(-1.4, 1.4); ax.set_ylim(-1.4, 1.4)

    if pontos:
        _plotar_pontos(ax, pontos, modo='reticulado')

    ax.legend(loc='upper right', fontsize=11, title="Anotações")
    plt.tight_layout()
    plt.show()

def _plotar_pontos(ax, pontos, modo):
    cores = ['#2ca02c', '#d62728', '#9467bd', '#ff7f0e', '#1f77b4', '#8c564b']
    marcadores = ['o', 's', '^', 'D', 'P', 'X']
    
    for i, (nome, grau) in enumerate(pontos.items()):
        cor = cores[i % len(cores)]
        marc = marcadores[i % len(marcadores)]
        
        if modo == 'quadrado':
            x, y = grau.mu, grau.lambda_
        else: # modo reticulado
            x, y = grau.grau_contradicao, grau.grau_certeza
            
        ax.scatter(x, y, s=300, c=cor, marker=marc, edgecolors='black', lw=1.5, zorder=10, label=f"{nome}")
