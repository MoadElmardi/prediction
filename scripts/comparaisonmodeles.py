# Réexécution du code après réinitialisation de l'environnement

import pandas as pd
import matplotlib.pyplot as plt

# Exemple fictif de performances (à remplacer par les valeurs réelles si disponibles)
performance_data = {
    "Modèle": ["Random Forest (global)", "Gradient Boosting (élémentaire)"],
    "MAE": [1.4916, 13.612],
    "RMSE": [13.681, 23.575]
}

df_perf = pd.DataFrame(performance_data)

# Création du graphe comparatif
fig, ax = plt.subplots(figsize=(8, 5))

bar_width = 0.35
x = range(len(df_perf))

ax.bar(x, df_perf["MAE"], width=bar_width, label="MAE")
ax.bar([i + bar_width for i in x], df_perf["RMSE"], width=bar_width, label="RMSE")

ax.set_xlabel("Modèles")
ax.set_ylabel("Erreur (en secondes)")
ax.set_title("Comparaison des performances des modèles")
ax.set_xticks([i + bar_width / 2 for i in x])
ax.set_xticklabels(df_perf["Modèle"], rotation=15)
ax.legend()
ax.set_axisbelow(True)
plt.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()
