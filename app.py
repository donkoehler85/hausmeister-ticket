import streamlit as st
from datetime import datetime
import pandas as pd

# Titel der App
st.title("🛠️ Hausmeister-Service Blattner Ticket-System")
st.write("Bitte füllen Sie das Formular aus, um einen Schaden oder Wunsch zu melden.")

# Formular-Felder
with st.form("ticket_form"):
    name = st.text_input("Ihr Name / Wohneinheit")
    kategorie = st.selectbox("Was ist das Problem?", ["Heizung", "Licht/Elektro", "Schlüssel/Schloss", "Garten/Außenanlage", "Sonstiges"])
    beschreibung = st.text_area("Beschreibung des Anliegens")
    dringlichkeit = st.select_slider("Wie dringend ist es?", options=["Normal", "Wichtig", "EILIG!"])
    
    submit = st.form_submit_button("Ticket absenden")

if submit:
    if name and beschreibung:
        # Hier würde man normalerweise in eine Datenbank schreiben
        timestamp = datetime.now().strftime("%d.%m.%Y %H:%M")
        
        # Bestätigung für den Mieter
        st.success(f"Vielen Dank, {name}! Ihr Ticket wurde am {timestamp} aufgenommen.")
        
        # Demo: Speichern in einer lokalen Datei (CSV)
        new_data = {"Zeit": [timestamp], "Name": [name], "Typ": [kategorie], "Info": [beschreibung], "Prio": [dringlichkeit]}
        df = pd.DataFrame(new_data)
        df.to_csv("tickets.csv", mode='a', header=not pd.io.common.file_exists("tickets.csv"), index=False)
    else:
        st.error("Bitte füllen Sie mindestens Name und Beschreibung aus.")