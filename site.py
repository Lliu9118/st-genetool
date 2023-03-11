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
"MIR7-2",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,
0.068181818,
0.045454545,
0.045454545,
0.022727273,
0.022727273,
0.022727273,
0.003058104,],
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
"MIR520E",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,
0.068181818,
0.045454545,
0.045454545,
0.022727273,
0.022727273,
0.022727273,],
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
"AC126323.1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,
0.068181818,
0.045454545,
0.045454545,
0.022727273,
0.022727273,],
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
"AC005631.1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,
0.068181818,
0.045454545,
0.045454545,
0.022727273,],
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
"MIR9-3",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,
0.068181818,
0.045454545,
0.045454545,],
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
"AC010203.1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,
0.068181818,
0.045454545,],
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
"MIR515-2",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,
0.068181818,],
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
"MIR512-1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,
0.068181818,],
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
"AC100757.1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,
0.068181818,],
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
"MIR1323",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,
0.090909091,],
})

data11 = pd.DataFrame({
    'Gene': ["AC011467.1",
"MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",
"AC091565.1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,
0.090909091,],
})

data12 = pd.DataFrame({
    'Gene': ["AC011467.1",
"MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",
"MIR520A",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,
0.113636364,],
})

data13 = pd.DataFrame({
    'Gene': ["AC011467.1",
"MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",
"MIR515-1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,
0.113636364,],
})

data14 = pd.DataFrame({
    'Gene': ["AC011467.1",
"MIR526B",
"AC090825.1",
"MIR519C",
"AC105339.2",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,
0.113636364,],
})

data15 = pd.DataFrame({
    'Gene': ["AC011467.1",
"MIR526B",
"AC090825.1",
"MIR519C",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,
0.159090909,],
})

data16 = pd.DataFrame({
    'Gene': ["AC011467.1",
"MIR526B",
"AC090825.1",]
  ,
    'Asian_p': [0.272727273,
0.25,
0.181818182,],
})

data17 = pd.DataFrame({
    'Gene': ["AC011467.1",
"MIR526B",]
  ,
    'Asian_p': [0.272727273,
0.25,],
})

data18 = pd.DataFrame({
    'Gene': ["AC011467.1",]
  ,
    'Asian_p': [0.272727273,],
})

data19 = pd.DataFrame({
    'Gene': ["MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",
"AC010203.1",
"MIR487B",
"MIR7-2",]
  ,
    'Asian_p': [1,
1,
0.5,
0.5,
0.5,
0.5,
0.5,
0.5,],
})

data20 = pd.DataFrame({
    'Gene': ["MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",
"AC010203.1",
"MIR487B",]
  ,
    'Asian_p': [1,
1,
0.5,
0.5,
0.5,
0.5,
0.5,],
})

data21 = pd.DataFrame({
    'Gene': ["MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",
"AC010203.1",]
  ,
    'Asian_p': [1,
1,
0.5,
0.5,
0.5,
0.5,],
})

data22 = pd.DataFrame({
    'Gene': ["MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",
"MIR30D",]
  ,
    'Asian_p': [1,
1,
0.5,
0.5,
0.5,],
})

data23 = pd.DataFrame({
    'Gene': ["MIR1275",
"MIR329-1",
"MIR1302-3",
"AC005631.1",]
  ,
    'Asian_p': [1,
1,
0.5,
0.5,],
})

data24 = pd.DataFrame({
    'Gene': ["MIR1275",
"MIR329-1",
"MIR1302-3",]
  ,
    'Asian_p': [1,
1,
0.5,],
})

data25 = pd.DataFrame({
    'Gene': ["MIR1275",
"MIR329-1",]
  ,
    'Asian_p': [1,
1,],
})

data26 = pd.DataFrame({
    'Gene': ["MIR1275",]
  ,
    'Asian_p': [1,],
})

data27 = pd.DataFrame({
    'Gene': []
  ,
    'Asian_p': [],
})

dataw1 = pd.DataFrame({
     'Gene': [	
"AC080008.1",
"MIR7-2",
"AC005631.1",
"AL161651.1",
"MIR520E",
"MIR124-2",
"AL391261.1",
"	MIR526B	",

		], 'White_p': [
	0.141025641	,
	0.08974359	,
	0.064102564	,
	0.051282051	,
	0.038461538	,
	0.025641025	,
	0.025641025	,
	0.025641025	,
	
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
        options=['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18'])
    
    st.write('You have selected', color, 'gene(s).')

    if option == 'LUAD' and option2 == 'Asian' and color == '0':
        st.write(data27)
        st.write(alt.Chart(data27).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '1':
        st.write(data26)
        st.write(alt.Chart(data26).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '2':
        st.write(data25)
        st.write(alt.Chart(data25).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '3':
        st.write(data24)
        st.write(alt.Chart(data24).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '4':
        st.write(data23)
        st.write(alt.Chart(data23).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '5':
        st.write(data22)
        st.write(alt.Chart(data22).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '6':
        st.write(data21)
        st.write(alt.Chart(data21).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '7':
        st.write(data20)
        st.write(alt.Chart(data20).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'LUAD' and option2 == 'Asian' and color == '8':
        st.write(data19)
        st.write(alt.Chart(data19).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'BRCA' and option2 == 'Asian' and color == '1':
        st.write(data18)
        st.write(alt.Chart(data18).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'BRCA' and option2 == 'Asian' and color == '2':
        st.write(data17)
        st.write(alt.Chart(data17).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'BRCA' and option2 == 'Asian' and color == '3':
        st.write(data16)
        st.write(alt.Chart(data16).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))

    if option == 'BRCA' and option2 == 'Asian' and color == '4':
        st.write(data15)
        st.write(alt.Chart(data15).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '5':
        st.write(data14)
        st.write(alt.Chart(data14).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '6':
        st.write(data13)
        st.write(alt.Chart(data13).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '7':
        st.write(data12)
        st.write(alt.Chart(data12).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '8':
        st.write(data11)
        st.write(alt.Chart(data11).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '9':
        st.write(data10)
        st.write(alt.Chart(data10).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))

    
    if option == 'BRCA' and option2 == 'Asian' and color == '10':
        st.write(data9)
        st.write(alt.Chart(data9).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '11':
        st.write(data8)
        st.write(alt.Chart(data8).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'BRCA' and option2 == 'Asian' and color == '12':
        st.write(data7)
        st.write(alt.Chart(data7).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
        
    if option == 'BRCA' and option2 == 'Asian' and color == '13':
        st.write(data6)
        st.write(alt.Chart(data6).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
 
    if option == 'BRCA' and option2 == 'Asian' and color == '14':
        st.write(data5)
        st.write(alt.Chart(data5).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '15':
        st.write(data4)
        st.write(alt.Chart(data4).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))

    if option == 'BRCA' and option2 == 'Asian' and color == '16':
        st.write(data3)
        st.write(alt.Chart(data3).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    
    if option == 'BRCA' and option2 == 'Asian' and color == '17':
        st.write(data2)
        st.write(alt.Chart(data2).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))

    if option == 'BRCA' and option2 == 'Asian' and color == '18':
        st.write(data)
        st.write(alt.Chart(data).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='Asian_p',
        ))
    if option == 'BRCA' and option2 == 'White' and color == '18':
  
        st.write(alt.Chart(dataw1).mark_bar().encode(
            x=alt.X('Gene', sort=None),
            y='pvalue',

        )
)
        st.write(dataw1)
