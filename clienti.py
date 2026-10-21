import pandas as pd
import numpy as np

# Rendiamo ripetibili le estrazioni casuali
np.random.seed(42)

# Creiamo 5.000 identificativi progressivi e senza ripetizioni
ClienteID = np.arange(1, 5001)

# Ogni cliente appartiene a una regione
Regione = np.random.choice(
    ["Nord", "Centro", "Sud"],
    size=5000
)

# Ogni cliente appartiene a un segmento
Segmento = np.random.choice(
    ["Premium", "Standard"],
    size=5000
)

# Organizziamo i dati in un dizionario
dati_clienti = {
    "ClienteID": ClienteID,
    "Regione": Regione,
    "Segmento": Segmento
}

# Creiamo il DataFrame dei clienti
clienti = pd.DataFrame(dati_clienti)

# Controlliamo le prime righe e le dimensioni
print(clienti.head())
print("Dimensioni clienti:", clienti.shape)

# Salviamo i dati in CSV senza l'indice
clienti.to_csv("clienti.csv", index=False)

print("File clienti.csv creato")