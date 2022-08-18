import streamlit as st 
import pandas as pd
import numpy as np
from streamlit_option_menu import option_menu
import plotly_express as px


st.set_page_config(layout="wide")
st.image('logo.png', width=100)
with st.sidebar:
    select = option_menu(
        menu_title='Model Selection',
        options= ['TATA', 'AL'],
        icons = ['truck','truck'],
        menu_icon='truck-flatbed'
    )
   
col2, col3= st.columns([1.2,0.2])



with col2:
    st.title('Hyper Automotives')
    st.caption('Innovative Solution')

    st.header('Building an automotive future'.capitalize())
    
    st.subheader('Reducing Global automobile emissions & hastening the electrification of vehicles.!'.capitalize())
    
    #Plot and visualize efficiency of different component
    def interactiveplots(df):
        comp = st.selectbox('Select to See Report Comparision', 
        options=['Injector','Railing', 'ECU'])
        if comp == 'Injector':
            plot = px.line(df[['iq','iq_pred']], title='Fuel Injection Compared')
            st.plotly_chart(plot)
        if comp == 'Railing':
            plot = px.line(df[['rp','rp_pred']], title='Fuel Injection Compared')
            st.plotly_chart(plot)  
        if comp == 'ECU':
            plot = px.line(df[['mu','mu_pred']], title='Fuel Injection Compared')
            st.plotly_chart(plot)   
    
    #If TATA is selected
    if select == 'TATA':
        st.image('Background MH 12 PQ 5841.png', caption='Model-TATA 5841', width= 750)
        #Load the csv file of the specific model
        df = pd.read_csv('AB 12 BC 3456.csv')
        
        #option menu to select graph or data
        grph = option_menu(
        menu_title='Visualize',
        options= ['Interactive Graph', 'Sample data'],
        icons = ['graph-up-arrow','clipboard-data'],
        menu_icon='activity',
        orientation='horizontal'
    )
    #Choose if you want to see an interactive graph or Sample of the data
        if grph == 'Interactive Graph':
            x = interactiveplots(df)
            x
        if grph == 'Sample data':
            y = df.sample(10)
            y

    #If Ashok Leyland is Selected
    if select == 'AL':
        st.image('Background TN 34 AB 7345.png', caption='Model-AL 7345', width= 750)
        
        #Load the data of the model
        df = pd.read_csv('BC 12 CD 3456.csv')
        
        #option menu to select graph or data
        grph = option_menu(
        menu_title='Visualize',
        options= ['Interactive Graph', 'Sample data'],
        icons = ['graph-up-arrow','clipboard-data'],
        menu_icon='activity',
        orientation='horizontal'
    )
    
    #Choose if you want to see an interactive graph or Sample of the data
        if grph == 'Interactive Graph':
            x = interactiveplots(df)
            x
        if grph == 'Sample data':
            y = df.sample(10)
            y