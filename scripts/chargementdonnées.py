import pandas as pd

# Charger le dataset existant
file_path = "données/dataset_tfhe_execution_times.csv"
df = pd.read_csv(file_path)

# Ajouter les colonnes "type_donnee" et "echelle" avec valeurs par défaut pour les anciennes données (entiers, sans échelle)
df["type_donnee"] = "entier"
df["echelle"] = None

# Données pour les flottants
float_data = [
    # Format: (operation, scale, value (in ms or s), type, unit)
    ("Chiffrement", "1e3", 3.535171, "flottant", "ms"),
    ("Chiffrement", "1e6", 3.619915, "flottant", "ms"),
    ("Generation des cles", "1e3", 1.094957687, "flottant", "s"),
    ("Generation des cles", "1e6", 1.08326463, "flottant", "s"),
    ("Addition homomorphe", "1e3", 782.65927, "flottant", "ms"),
    ("Addition homomorphe", "1e6", 814.207712, "flottant", "ms"),
    ("Soustraction homomorphe", "1e3", 762.669487, "flottant", "ms"),
    ("Soustraction homomorphe", "1e6", 801.113175, "flottant", "ms"),
    ("Multiplication homomorphe", "1e3", 13.031773567, "flottant", "s"),
    ("Multiplication homomorphe", "1e6", 14.055032123, "flottant", "s"),
    ("Division homomorphe", "1e3", 74.999825657, "flottant", "s"),
    ("Division homomorphe", "1e6", 79.121153683, "flottant", "s"),
    ("ET binaire", "1e3", 226.110589, "flottant", "ms"),
    ("ET binaire", "1e6", 241.049094, "flottant", "ms"),
    ("OU binaire", "1e3", 228.170855, "flottant", "ms"),
    ("OU binaire", "1e6", 242.838415, "flottant", "ms"),
    ("XOR binaire", "1e3", 226.719395, "flottant", "ms"),
    ("XOR binaire", "1e6", 241.592229, "flottant", "ms"),
    ("Egalite", "1e3", 349.682782, "flottant", "ms"),
    ("Egalite", "1e6", 370.338026, "flottant", "ms"),
    ("Inegalite", "1e3", 349.317717, "flottant", "ms"),
    ("Inegalite", "1e6", 366.521332, "flottant", "ms"),
    ("Superieur", "1e3", 414.95611, "flottant", "ms"),
    ("Superieur", "1e6", 434.053627, "flottant", "ms"),
    ("Superieur ou egal", "1e3", 411.9551, "flottant", "ms"),
    ("Superieur ou egal", "1e6", 432.027594, "flottant", "ms"),
    ("Dechiffrement", "1e3", 71.316, "flottant", "us"),
    ("Dechiffrement", "1e6", 71.877, "flottant", "us"),
    # Programmes FheInt64
    ("Programme Soustraction", "1e3", 1843317755, "flottant", "ns"),
    ("Programme Soustraction", "1e6", 1827881076, "flottant", "ns"),
    ("Programme Soustraction", "1e9", 1846761044, "flottant", "ns"),
    ("Programme Addition", "1e3", 1881751513, "flottant", "ns"),
    ("Programme Addition", "1e6", 1878958681, "flottant", "ns"),
    ("Programme Addition", "1e9", 1847345224, "flottant", "ns"),
    ("Programme Multiplication", "1e3", 14502131521, "flottant", "ns"),
    ("Programme Multiplication", "1e6", 14542608163, "flottant", "ns"),
    ("Programme Multiplication", "1e9", 14365884401, "flottant", "ns"),
    ("Programme Division", "1e3", 76862484510, "flottant", "ns"),
    ("Programme Division", "1e6", 77630934641, "flottant", "ns"),
    ("Programme Division", "1e9", 77440679578, "flottant", "ns"),
]

# Créer les lignes à ajouter
rows = []
for op, scale, val, dtype, unit in float_data:
    if unit == "ns":
        val_s = val / 1e9
    elif unit == "ms":
        val_s = val / 1e3
    elif unit == "us":
        val_s = val / 1e6
    else:
        val_s = val
    rows.append({
        "param_tfhe": "FheInt64",
        "operation": op,
        "temps_moyen_s": val_s,
        "ecart_type_s": None,
        "nb_chiffres": 2,
        "type_donnee": dtype,
        "echelle": scale
    })

# Ajouter au DataFrame existant
df = pd.concat([df, pd.DataFrame(rows)], ignore_index=True)

# Sauvegarder le fichier mis à jour
df.to_csv(file_path, index=False)
