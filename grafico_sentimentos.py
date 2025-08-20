import json
import os
import matplotlib.pyplot as plt

# Diretório onde estão os arquivos json de sentimento
sentimento_dir = os.path.join(os.path.dirname(__file__), 'json', 'Sentimento')

arquivos = [
    ("Frase 1", "resultadoFrase1.json"),
    ("Frase 2", "resultadoFrase2.json"),
    ("Frase 3", "resultadoFrase3.json"),
]

labels = []
positivos = []
neutros = []
negativos = []

for nome, arquivo in arquivos:
    caminho = os.path.join(sentimento_dir, arquivo)
    with open(caminho, encoding="utf-8") as f:
        dados = json.load(f)
        doc = dados["data"]["results"]["documents"][0]
        scores = doc["confidenceScores"]
        labels.append(nome)
        positivos.append(scores["positive"])
        neutros.append(scores["neutral"])
        negativos.append(scores["negative"])

x = range(len(labels))
plt.figure(figsize=(8,5))
bar1 = plt.bar(x, positivos, width=0.2, label="Positivo", align="center")
bar2 = plt.bar([i+0.2 for i in x], neutros, width=0.2, label="Neutro", align="center")
bar3 = plt.bar([i+0.4 for i in x], negativos, width=0.2, label="Negativo", align="center")
plt.xticks([i+0.2 for i in x], labels)
plt.ylabel("Confiança")
plt.title("Comparativo de Sentimentos das Frases")
plt.legend()

# Exibir valores percentuais em cada barra
for bars, valores in zip([bar1, bar2, bar3], [positivos, neutros, negativos]):
    for bar, valor in zip(bars, valores):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height(), f'{valor*100:.1f}%',
                 ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()
