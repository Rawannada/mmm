import streamlit as st
import pandas as pd 
#title
st.title("first streamlit app")
name = st.text_input("enter your name",placeholder="type here ...")
# if name != "type here ...":
#     st.write(f"hello {name}🥰")

st.write(f"hello {name}🥰")
upload =st.file_uploader("upload a csv file",type=["csv"])
if upload:
    df=pd .read_csv(upload)
    st.write("dataframe:")
    st.dataframe(df.head())
    
    
    st.download_button(
        label="download csv",
        data=df.to_csv(index=False),
        file_name="dowenloaded_data.csv",
        mime="text/csv"
    )
    
    

    
