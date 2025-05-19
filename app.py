
import datetime
import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st

# Data z tabulky pro jednotlivé poškození listové plochy
DNY = np.array([29, 39, 49, 59, 69, 79, 89, 99, 109, 119, 129])
ZTRATY = {
    10: [1, 2, 4, 5, 6, 6, 6, 5, 5, 4, 3],
    20: [3, 5, 7, 9, 11, 12, 12, 11, 9, 7, 5],
    30: [4, 7, 12, 15, 17, 18, 18, 16, 14, 10, 7],
    40: [6, 10, 15, 19, 22, 23, 23, 21, 16, 12, 9],
    50: [7, 12, 20, 24, 27, 29, 29, 26, 23, 18, 11],
    60: [9, 15, 23, 29, 32, 35, 35, 33, 28, 22, 13],
    70: [10, 17, 26, 34, 38, 41, 41, 38, 33, 25, 16],
    80: [12, 20, 30, 38, 44, 47, 47, 43, 38, 29, 18],
    90: [13, 22, 35, 44, 50, 52, 52, 48, 42, 33, 20],
    100: [15, 25, 38, 48, 56, 59, 59, 55, 47, 37, 22]
}

def vypocitej_ztratu(den_seti: str, den_poskozeni: str, poskozeni_listove_plochy: int) -> float:
    datum_seti = datetime.datetime.strptime(den_seti, '%d.%m.%Y')
    datum_poskozeni = datetime.datetime.strptime(den_poskozeni, '%d.%m.%Y')
    dny_od_seti = (datum_poskozeni - datum_seti).days

    if dny_od_seti <= DNY[0]:
        x = np.array([DNY[0], DNY[1]]).reshape(-1, 1)
        y = [ZTRATY[poskozeni_listove_plochy][0], ZTRATY[poskozeni_listove_plochy][1]]
    elif dny_od_seti >= DNY[-1]:
        x = np.array([DNY[-2], DNY[-1]]).reshape(-1, 1)
        y = [ZTRATY[poskozeni_listove_plochy][-2], ZTRATY[poskozeni_listove_plochy][-1]]
    else:
        for i in range(len(DNY) - 1):
            if DNY[i] <= dny_od_seti <= DNY[i + 1]:
                x = np.array([DNY[i], DNY[i + 1]]).reshape(-1, 1)
                y = [ZTRATY[poskozeni_listove_plochy][i], ZTRATY[poskozeni_listove_plochy][i + 1]]
                break

    model = LinearRegression().fit(x, y)
    ztrata = model.predict(np.array([[dny_od_seti]]))[0]
    return round(ztrata, 2)

# Streamlit UI
st.title("Odhad ztráty na výnosu kukuřice")

with st.form("vstupni_formular"):
    den_seti = st.text_input("Datum setí (dd.mm.rrrr)", "10.04.2025")
    den_poskozeni = st.text_input("Datum škodné události (dd.mm.rrrr)", "03.05.2025")
    poskozeni = st.slider("Poškození listové plochy (%)", 10, 100, 70, step=10)
    odeslat = st.form_submit_button("Vypočítat")

if odeslat:
    try:
        vysledek = vypocitej_ztratu(den_seti, den_poskozeni, poskozeni)
        st.success(f"Odhadovaná ztráta na výnosu je {vysledek} %")
    except Exception as e:
        st.error(f"Chyba při výpočtu: {e}")
