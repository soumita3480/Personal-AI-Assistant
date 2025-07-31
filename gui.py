import streamlit as st
import pandas as pd

st.title("Give Your Inputs")

with st.form(key="user_info_form"):
    button=None
    st.subheader("Bubu loves Dudu?")
    lv=st.radio("choose option my pookiee boo!!",['None','Yes','No'])
    st.subheader("Dudu is always right?")
    rd=st.radio("choose option Bubu",['None','Yes','No'])
    st.subheader("Dudu will order biriyani for Bubu?")
    box=st.selectbox("choose option if you are hungry Bubu",['None','Yes','No'])

    button=st.form_submit_button()
    if button:
        if lv.lower() == 'yes' and rd.lower()=='yes' and box.lower()=='yes':
            st.markdown("Dudu is happy!")
        else:
            st.write('Dudu is sad :(')
            st.warning('Choose Wisely Bubu!!!')
    else:
        st.write('No Message for Bubu')
        

