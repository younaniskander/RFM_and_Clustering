

import streamlit as st 
import numpy as np
import pandas as pd


df = pd.read_csv("Clustered_data.csv")
pivot_total = pd.read_csv("Clustered_pivot.csv")

def get_Recommendation(User,num_of_rec) :
    Cluster = df[df["User_Id"] == int(User)]["Cluster"].unique()[0]
    df_cluster = df[df["Cluster"] == Cluster]
    df_cluster = df_cluster.groupby("Mer_Id")["Trx_Vlu"].sum().nlargest(int(num_of_rec))
    for index , mer in enumerate(df_cluster.index):
        st.text(f"Recommendation number {index+1} of user {User} is {mer}")
        
def main():
    User = st.text_input("Enter User Id")
    num_of_rec = st.text_input("Enter num of Rec")
    if st.button("recommend"):
        get_Recommendation(User , num_of_rec)
main()
    
