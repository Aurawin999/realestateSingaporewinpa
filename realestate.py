import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title='Singapore Realestate Dashboard',page_icon=':bar_chart:',layout='wide')
df = pd.read_csv('HDDclean.csv')
st.sidebar.header('Please Filter Here')

town_name = st.sidebar.multiselect(
    'Select Town:', 
    options = df['town'].unique(), 
    default=df['town'].unique()[:5]
)

year_name = st.sidebar.multiselect(
    'Select Year:', 
    options = df['year'].unique(), 
    default=df['year'].unique()[:5]
)

flatType_name = st.sidebar.multiselect(
    'Select Flat Type:', 
    options = df['flat_type'].unique(), 
    default=df['flat_type'].unique()[:5]
)
st.title(':bar_chart: Real Estate Analysis of Singapore')
total_resaleprice = df['resale_price'].sum()
total_remaninLease = df['remaining_lease'].nunique()
a,b = st.columns(2)
with a:
    st.subheader('Total Resale Price')
    st.subheader(f'US $ {total_resaleprice}')
with b:
    st.subheader('Remaining Lease Status')
    st.subheader(total_remaninLease)
selection = df.query('town == @town_name and year == @year_name and flat_type == @flatType_name')

total_resaleprice = selection.groupby('year')['resale_price'].sum().sort_values()
fig_by_resaleprice = px.bar(
    total_resaleprice,
    x = total_resaleprice.index,
    y = total_resaleprice.values,
    title = 'Yearly Resale Price'
)
c,d = st.columns(2)
c.plotly_chart(fig_by_resaleprice, use_container_width = True)

fig_by_town = px.pie(
    selection,
    values = 'resale_price',
    names = 'town',
    title = 'Resale Price by Town'
)
d.plotly_chart(fig_by_town, use_container_width = True)

total_resaleprice = selection.groupby('flat_type')['resale_price'].sum().sort_values()
fig_by_flatType = px.line(
    total_resaleprice,
    x = total_resaleprice.index,
    y = total_resaleprice.values,
    title = 'Resale Price by Flat Type'
)
e,f = st.columns(2)
e.plotly_chart(fig_by_flatType, use_container_width = True)

fig_by_resaleprice = px.pie(
    selection,
    values = 'resale_price',
    names = 'flat_type',
    title = 'Resale Price by Flat Type'
)
f.plotly_chart(fig_by_resaleprice, use_container_width = True)
    

