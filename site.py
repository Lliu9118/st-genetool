import requests
import streamlit as st
import array as ary
import pandas as pd




st.set_page_config(page_title="My Webpage", page_icon=":skull:", layout="wide")


a = ary.array('i',[5])








with st.container():
    st.title("The Gene Mutation Interactive Tool")
    #st.subheader("Helping to go further in studies on race and cancer")
with st.container():
    #st.download_button(
        #label="Download data as CSV",
    #data=csv,
    #file_name='miRNA_outputs.csv',
    #mime='text/csv',
         #)
    with st.container():
        st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Our Goal")
        st.write("##")
        st.write("In past research on the correlation between race and the frequency of cancer within those races, researchers lacked an efficient and simple way to gain access to the most prevalent cancerous genes by race. Our interactive tool strives to assist the further research on the topic of cancer and race. With a few clicks, researchers of the future will be able to easily gain access to the most prevalent genes within affected patients.")
  
    option = st.selectbox(
        'Which cancer type would ypu like to view?',
        ('BRCA', 'LUAD',))

    st.write('You selected:', option)

    option2 = st.selectbox(
        'Which race would you like to view?',
        ('Asian', 'White',))
    st.write('You selected:', option2)

    color = st.select_slider(
        'Select the amount of genes you would like to view.',
        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50'])
    st.write('You have selected', color, 'gene(s).')



    if option == 'BRCA' and option2 == 'Asian' and color == '1':
        (st.write('Link: https://docs.google.com/spreadsheets/d/1EWuYDcKM-jnjLPNm_dOJl33j4BHVE8CPD_LD47kS0dY/edit#gid=0'))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '50':
        (st.write('Link: Asian50.org'))
 
    if option == 'BRCA' and option2 == 'Asian' and color == '8':
        st.image("6genes.jpg")


