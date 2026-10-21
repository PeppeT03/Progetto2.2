import pandas as pd
import numpy as np

# Rendiamo ripetibili le estrazioni casuali
np.random.seed(42)

# Creiamo 20 identificativi univoci, da 1 a 20
ProdottoID = np.arange(1, 21)

# Assegniamo casualmente una categoria a ogni prodotto
Categoria = np.random.choice(
    ["Elettronica", "Casa", "Sport", "Abbigliamento"],
    size=20
)

# Assegniamo un fornitore
Fornitore = np.random.choice(
    ["Amazon", "Battolini", "GYS"],
    size=20
)

# Generiamo prezzi tra 10 e 500 euro, arrotondati ai centesimi
Prezzo = np.round(
    np.random.uniform(10, 500, size=20),
    2
)

# Organizziamo i dati in un dizionario
dati_prodotti = {
    "ProdottoID": ProdottoID,
    "Categoria": Categoria,
    "Fornitore": Fornitore,
    "Prezzo": Prezzo
}

# Creiamo il DataFrame dei prodotti
prodotti = pd.DataFrame(dati_prodotti)

# Controlliamo il risultato
print(prodotti.head())
print("Dimensioni prodotti:", prodotti.shape)

# Salviamo in JSON, con un record per prodotto
# In orient="records" l'indice non viene incluso
prodotti.to_json(
    "prodotti.json",
    orient="records",
    indent=2
)

print("File prodotti.json creato")