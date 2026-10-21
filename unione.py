import pandas as pd

# =========================================
# 1. LETTURA DELLE TRE SORGENTI
# =========================================

ordini = pd.read_csv("ordini.csv")
prodotti = pd.read_json("prodotti.json")
clienti = pd.read_csv("clienti.csv")

# Verifichiamo le dimensioni iniziali
print("--- DIMENSIONI INIZIALI ---")
print("Ordini:", ordini.shape)
print("Prodotti:", prodotti.shape)
print("Clienti:", clienti.shape)


# =========================================
# 2. UNIONE ORDINI E PRODOTTI
# =========================================

# Colleghiamo ogni ordine al prodotto acquistato.
# Il left join conserva tutti gli ordini.
df_vendite = ordini.merge(
    prodotti,
    how="left",
    on="ProdottoID"
)

print("\nDopo l'unione con i prodotti:", df_vendite.shape)


# =========================================
# 3. UNIONE CON I CLIENTI
# =========================================

# Aggiungiamo Regione e Segmento utilizzando ClienteID.
# Manteniamo tutte le righe degli ordini.
df_vendite = df_vendite.merge(
    clienti,
    how="left",
    on="ClienteID"
)

print("Dopo l'unione con i clienti:", df_vendite.shape)


# =========================================
# 4. CALCOLO DEL VALORE TOTALE
# =========================================

# Valore del singolo ordine = prezzo unitario x quantità
df_vendite["ValoreTotale"] = (
    df_vendite["Prezzo"] * df_vendite["Quantita"]
)


# =========================================
# 5. MISURA DELLA MEMORIA INIZIALE
# =========================================

print("\n--- TIPI ORIGINALI ---")
print(df_vendite.dtypes)

# Sommiamo la memoria delle colonne e dell'indice.
# Dividiamo per 1.048.576 per ottenere MiB.
memoria_iniziale = (
    df_vendite.memory_usage(deep=True).sum()
    / 1048576
)

print(f"Memoria iniziale: {memoria_iniziale:.2f} MiB")


# =========================================
# 6. OTTIMIZZAZIONE DEI TIPI NUMERICI
# =========================================

# Pandas sceglie un tipo intero più piccolo compatibile
# con i valori presenti in ciascuna colonna.
colonne_intere = ["ClienteID", "ProdottoID", "Quantita"]

for colonna in colonne_intere:
    df_vendite[colonna] = pd.to_numeric(
        df_vendite[colonna],
        downcast="integer"
    )

# Convertiamo il testo delle date nel tipo datetime
df_vendite["DataOrdine"] = pd.to_datetime(
    df_vendite["DataOrdine"]
)

# Riduciamo la dimensione dei tipi decimali.
# Attenzione: float32 ha meno precisione di float64.
colonne_decimali = ["Prezzo", "ValoreTotale"]

for colonna in colonne_decimali:
    df_vendite[colonna] = pd.to_numeric(
        df_vendite[colonna],
        downcast="float"
    )


# =========================================
# 7. OTTIMIZZAZIONE DELLE COLONNE TESTUALI
# =========================================

# Sono colonne con pochi valori distinti ripetuti
# su molte righe: category può ridurne la memoria.
colonne_categoriche = [
    "Categoria",
    "Fornitore",
    "Regione",
    "Segmento"
]

for colonna in colonne_categoriche:
    df_vendite[colonna] = df_vendite[colonna].astype(
        "category"
    )


# =========================================
# 8. VERIFICA DELL'OTTIMIZZAZIONE
# =========================================

print("\n--- TIPI OTTIMIZZATI ---")
print(df_vendite.dtypes)

memoria_ottimizzata = (
    df_vendite.memory_usage(deep=True).sum()
    / 1048576
)

print(f"Memoria ottimizzata: {memoria_ottimizzata:.2f} MiB")

# Calcoliamo la percentuale di memoria risparmiata
risparmio_percentuale = (
    (memoria_iniziale - memoria_ottimizzata)
    / memoria_iniziale
    * 100
)

print(f"Memoria risparmiata: {risparmio_percentuale:.2f}%")


# =========================================
# 9. FILTRO DEGLI ORDINI DI VALORE ELEVATO
# =========================================

# Selezioniamo soltanto gli ordini superiori a 100 euro.
# copy() crea una copia indipendente del risultato.
filtro = df_vendite["ValoreTotale"] > 100

ordini_alto_valore = df_vendite.loc[filtro].copy()

# Verifichiamo le dimensioni e le prime righe
print("\n--- ORDINI CON VALORE > 100 ---")
print("Dimensioni:", ordini_alto_valore.shape)
print(ordini_alto_valore.head())


# =========================================
# 10. CALCOLO DELLE STATISTICHE
# =========================================

# Calcoliamo totale e media solo sugli ordini filtrati
totale_valore = ordini_alto_valore["ValoreTotale"].sum()

media_valore = ordini_alto_valore["ValoreTotale"].mean()

print("\n--- STATISTICHE DEGLI ORDINI FILTRATI ---")
print(f"Valore totale: {totale_valore:,.2f} euro")
print(f"Valore medio per ordine: {media_valore:,.2f} euro")