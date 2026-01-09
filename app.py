import streamlit as st
import pandas as pd
from datetime import datetime
# Wir nutzen gspread für den stabilen Schreibzugriff
import gspread

st.set_page_config(page_title="Hausmeister-Service", page_icon="🛠️")

# KONFIGURATION
# WICHTIG: Die URL muss auf /export?format=csv enden für den Lesezugriff
# Aber für gspread nutzen wir die normale URL
SHEET_URL = "https://docs.google.com/spreadsheets/d/14FQqsnORuzzn3XUE-9I1q9TL1vWsf4Vagbk_h0_3yug/edit?usp=sharing"

st.title("🛠️ Ticket-System Blattner Services")

with st.form("ticket_form", clear_on_submit=True):
    name = st.text_input("Name / Wohneinheit")
    kategorie = st.selectbox("Anliegen", ["Licht", "Wasser", "Heizung", "Sonstiges"])
    nachricht = st.text_area("Details")
    prio = st.select_slider("Dringlichkeit", options=["Normal", "Wichtig", "Eilt!"])
    submit = st.form_submit_button("Absenden")

if submit:
    if name and nachricht:
        try:
            # Verbindung über gspread (einfacher für Schreibrechte)
            # Hinweis: Für die 'Einfache Freigabe' muss das Sheet für 'Jeden mit Link' als Editor frei sein
            gc = gspread.public_spreadsheet(SHEET_URL) # Für öffentliche Sheets
            # Wenn das Sheet nicht komplett öffentlich ist, nutzen wir diesen Weg:
            
            # Alternative: Wir hängen die Zeile einfach an
            # Hier ist ein Trick, wie man es ohne komplexe API-Keys macht:
            # Wir nutzen die URL und schreiben direkt via Google Forms-Schnittstelle ODER 
            # wir nutzen die Streamlit Secrets.
            
            st.warning("Verbindung wird aufgebaut...")
            
            # Da gspread ohne Service-Account bei privaten Sheets hakt, 
            # hier die Lösung für den Fehler:
            # Der Fehler 'UnsupportedOperation' kommt oft, wenn die App 
            # versucht, eine Datei zu überschreiben, die sie nur lesen darf.
            
            st.error("Technischer Hinweis: Für Schreibzugriff benötigt Streamlit Cloud 'Secrets'.")
        except Exception as e:
            st.error(f"Fehler: {e}")
