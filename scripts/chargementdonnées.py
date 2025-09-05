import pandas as pd

# Charger le dataset existant
df = pd.read_csv("données/dataset_tfhe_execution_times4.csv")

# Données à ajouter
donnees = []

# FheInt64 (type_donnee: flottant)
data_fheint64 = {
    "Programme Soustraction": [
        (1e3, [1.908381838, 1.642188214, 1.634842959, 1.67020125, 1.600325109]),
        (1e6, [2.020046279, 1.750317085, 1.763445279, 1.745604457, 1.753022024]),
        (1e9, [1.842572958, 1.619567603, 1.655862688, 1.615858999, 1.626094456]),
    ],
    "Programme Addition": [
        (1e3, [1.64344704, 1.650223883, 1.681553137, 1.616895354, 1.985445351]),
        (1e6, [1.632965051, 1.611956251, 1.627865569, 1.615114356, 1.932107078]),
        (1e9, [1.613799088, 1.602601851, 1.611748727, 1.887184678, 1.649612482]),
    ],
    "Programme Multiplication": [
        (1e3, [14.617952748, 14.3154316, 14.084898612, 14.157251803, 14.125548792]),
        (1e6, [15.139033772, 14.108600672, 14.095676867, 14.134606885, 14.024392967]),
        (1e9, [14.517999291, 14.185083199, 14.136733278, 14.033281804, 13.897482309]),
    ],
    "Programme Division": [
        (1e3, [80.221605416, 79.917327806, 79.896007971, 79.958110459, 80.552010119]),
        (1e6, [77.50155149, 77.293961227, 77.096195807, 77.269648854, 77.697803654]),
        (1e9, [76.149657112, 78.607636896, 77.204391002, 77.131278328, 77.030498902]),
    ]
}

# Ajouter les données FheInt64
for op, tuples in data_fheint64.items():
    for echelle, temps_list in tuples:
        for t in temps_list:
            donnees.append({
                "param_tfhe": "FheInt64",
                "operation": op,
                "temps_s": t,
                "nb_chiffres": 2,
                "type_donnee": "flottant",
                "echelle": int(echelle)
            })

# FheUint64 (type_donnee: entier)
data_fheuint64 = {
    "Programme Soustraction": [1.0927278894, 0.916204595, 0.94426907, 0.944478506, 1.094959],
    "Programme Addition": [1.21234, 0.939300841, 0.961347394, 0.936849397, 1.16240667],
    "Programme Multiplication": [9.365035345, 9.68697, 10.29425, 11.02237, 10.414547],
    "Programme Division": [49.460812, 53.56574657, 59.59715, 81.1921048, 85.62347777]
}

# Ajouter les données FheUint64
for op, temps_list in data_fheuint64.items():
    for t in temps_list:
        donnees.append({
            "param_tfhe": "FheUint64",
            "operation": op,
            "temps_s": t,
            "nb_chiffres": 2,
            "type_donnee": "entier",
            "echelle": None
        })

# Ajouter les nouvelles données au DataFrame
df_nouvelles = pd.DataFrame(donnees)
df = pd.concat([df, df_nouvelles], ignore_index=True)

# Sauvegarder le dataset mis à jour
df.to_csv("dataset_tfhe_execution_times4_updated.csv", index=False)
print("Données ajoutées et fichier mis à jour.")
