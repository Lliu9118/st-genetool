import requests
import streamlit as st
import array as ary
import pandas as pd
import altair as alt


st.set_page_config(page_title="My Webpage", page_icon=":skull:", layout="wide")
a = ary.array('i',[5])








data = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",
"AC010203.1",
"MIR487B",
"MIR7-2",],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
1,
                    0.5,
0.5,
0.5,
0.5,
0.5,
0.5,],
})


data2 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",
"AC010203.1",
"MIR487B",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
1,
                    0.5,
0.5,
0.5,
0.5,
0.5,
],
})

data3 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",
"AC010203.1",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
1,
                    0.5,
0.5,
0.5,
0.5,
],
})

data4 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
1,
                    0.5,
0.5,
0.5,
],
})

data5 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
1,
                    0.5,
0.5,
],
})

data6 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
"MIR329-1",
"MIR1302-3",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
1,
                    0.5,
],
})

data7 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
"MIR329-1",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
1,
],
})

data8 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
"MIR1275",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
1,
],
})

data9 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
"MIR7-2",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
3058104,
],
})

data10 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
"MIR520E",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
22727273,
],
})


data11 = pd.DataFrame({
    'Gene': ["AC011467.1",
             "MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",
"MIR1323",
"AC100757.1",
"MIR512-1",
"MIR515-2",
"AC010203.1",
"MIR9-3",
"AC005631.1",
"AC126323.1",
],
    'pvalue': [272727273,
250000000,
181818182,
159090909,
113636364,
113636364,
113636364,
90909091,
90909091,
68181818,
68181818,
68181818,
45454545,
45454545,
22727273,
22727273,
],
})
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
        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25'])
    st.write('You have selected', color, 'gene(s).')
    if option == 'BRCA' and option2 == 'Asian' and color == '1':
        (st.write('Link: https://docs.google.com/spreadsheets/d/1EWuYDcKM-jnjLPNm_dOJl33j4BHVE8CPD_LD47kS0dY/edit#gid=0'))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '25':
        st.write(data11)
        st.write(alt.Chart(data11).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '25':
        st.write(data10)
        st.write(alt.Chart(data10).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))

    
    if option == 'BRCA' and option2 == 'Asian' and color == '17':
        st.write(data9)
        st.write(alt.Chart(data9).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '18':
        st.write(data8)
        st.write(alt.Chart(data8).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
        
    if option == 'BRCA' and option2 == 'Asian' and color == '19':
        st.write(data7)
        st.write(alt.Chart(data7).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
        
    if option == 'BRCA' and option2 == 'Asian' and color == '20':
        st.write(data6)
        st.write(alt.Chart(data6).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
 
    if option == 'BRCA' and option2 == 'Asian' and color == '21':
        st.write(data5)
        st.write(alt.Chart(data5).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '22':
        st.write(data4)
        st.write(alt.Chart(data4).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))

    if option == 'BRCA' and option2 == 'Asian' and color == '23':
        st.write(data3)
        st.write(alt.Chart(data3).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '24':
        st.write(data2)
        st.write(alt.Chart(data2).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))

    if option == 'BRCA' and option2 == 'Asian' and color == '25':
        st.write(data)
        st.write(alt.Chart(data).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',
        ))
