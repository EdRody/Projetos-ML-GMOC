

import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression
import matplotlib as mp

#Atribui à variável "df" a leitura do arquivo CSV "pizzas.csv" por meio da biblioteca Pandas
df = pd.read_csv("pizzas.csv")

#Atribui à váriavel "mdl" a função de regressão linear da biblioteca do scikit-learn
mdl = LinearRegression()

#"Lê" o arquivo csv e atribui os valores da coluna "Diametro" à variável "x" e os da coluna "Preço" à variável "y",
x = df[["diametro"]]   
y = df[["preco"]]

#Realiza o treinamento do modelo de ML de regressão linear a partir das variáveis "x" e "y"
mdl.fit(x,y)

#Interface do programa por meio da biblioteca "Streamlit"
st.title("Calculadora de Preço de pizza")

st.divider()
    #Pede para o usuário inserir um valor para o diâmetro e atribui o valor inserido à variável "diametro"
diametro = st.number_input("Insira o diametro da pizza em centímetros:", value = 0, step = 1, format = "%d")

#Se a variável "diametro" não for Nula (=0), realiza a predição do preço da pizza 
# a partir do diametro inserido e escreve o valor na tela
if diametro:
    preco_previsto = mdl.predict([[diametro]])[0][0]
    st.write(f"Ficou R${preco_previsto:.2f}")
    st.balloons()