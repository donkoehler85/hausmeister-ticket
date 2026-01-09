import streamlit as st
import pandas as pd

st.set_page_config(page_title="Hausmeister Zentrale", layout="wide")

# 1. LINK ZUM SHEET (Wichtig: Am Ende muss /export?format=csv stehen!)
# Kopiere deinen Sheet Link bis zum langen Code und hänge das Ende an:
SHEET_ID = "18AutADfei-GjIC-hKokIOGrSAlzeMOpJHtxlKLgWXNY"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv"

st.title("📋 Offene Reparatur-Aufträge")

try:
    # Daten einlesen (reiner Lesezugriff ist kinderleicht)
    df = pd.read_csv(URL)
    
    # Kleine Statistik
    st.metric("Gesamtanzahl Tickets", len(df))
    
    # Filter-Optionen an der Seite
    st.sidebar.header("Filter")
    suche = st.sidebar.text_input("Nach Mieter suchen")
    
    if suche:
        df = df[df.iloc[:, 1].str.contains(suche, case=False, na=False)]

    # Die Tabelle schön anzeigen
    st.dataframe(df, use_container_width=True)
    
    # Button zum manuellen Aktualisieren
    if st.button("Liste aktualisieren"):
        st.rerun()

except Exception as e:
    st.error("Konnte Daten nicht laden. Hast du das Sheet für 'Jeden mit Link' freigegeben?")
