import streamlit as st
import data 
import pandas as pd
import os 
from io import BytesIO
from pyxlsb import open_workbook as open_xlsb

st.title("Order System V2")

if os.path.exists('Out.xlsx'):
    os.remove('Out.xlsx')


excelRaw = st.file_uploader('Upload xlsx file') 

if excelRaw is not None:
    rawOrders = pd.read_excel(excelRaw)
    dfRaw =  rawOrders.drop(['ID','Start time','Completion time','Email','Name'], axis=1)
else:
    rawOrders = pd.read_excel(r'Raw.xlsx')
    dfRaw =  rawOrders.drop(['ID','Start time','Completion time','Email','Name'], axis=1)    

def create_data():
    data.main(dfRaw)


# def to_excel(df):
#     output = BytesIO()
#     writer = pd.ExcelWriter(output,engine="xlsxwriter")
#     df.to_excel(writer, index=False)



def main():
    create_data()
    if os.path.exists('Out.xlsx'):
        data_times = pd.read_excel('Out.xlsx',sheet_name=4)
        
        st.header("Eggs and Times they need to be completed")
        st.dataframe(data_times)

        dfOut = pd.read_excel("Out.xlsx")

        # st.download_button(
        #     label="Download Full Stock list",
        #     data=csv,
        #     file_name="Out.csv", 
        #     mime='text/csv'
        #     )


if __name__ == '__main__':
    main()