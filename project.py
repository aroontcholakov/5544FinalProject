import streamlit as st
import pandas as pd
import random
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

gdp = pd.read_csv(r'https://raw.githubusercontent.com/aroontcholakov/5544FinalProject/main/gdp%2Bemissions.csv', sep=',')
gov = pd.read_csv(r'https://raw.githubusercontent.com/aroontcholakov/5544FinalProject/main/government_type%2Bavg_emissions.csv', sep=',')
capita = pd.read_csv(r'https://raw.githubusercontent.com/aroontcholakov/5544FinalProject/main/emissions_per_capita.csv', sep=',')

st.title('Final Project')
