import streamlit as st

u18biljett = 130
vbiljett = 230
pbiljett = 100
saldo = 0
enkel = 1
retur = 2 * 0.8
express = 1.2

st.title("SJ biljett")
st.header("Välkommen!")
st.subheader("vänligen ange ditt saldo")
updsaldo = st.number_input('Välj belopp här')
saldo = saldo + updsaldo
st.write(f'Ditt nya saldo är {saldo}kr')

st.header('Vilken Biljett typ vill du ha? enkel, retur, express')
biljettyp =st.text_input('Vänligen ange biljett typ.')

st.header('Ange din ålder')
age = st.slider('Ange här', min_value=None, max_value=120, value=None, step=1)

if age < 18 and biljettyp == 'enkel':
    saldo = saldo - u18biljett * enkel
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif age < 18 and biljettyp == 'express':
    saldo = saldo - u18biljett * express
elif age < 18 and biljettyp == 'retur':
    saldo = saldo - u18biljett * retur
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 18 <= age <= 64 and biljettyp == 'enkel':
    saldo = saldo - vbiljett * enkel
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 18 <= age <= 64 and biljettyp == 'express':
    saldo = saldo - vbiljett * express
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 18 <= age <= 64 and biljettyp == 'retur':
    saldo = saldo - vbiljett * retur
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 120 and biljettyp == 'enkel':
    saldo = saldo - pbiljett * enkel
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 120 and biljettyp == 'express':
    saldo = saldo - pbiljett * express
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
elif 64 < age <= 120 and biljettyp == 'retur':
    saldo = saldo - pbiljett * retur
    st.write(f'Du angav åldern {age}. Ditt nya saldo är {saldo}kr')
    st.subheader('Ha en trevlig resa!')
