import streamlit as st

st.title("Meu primeiro app no iPhone 📱")
st.write("Rodando Streamlit direto do celular 🚀")

nome = st.text_input("Digite seu nome:")

if nome:
    st.success(f"Olá, {nome}!")
