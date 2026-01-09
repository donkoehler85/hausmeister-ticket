import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="Hausmeister-Service", page_icon="🔧")

# 1. Verbindung zum Google Sheet herstellen
# Die URL ist der Link zu deinem Google Sheet (Freigabe: "Jeder mit dem Link kann bearbeiten")
sheet_url = "https://docs.google.com/spreadsheets/d/14FQqsnORuzzn3XUE-9I1q9TL1vWsf4Vagbk_h0_3yug/edit?usp=sharing"
conn = st.connection("gsheets", type=GSheetsConnection)

st.title("🔧 Ticket-System Blattner Services")

with st.form("ticket_form", clear_on_submit=True):
    name = st.text_input("Name / Wohneinheit")
    kategorie = st.selectbox("Anliegen", ["Licht", "Wasser", "Heizung", "Garten", "Sonstiges"])
    beschreibung = st.text_area("Beschreibung")
    dringlichkeit = st.select_slider("Dringlichkeit", options=["Normal", "Wichtig", "NOTFALL"])
    
    submit = st.form_submit_button("Ticket absenden")

if submit:
    if name and beschreibung:
        # Bestehende Daten laden
        existing_data = conn.read(spreadsheet=sheet_url, usecols=[0,1,2,3,4,5])
        
        # Neues Ticket erstellen
        new_ticket = pd.DataFrame([{
            "Zeitstempel": datetime.now().strftime("%d.%m.%Y %H:%M"),
            "Name": name,
            "Kategorie": kategorie,
            "Beschreibung": beschreibung,
            "Dringlichkeit": dringlichkeit,
            "Status": "Offen"
        }])
        
        # Daten kombinieren und zurückschreiben
        updated_df = pd.concat([existing_data, new_ticket], ignore_index=True)
        conn.update(spreadsheet=sheet_url, data=updated_df)
        
        st.success("Ticket wurde gespeichert!")
        # HIER KOMMT DER TRICK FÜR DIE BENACHRICHTIGUNG (siehe unten)
    else:
        st.error("Bitte Felder ausfüllen.")
