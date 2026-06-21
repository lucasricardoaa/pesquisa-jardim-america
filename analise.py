import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from collections import Counter
import warnings
warnings.filterwarnings("ignore")

# ── Configurações gerais de estilo ───────────────────────────────────────────
plt.rcParams.update({
    "font.family": "Arial",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

AZUL_ESCURO  = "#1F4E79"
AZUL_MEDIO   = "#2E75B6"
AZUL_CLARO   = "#BDD7EE"
LARANJA      = "#C55A11"
CINZA        = "#595959"

# ── Carregar dados ────────────────────────────────────────────────────────────
# OBS: o arquivo CSV exportado do Google Forms não está incluído neste repositório
# por conter respostas individuais dos moradores. Para reproduzir a análise,
# baixe o CSV de respostas do seu próprio Google Forms e coloque-o na mesma
# pasta deste script, ajustando o nome do arquivo abaixo se necessário.
df = pd.read_csv("respostas.csv")

# Renomear colunas para facilitar
df.columns = [
    "timestamp", "nome", "tempo_moradia", "faixa_etaria",
    "iluminacao", "limpeza", "ruas_calcadas", "transporte",
    "seguranca", "saude", "educacao", "comercio",
    "maior_problema", "sugestao"
]

colunas_escala = ["iluminacao", "limpeza", "ruas_calcadas", "transporte",
                  "seguranca", "saude", "educacao", "comercio"]

labels_escala = [
    "Iluminação pública", "Limpeza e coleta\nde lixo",
    "Ruas e calçadas", "Transporte público",
    "Segurança", "Acesso à saúde",
    "Acesso à educação", "Comércio e\nserviços básicos"
]

total = len(df)

# ─────────────────────────────────────────────────────────────────────────────
# FIGURA 1 — Médias por aspecto (barras horizontais)
# ─────────────────────────────────────────────────────────────────────────────
medias = df[colunas_escala].mean().values
ordem  = np.argsort(medias)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(
    [labels_escala[i] for i in ordem],
    [medias[i] for i in ordem],
    color=[LARANJA if medias[i] < 2 else AZUL_MEDIO if medias[i] < 3.5 else AZUL_ESCURO for i in ordem],
    height=0.6, edgecolor="white"
)

ax.set_xlim(0, 5.5)
ax.set_xlabel("Média (escala 1–5)", color=CINZA, fontsize=10)
ax.set_title(f"Avaliação média por aspecto do bairro\n({total} respondentes)", fontsize=13, fontweight="bold", color=AZUL_ESCURO)
ax.axvline(x=3, color="gray", linestyle="--", linewidth=0.8, alpha=0.5)

for bar, val in zip(bars, [medias[i] for i in ordem]):
    ax.text(val + 0.08, bar.get_y() + bar.get_height() / 2,
            f"{val:.2f}", va="center", fontsize=10, color=CINZA)

patches = [
    mpatches.Patch(color=LARANJA,    label="Crítico (< 2,0)"),
    mpatches.Patch(color=AZUL_MEDIO, label="Regular (2,0 – 3,4)"),
    mpatches.Patch(color=AZUL_ESCURO,label="Bom (≥ 3,5)"),
]
ax.legend(handles=patches, loc="lower right", fontsize=9)
ax.tick_params(colors=CINZA)
plt.tight_layout()
plt.savefig("outputs/fig1_medias_aspectos.png", dpi=150, bbox_inches="tight")
plt.close()
print("Fig 1 salva.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURA 2 — Distribuição por faixa etária
# ─────────────────────────────────────────────────────────────────────────────
ordem_faixa = ["Menos de 18 anos", "18 a 29 anos", "30 a 44 anos", "45 a 59 anos", "60 anos ou mais"]
contagem_faixa = df["faixa_etaria"].value_counts().reindex(ordem_faixa, fill_value=0)

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(contagem_faixa.index, contagem_faixa.values,
              color=AZUL_MEDIO, edgecolor="white", width=0.55)
ax.set_title(f"Distribuição por faixa etária\n({total} respondentes)", fontsize=13, fontweight="bold", color=AZUL_ESCURO)
ax.set_ylabel("Número de respondentes", color=CINZA, fontsize=10)
ax.set_ylim(0, contagem_faixa.max() + 2)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
            str(int(bar.get_height())), ha="center", va="bottom", fontsize=11, color=CINZA)

ax.tick_params(colors=CINZA)
plt.tight_layout()
plt.savefig("outputs/fig2_faixa_etaria.png", dpi=150, bbox_inches="tight")
plt.close()
print("Fig 2 salva.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURA 3 — Tempo de moradia (pizza)
# ─────────────────────────────────────────────────────────────────────────────
ordem_moradia = ["Menos de 1 ano", "De 1 a 5 anos", "De 5 a 10 anos", "Mais de 10 anos"]
contagem_moradia = df["tempo_moradia"].value_counts().reindex(ordem_moradia, fill_value=0)

cores_pizza = [AZUL_CLARO, AZUL_MEDIO, AZUL_ESCURO, LARANJA]
fig, ax = plt.subplots(figsize=(7, 6))
wedges, texts, autotexts = ax.pie(
    contagem_moradia.values,
    labels=contagem_moradia.index,
    autopct="%1.0f%%",
    colors=cores_pizza,
    startangle=140,
    wedgeprops={"edgecolor": "white", "linewidth": 1.5}
)
for t in autotexts:
    t.set_fontsize(11)
    t.set_color("white")
    t.set_fontweight("bold")

ax.set_title(f"Tempo de moradia no bairro\n({total} respondentes)", fontsize=13, fontweight="bold", color=AZUL_ESCURO)
plt.tight_layout()
plt.savefig("outputs/fig3_tempo_moradia.png", dpi=150, bbox_inches="tight")
plt.close()
print("Fig 3 salva.")

# ─────────────────────────────────────────────────────────────────────────────
# FIGURA 4 — Distribuição das notas de segurança (pior aspecto)
# ─────────────────────────────────────────────────────────────────────────────
contagem_seg = df["seguranca"].value_counts().sort_index()

fig, ax = plt.subplots(figsize=(7, 5))
bars = ax.bar(contagem_seg.index, contagem_seg.values,
              color=LARANJA, edgecolor="white", width=0.55)
ax.set_title(f"Distribuição das notas — Segurança\n(aspecto mais crítico | média: {df['seguranca'].mean():.2f})",
             fontsize=13, fontweight="bold", color=AZUL_ESCURO)
ax.set_xlabel("Nota (1 = Péssimo, 5 = Ótimo)", color=CINZA, fontsize=10)
ax.set_ylabel("Número de respondentes", color=CINZA, fontsize=10)
ax.set_xticks([1, 2, 3, 4, 5])
ax.set_ylim(0, contagem_seg.max() + 2)

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
            str(int(bar.get_height())), ha="center", va="bottom", fontsize=11, color=CINZA)

ax.tick_params(colors=CINZA)
plt.tight_layout()
plt.savefig("outputs/fig4_distribuicao_seguranca.png", dpi=150, bbox_inches="tight")
plt.close()
print("Fig 4 salva.")

# ─────────────────────────────────────────────────────────────────────────────
# RESUMO TEXTUAL NO TERMINAL
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "="*60)
print("  RESUMO DA ANÁLISE — JARDIM AMÉRICA")
print("="*60)
print(f"\nTotal de respondentes: {total}")
print(f"Identificados (com nome): {df['nome'].notna().sum()}")
print(f"Anônimos: {df['nome'].isna().sum()}")

print("\n── Médias por aspecto (1–5) ──")
for col, label in zip(colunas_escala, labels_escala):
    media = df[col].mean()
    barra = "█" * int(media * 4)
    print(f"  {label.replace(chr(10),' '):<30} {media:.2f}  {barra}")

print(f"\n── Aspecto mais bem avaliado ──")
idx_max = np.argmax(medias)
print(f"  {labels_escala[idx_max].replace(chr(10),' ')}: {medias[idx_max]:.2f}")

print(f"\n── Aspecto mais crítico ──")
idx_min = np.argmin(medias)
print(f"  {labels_escala[idx_min].replace(chr(10),' ')}: {medias[idx_min]:.2f}")

print("\n── Principais problemas mencionados ──")
problemas = df["maior_problema"].dropna().str.lower().tolist()
palavras_chave = ["segurança", "calçada", "saúde", "limpeza", "transporte", "educação", "emprego"]
for kw in palavras_chave:
    count = sum(kw in p for p in problemas)
    if count > 0:
        print(f"  '{kw}' mencionado em {count} resposta(s)")

print("\n── Gráficos salvos em outputs/ ──")
print("  fig1_medias_aspectos.png")
print("  fig2_faixa_etaria.png")
print("  fig3_tempo_moradia.png")
print("  fig4_distribuicao_seguranca.png")
print("="*60)
