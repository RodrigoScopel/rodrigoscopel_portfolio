import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.set_page_config(page_title="Home", layout="wide")

c=st.container()

col1,col2,col3 = st.columns(3)

with col2:
    st.markdown("<h1 style='text-align: center; color: white;'>RODRIGO SCOPEL</h1>", unsafe_allow_html=True)
    # st.title("RODRIGO SCOPEL", anchor=None, help=None)
st.divider()

col1,col2,col3 = st.columns(3)

with col2:

    st.header("'This website was built from the ground up to showcase how my previous experiences can be transfered into the audio industry'", anchor=None, help=None)
    st.divider()
    st.subheader("Here you will find: ")
    st.markdown("1 - Career Background / CV")
    st.markdown("2 - Case Study (Spitfire Audio - Competitive Intelligence Analysis)")
    st.markdown("3 - Case Study (Spitfire Audio - Consumer Study Analysis)")
    st.markdown("4 - How can a Chemical Engineer and Materials Scientist help to drive innovation in the audio industry?")


st.divider()

st.markdown("<h5 style='text-align: center; color: white;'>London</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: white;'>2024</h6>", unsafe_allow_html=True)
