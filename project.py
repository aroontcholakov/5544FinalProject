import streamlit as st
import pandas as pd
import random
import os
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import altair as alt

gdp = pd.read_csv(r'https://github.com/aroontcholakov/5544FinalProject/blob/568a6bf6268a16a8c1727ff95564ec5f3d756508/gdp+emissions.csv', sep=',')
gov = pd.read_csv(r'https://github.com/aroontcholakov/5544FinalProject/blob/568a6bf6268a16a8c1727ff95564ec5f3d756508/government_type+avg_emissions.csv', sep=',')
capita = pd.read_csv(r'https://github.com/aroontcholakov/5544FinalProject/blob/568a6bf6268a16a8c1727ff95564ec5f3d756508/emissions_per_capita.csv', sep=',')



st.title('Final Project')
