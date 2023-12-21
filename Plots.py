import streamlit as st
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

# Generate random data
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['X', 'Y'])

st.header('1. Charts with random numbers')
st.subheader('1.1 Line Chart')
st.line_chart(chart_data)

# How widely spread each data point is
st.subheader('1.2 Area Chart')
st.area_chart(chart_data)

st.subheader('1.3 Bar Chart')
st.bar_chart(chart_data)

st.header('2. Data Visualization with Matplotlib & Seaborn')
st.subheader('2.1 Loading the dataFrame')
df = pd.read_csv('./iris.csv')
st.dataframe(df)

st.subheader('2.2 Bar Graph with Matplotlib')
fig = plt.figure(figsize=(15,8))
df['Species'].value_counts().plot(kind='bar')
st.pyplot(fig)

st.subheader('2.3 Distribution PLot with Seaborn')
fig = plt.figure(figsize=(15,8))
sns.distplot(df['SepalLengthCm'])
st.pyplot(fig)

st.header('3 Multiple Graphs in one columns')
col1,col2 = st.columns(2)
with col1:
    col1.header = 'KDE = False'
    col1.write('KDE = False')
    fig1 = plt.figure(figsize=(5,5))
    sns.distplot(df['SepalLengthCm'],kde=False)
    st.pyplot(fig1)
with col2:
    col2.header = 'Hist = False'
    fig2 = plt.figure(figsize=(5,5))
    sns.distplot(df['SepalLengthCm'],hist=False)
    st.pyplot(fig2)

st.header('4. Changing Style')
col1,col2 = st.columns(2)
with col1:
    fig = plt.figure()
    sns.set_style("darkgrid")
    sns.set_context("notebook")
    sns.distplot(df['PetalLengthCm'],hist=False)
    st.pyplot(fig)
with col2:
    fig = plt.figure()
    sns.set_theme(context = 'poster', style='darkgrid')
    sns.distplot(df['PetalLengthCm'],hist=False)
    st.pyplot(fig)


st.header('5. Exploring Different Graphs')
st.subheader('5.1 Scatter Plot')
fig, ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count-Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = df, x='Species')
st.pyplot(fig)

st.subheader('5.3 Box-Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = df, x='Species', y='PetalLengthCm')
st.pyplot(fig)

st.subheader('5.4 Violin-Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = df, x='Species', y='PetalLengthCm')
st.pyplot(fig)
