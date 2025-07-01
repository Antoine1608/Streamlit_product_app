#!/usr/bin/env python
# coding: utf-8

# In[5]:


import streamlit as st
import pandas as pd
import numpy as np

import plotly.express as px


# In[6]:


# page config
st.set_page_config(page_title='Basic Sales Dashboard', layout='wide')


# In[7]:


# Generate sample data
np.random.seed(42)
df = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=100),
    'Sales': np.random.randint(500, 2000, size=100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], size=100),
    'Product': np.random.choice(['Product A', 'Product B', 'Product C'], size=100)
})


# In[8]:


# Sidebar filters
st.sidebar.title('filters')
regions = st.sidebar.multiselect('Select region', df['Region'].unique(), default=df['Region'].unique())
product = st.sidebar.multiselect('Select product', df['Product'].unique(), default=df['Product'].unique())


# In[9]:


# filtered df
filtered_df = df[(df['Region'].isin(regions) & df['Product'].isin(product))]


# In[10]:


# metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total sales", f"{filtered_df['Sales'].sum():,}")
col2.metric("Average sales", f"{filtered_df['Sales'].mean():.0f}")
col3.metric("Records", f"{len(filtered_df['Sales'])}")


# In[11]:


# Charts
col1, col2 = st.columns(2)
with col1 :
    figline = px.line(filtered_df, x='Date', y='Sales', color='Region', title='Sales Over Time')
    st.plotly_chart(figline, use_container_width=True)
with col2 :
    df_by_region = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    figbar = px.bar(df_by_region, x='Region', y='Sales', title='Total Sales By Region')
    st.plotly_chart(figbar, use_container_width=True)    


# In[12]:


# Display Dataframe
st.subheader("DataFrame")
st.dataframe(filtered_df)


# In[ ]:




