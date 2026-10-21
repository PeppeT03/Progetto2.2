import pandas as pd
import numpy as np

# Impostiamo un seme per rendere ripetibili i dati casuali
np.random.seed(42)

# Generiamo tutte le date possibili del 2025
date_possibili = pd.date_range(
    start="2025-01-01",
    end="2025-12-31"
)

# Generiamo 100.000 ordini
# Gli identificativi possono ripetersi perché un cliente
# può effettuare più ordini
ClienteID = np.random.randint(1, 5001, size=100000)

# Ogni ordine riguarda uno dei 20 prodotti
ProdottoID = np.random.randint(1, 21, size=100000)

# Ogni ordine contiene da 1 a 5 unità
Quantita = np.random.choice(
    np.arange(1, 6),
    size=100000
)

# Assegniamo una data casuale del 2025 a ogni ordine
DataOrdine = np.random.choice(
    date_possibili,
    size=100000
)

# Raccogliamo le colonne in un dizionario
dati_ordini = {
    "ClienteID": ClienteID,
    "ProdottoID": ProdottoID,
    "Quantita": Quantita,
    "DataOrdine": DataOrdine
}

# Creiamo il DataFrame degli ordini
ordini = pd.DataFrame(dati_ordini)

# Controlliamo le prime righe
print(ordini.head())

# Salviamo il CSV senza l'indice
ordini.to_csv("ordini.csv", index=False)

print("File ordini.csv creato:", ordini.shape)