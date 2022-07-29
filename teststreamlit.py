import streamlit as st
import pandas as pd
import numpy as np
st.header("SHIVA WEB APP")
st.write("Streamlit In My Linux")
#dataframe
data1 = [{'satu': 1, 'dua': 2,'tiga': 3}, # index ke-0
        {'satu': 1, 'dua': 2,'tiga': 3}, # index ke-1
        {'satu': 1, 'dua': 2,'tiga': 3}] # index ke-3

data2 = {'Nama' : ['ASIFA','SAIFA','ISAFA','FISAA'],
        'Kelas' : ['TIA','TIB','TIB','TIA'],
        'NIM' : ['S1TIS210438','S1TIS210438','S1TIS210438','S1TIS210438']}

data3 =[{'genap':2,'ganjil':1},
        {'genap':4,'ganjil':3},
        {'ganjil':5,'genap':6}]
#tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Tab 1", "Tab 2", "Tab3", "Tab4", "Tab5"])
with tab1:
	st.header("Tab 1")
	df1 = pd.DataFrame(data1)
	st.table(df1)
	st.write("Table DataFrame 1")
with tab2:
	st.header("Tab 2")
	df2 = pd.DataFrame(data2)
	st.table(df2)
	st.write("Table DataFrame 2")
with tab3:
	st.header("Tab 3")
	df3 = pd.DataFrame(data3)
	st.table(df3)
	st.write("Table DataFrame 3")
with tab4:
	st.header("Tab 4")
	df4 = pd.DataFrame(
    np.random.randn(5, 5),
    columns=('col %g' % i for i in range(5)))
	st.table(df4)
	st.write("Data Random Columns")
with tab5:
	st.header("Tab 5")
	st.line_chart(df3)
	st.write("Line Chart dari DataFrame 3")
	










