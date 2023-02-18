import requests
import streamlit as st
import array as ary
import pandas as pd
import altair as alt


st.set_page_config(page_title="My Webpage", page_icon=":skull:", layout="wide")




chart_data={"gene":["gene1","gene2","gene3"],"mutationrate":[0.009,0.003,0.006]
chart_data = pd.DataFrame(chart_data)
chart_data=chart_data.set_index("name")
source = pd.DataFrame({
    'Gene': ['gene1','gene2','gene3'],
    'Mutationrate': [0.009,0.003,0.006]
})
bar_chart=alt.Chart(source).mark_bar().encode(
    x='Gene',
    y='Mutationrate',
)



        (st.write('Link: Asian50.org'))

    if option == 'BRCA' and option2 == 'Asian' and color == '49':
        st.bar_chart(chart_data)
        st.altair_chart(bar_chart,use_container_width=True)

