import streamlit as st
import data 
import pandas as pd
import os 

if os.path.exists('Out.xlsx'):
    os.remove('Out.xlsx')

excelRaw = st.file_uploader('Upload a file') 
if excelRaw is not None:
    rawOrders = pd.read_excel(excelRaw)
    dfRaw =  rawOrders.drop(['ID','Start time','Completion time','Email','Name'], axis=1)
else:
    rawOrders = pd.read_excel(r'Raw.xlsx')
    dfRaw =  rawOrders.drop(['ID','Start time','Completion time','Email','Name'], axis=1)    

def create_data():
    data.main(dfRaw)
    

def main():
    
    create_data()
    if os.path.exists('Out.xlsx'):
        data_times = pd.read_excel('Out.xlsx',sheet_name=4)
        st.title('Eggs and Times it needs to be completed')
        st.dataframe(data_times)


if __name__ == '__main__':
    main()