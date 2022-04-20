import streamlit as st
import pandas as pd
import random
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

df_emissions = pd.read_csv(r'https://raw.githubusercontent.com/aroontcholakov/5544FinalProject/main/gdp%2Bemissions.csv', sep=',')
df_gov = pd.read_csv(r'https://raw.githubusercontent.com/aroontcholakov/5544FinalProject/main/government_type%2Bavg_emissions.csv', sep=',')
df_percapita = pd.read_csv(r'https://raw.githubusercontent.com/aroontcholakov/5544FinalProject/main/emissions_per_capita.csv', sep=',')



st.title('F')
st.write(df_emissions.head())
st.write(df_gov.head())

