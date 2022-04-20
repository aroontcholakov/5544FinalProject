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

df_gov.drop(df_gov.index[0], inplace=True)
df_emissions.drop(df_emissions.index[0], inplace=True)
df_percapita.drop(df_percapita.index[0], inplace=True)

st.title('F')
st.write(df_emissions.head())
st.write(df_gov.head())

# Government Type Plot
sns.set(rc = {'figure.figsize':(20,20)})
ax = sns.boxplot(x="government type", y="average emissions", data=df_gov)
ax = sns.swarmplot(x="government type", y="average emissions", data=df_gov, color=".25")
ax.set_xticklabels(ax.get_xticklabels(),rotation = 10)


# Emissions GDP plot
df_gdp = df_emissions[['Country', '2000_gdp', '2001_gdp', '2002_gdp', '2003_gdp', '2004_gdp', '2005_gdp',
                                 '2006_gdp', '2007_gdp', '2008_gdp', '2009_gdp', '2010_gdp', '2011_gdp', '2012_gdp',
                                 '2013_gdp', '2014_gdp', '2015_gdp', '2016_gdp', '2017_gdp', '2018_gdp', '2019_gdp']]
df_gdp = df_gdp.rename(columns={'2000_gdp' : '2000', '2001_gdp' : '2001','2002_gdp' : '2002', '2003_gdp' : '2003',
    '2004_gdp' : '2004', '2005_gdp' : '2005','2006_gdp' : '2006', '2007_gdp' : '2007',
    '2008_gdp' : '2008', '2009_gdp' : '2009','2010_gdp' : '2010', '2011_gdp' : '2011',
    '2012_gdp' : '2012', '2013_gdp' : '2013', '2014_gdp' : '2014', '2015_gdp' : '2015',
    '2016_gdp' : '2016', '2017_gdp' : '2017', '2018_gdp' : '2018', '2019_gdp' : '2019'})
melted_gdp = pd.melt(df_gdp, id_vars=['Country'], value_vars=['2000', '2001', '2002', '2003', '2004', '2005',
                                                              '2006', '2007', '2008', '2009', '2010', '2011',
                                                              '2012', '2013', '2014', '2015', '2016', '2017',
                                                              '2018', '2019'], var_name='Year', value_name='GDP')
#data manip chart 2
df_emissions_only = df_emissions.iloc[:, 0:21]
df_full_emissions = df_emissions_only.drop([1, 6, 9, 10, 11, 12, 24, 25, 26, 28, 32, 38, 43, 48, 51])
df_full_emissions
melted_emissions = pd.melt(df_full_emissions, id_vars=['Country'], value_vars=['2000', '2001', '2002', '2003', '2004', '2005',
                                                              '2006', '2007', '2008', '2009', '2010', '2011',
                                                              '2012', '2013', '2014', '2015', '2016', '2017',
                                                              '2018', '2019'], var_name='Year', value_name='Emissions')

#dropdown menu
countries = list(melted_gdp['Country'].unique())
selection = alt.selection_single(name='Select', fields=['Country'], bind=alt.binding_select(options=countries))

countries2 = list(melted_emissions['Country'])
selection2 = alt.selection_single(name='Select', fields=['Country'], bind=alt.binding_select(options=countries2))

chart1 = alt.Chart(melted_gdp).mark_line().add_selection(
    selection
).encode(
    x='Year',
    y=alt.Y('GDP:Q', scale=alt.Scale(type="log")),
    color=alt.Color('Country',legend=alt.Legend(symbolLimit=62)),
    opacity=alt.condition(selection, alt.value(0.75), alt.value(0.20))
).properties(
    width=400,
    height=800
)

chart2 = alt.Chart(melted_emissions).mark_line().add_selection(
    selection2
).encode(
    x='Year',
    y=alt.Y('Emissions:Q', scale=alt.Scale(type="log")),
    color=alt.Color('Country',legend=alt.Legend(symbolLimit=62)),
    opacity=alt.condition(selection2, alt.value(1), alt.value(0.07))
).properties(
    width=400,
    height=800
)

both = chart1 | chart2
st.altair_chart(both, use_container_width=False)
