import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# URL do dataset
url = "C:/Users/Paulo/Documents/FIAP/4_etapa/ex_1/Atividade_Cap10_produtos_agricolas.csv"

# Lendo o CSV
dados_cultura = pd.read_csv(url)

# Função para definir a recomendação de irrigação/monitoramento/drenagem
def definir_acao(row):
    if row['temperature'] >= 30 and row['rainfall'] <= 100:
        return 'irrigação'
    elif row['temperature'] >= 30 and row['rainfall'] <= 150:
        return 'monitoramento'
    elif row['rainfall'] >= 200:
        return 'drenagem'
    else:
        return 'monitoramento'

# Criando a nova coluna
dados_cultura['acao'] = dados_cultura.apply(definir_acao, axis=1)


# ------------------- PREPARAÇÃO -------------------

# Selecionar variáveis independentes
X = dados_cultura[['temperature', 'humidity', 'ph', 'rainfall']]

# Variáveis alvo
y_label = dados_cultura['label']
y_acao = dados_cultura['acao']

# Dividir em treino e teste para cada alvo
X_train, X_test, y_label_train, y_label_test = train_test_split(X, y_label, test_size=0.2, random_state=42)
_, _, y_acao_train, y_acao_test = train_test_split(X, y_acao, test_size=0.2, random_state=42)

# ------------------- TREINAR MODELOS -------------------

# Modelo para label
modelo_label = RandomForestClassifier(random_state=42)
modelo_label.fit(X_train, y_label_train)

# Modelo para ação
modelo_acao = RandomForestClassifier(random_state=42)
modelo_acao.fit(X_train, y_acao_train)

# Avaliar acurácia
y_label_pred = modelo_label.predict(X_test)
y_acao_pred = modelo_acao.predict(X_test)

acuracia_label = accuracy_score(y_label_test, y_label_pred)
acuracia_acao = accuracy_score(y_acao_test, y_acao_pred)

# ------------------- STREAMLIT -------------------

st.title("🌱 Predição de Cultura Agrícola e Ação de Manejo")
st.write(f"Acurácia do modelo Random Forest (Label): **{acuracia_label:.2%}**")
st.write(f"Acurácia do modelo Random Forest (Ação): **{acuracia_acao:.2%}**")

st.sidebar.header("Ajuste das variáveis de projeção")

# Sliders para entrada do usuário
temperature = st.sidebar.slider("Temperatura (°C)", float(X['temperature'].min()), float(X['temperature'].max()), 25.0)
humidity = st.sidebar.slider("Umidade (%)", float(X['humidity'].min()), float(X['humidity'].max()), 80.0)
ph = st.sidebar.slider("pH do solo", float(X['ph'].min()), float(X['ph'].max()), 6.5)
rainfall = st.sidebar.slider("Precipitação (mm)", float(X['rainfall'].min()), float(X['rainfall'].max()), 200.0)

# Criar DataFrame com valores do usuário
entrada_usuario = pd.DataFrame({
    'temperature': [temperature],
    'humidity': [humidity],
    'ph': [ph],
    'rainfall': [rainfall]
})

# Predições
cultura_predita = modelo_label.predict(entrada_usuario)
acao_predita = modelo_acao.predict(entrada_usuario)

st.subheader("🌾 Resultado da Predição")
st.write(f"Cultura ideal para as condições fornecidas: **{cultura_predita[0]}**")
st.write(f"Ação recomendada para manejo: **{acao_predita[0]}**")

# ------------------- GRÁFICOS -------------------

st.subheader("📊 Distribuição das Variáveis")
fig, axs = plt.subplots(2, 2, figsize=(10, 8))
sns.histplot(dados_cultura['temperature'], kde=True, ax=axs[0,0], color="orange")
axs[0,0].set_title("Distribuição da Temperatura")

sns.histplot(dados_cultura['humidity'], kde=True, ax=axs[0,1], color="blue")
axs[0,1].set_title("Distribuição da Umidade")

sns.histplot(dados_cultura['ph'], kde=True, ax=axs[1,0], color="green")
axs[1,0].set_title("Distribuição do pH")

sns.histplot(dados_cultura['rainfall'], kde=True, ax=axs[1,1], color="purple")
axs[1,1].set_title("Distribuição da Precipitação")

st.pyplot(fig)

# Importância das variáveis
st.subheader("🌟 Importância das Variáveis no Modelo (Label)")
importancias_label = pd.DataFrame({
    'Variável': X.columns,
    'Importância': modelo_label.feature_importances_
}).sort_values(by="Importância", ascending=False)
st.bar_chart(importancias_label.set_index("Variável"))

st.subheader("🌟 Importância das Variáveis no Modelo (Ação)")
importancias_acao = pd.DataFrame({
    'Variável': X.columns,
    'Importância': modelo_acao.feature_importances_
}).sort_values(by="Importância", ascending=False)
st.bar_chart(importancias_acao.set_index("Variável"))