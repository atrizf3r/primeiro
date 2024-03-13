import streamlit as st

st.write("Meu primeiro programa de web")
st.text('Nome')
nome = st.text_input('Digite seu nome')
st.write('Olá', nome)


def inverte_texto(texto):
    return texto[::-1]


#botão para inverter o texto
if st.button("Inverter"):
#outra manerira de escrever 
# tem como colocar b1 = st.button("Inverter")
#st.write(b1)
#if b1:
#texto_invertido = inverte_texto(nome) st.write(f"Texto Invertido: {texto_invertido}")
   texto_invertido = inverte_texto(nome)
   st.write(f"Texto Invertido: {texto_invertido}")

