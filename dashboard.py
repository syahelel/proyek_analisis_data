import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

st.set_option('deprecation.showPyplotGlobalUse', False)
day_df = pd.read_csv('data.csv')

st.title('ANALISIS DATA BIKE-SHARING 2011-2012')
st.header('penyebaran penyewa sepedah berdasarkan suhu dan musim (2011-2012)')

plt.figure(figsize=(10,6))

sns.scatterplot(x='temp', y='total_count', data=day_df, hue='season')

plt.xlabel("suhu (degC)")
plt.ylabel("Total penyewa")
plt.title("penyebaran penyewa sepedah berdasarkan suhu dan musim (2011-2012)")

# Show the plot
plt.tight_layout()
st.pyplot()


st.subheader("Perbandingan penyewaan sepedah perbulan dan permusim")
 
col1, col2 = st.columns(2)

with col1:
    plt.figure(figsize=(10,6))

    sns.barplot(x='season', y='total_count', data=day_df, hue='year')

    plt.xlabel("musim")
    plt.ylabel("Total penyewa")
    plt.title("Total penyewaan dalam musiman")

    st.pyplot()

with col2:
    plt.figure(figsize=(10,6))

    sns.barplot(x='month', y='total_count', data=day_df, hue='year')

    plt.xlabel("Bulan")
    plt.ylabel("Total Penyewa")
    plt.title("Total Penyewaan sepeda dalam bulanan")

    st.pyplot()