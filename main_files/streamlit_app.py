import streamlit as st
import data 
import pandas as pd
import os 

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

def egg_time_page():
    if os.path.exists('Out.xlsx'):
        data_times = pd.read_excel('Out.xlsx',sheet_name=4)
        
        st.header("Eggs and Times they need to be completed")
        st.dataframe(data_times)
        dfOut = pd.read_excel("Out.xlsx")

def stock_data_page():
    st.title('Stock Data')

    st.header("Drinks, Coffee and Cereal")
    data_juice = pd.read_excel('Out.xlsx',sheet_name=0)
    index_zero = data_juice[(data_juice['Amount']==0)].index
    data_juice.drop(index_zero, inplace=True)
    st.dataframe(data_juice)

    st.header("Eggs")
    data_eggs = pd.read_excel('Out.xlsx',sheet_name=1)
    index_zero = data_eggs[(data_eggs['Amount']==0)].index
    data_eggs.drop(index_zero, inplace=True)
    st.dataframe(data_eggs)

    st.header('Meat')
    data_meat = pd.read_excel('Out.xlsx',sheet_name=2)
    index_zero = data_meat[(data_meat['Amount']==0)].index
    data_meat.drop(index_zero, inplace=True)
    st.dataframe(data_meat)

    st.header('Starch and Veg')
    data_veg =pd.read_excel('Out.xlsx',sheet_name=3)
    # index_veg = data_veg[(data_veg['Amount']==0)].index
    # data_veg.drop(index_zero, inplace=True)
    st.dataframe(data_veg)








def main():
    create_data()
    page = st.sidebar.selectbox(
    "Select Page",[
    "Egg Time","Stock Data"
    ])
    if page =='Egg Time':
        egg_time_page()

    elif page == 'Stock Data':
        stock_data_page()

        st.download_button(
            label="Download Full Stock list",
            data='text',
            file_name="Out.csv", 
            mime='text/csv'
            )


if __name__ == '__main__':
    main()