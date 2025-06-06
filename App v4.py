# -*- coding: utf-8 -*-
"""Untitled41.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1wmhuHI07MmnRT53O3Yg39OIZK_OvAS12
"""

import streamlit as st

# Configuração da página
st.set_page_config(page_title="Mark da Marketri - Quiz de Marketing", page_icon="📊", layout="centered")

# Cores
COR_ROXO = "#8c52ff"
COR_AZUL = "#5ce1e6"

# Estilo global com fundo em degradê e textos em preto
st.markdown(f"""
    <style>
        body {{
            background: linear-gradient(135deg, {COR_ROXO}, {COR_AZUL}) !important;
            background-attachment: fixed;
            color: black !important;
        }}
        .stApp {{
            background-color: transparent !important;
        }}
        .stButton > button {{
            background-color: {COR_AZUL};
            color: white;
            font-weight: bold;
            border-radius: 6px;
            padding: 0.5em 1em;
        }}
        .stRadio > div {{
            padding: 10px 0;
        }}
    </style>
""", unsafe_allow_html=True)

# Logo da Marketri centralizada
st.markdown("""
    <div style='text-align: center; padding-top: 10px;'>
        <img src='https://raw.githubusercontent.com/RPAlbuquerque/Data/main/Logo%20Marketri.png' width='200'>
    </div>
""", unsafe_allow_html=True)

# Mark da Marketri e chamada
st.markdown("""
    <div style='text-align: center; margin-top: 20px;'>
        <img src='https://raw.githubusercontent.com/RPAlbuquerque/Data/main/Mark.png' width='120'>
        <h2 style='color: white; margin-top: 10px;'>Vamos avaliar o nível de Marketing Estratégico da sua empresa?</h2>
    </div>
""", unsafe_allow_html=True)

# Perguntas e respostas
perguntas = [
    {
        "pergunta": "Você tem um plano de Marketing claro para os próximos meses?",
        "alternativas": [
            ("Não tenho planejamento, faço postagens e campanhas aleatórias", 1),
            ("Tenho algumas ideias, mas sem plano estruturado", 2),
            ("Sim, tenho um planejamento bem definido com metas claras", 3)
        ]
    },
    {
        "pergunta": "Você acompanha e analisa os resultados e dados de sua campanha?",
        "alternativas": [
            ("Não, só vejo curtidas e seguidores", 1),
            ("Analiso algumas métricas, mas sem muita frequência", 2),
            ("Uso dados para tomar decisões estratégicas e otimizar minhas campanhas", 3)
        ]
    },
    {
        "pergunta": "Seu marketing está alinhado com suas metas de vendas?",
        "alternativas": [
            ("Não, marketing e vendas são coisas separadas pra mim", 1),
            ("Tenho algumas ações voltadas pra vendas, mas sem funil bem definido", 2),
            ("Sim, marketing e vendas andam juntos na minha empresa", 3)
        ]
    },
    {
        "pergunta": "Sua marca tem uma identidade visual forte e reconhecível?",
        "alternativas": [
            ("Não tenho um padrão visual bem definido", 1),
            ("Uso uma identidade visual, mas sem consistência em todos os canais", 2),
            ("Sim, minha identidade visual é bem estruturada e reforça meu posicionamento", 3)
        ]
    },
    {
        "pergunta": "Você trabalha com Marketing Virtual e Offline de forma integrada?",
        "alternativas": [
            ("Uso só marketing digital ou offline, não tem integração", 1),
            ("Tenho algumas ações integradas, mas ainda sem um plano estruturado", 2),
            ("Sim, minhas estratégias online e offline são alinhadas para potencializar os resultados", 3)
        ]
    },
]

# Controle do estado do quiz
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.pontuacao = 0

indice = st.session_state.indice

if indice < len(perguntas):
    q = perguntas[indice]
    st.subheader(f"{indice+1}. {q['pergunta']}")
    opcoes = [alt[0] for alt in q['alternativas']]
    escolha = st.radio("Escolha uma opção:", opcoes, key=f"q_{indice}")

    if st.button("Próxima"):
        if escolha:
            valor = dict(q['alternativas'])[escolha]
            st.session_state.pontuacao += valor
            st.session_state.indice += 1
            st.experimental_rerun()
        else:
            st.warning("Por favor, selecione uma opção.")
else:
    # Resultado final
    score = st.session_state.pontuacao
    st.markdown("---")
    st.subheader("Resultado Final 🎯")

    if score <= 10:
        st.error("🔻 **Nível: Iniciante**\n\nSeu marketing ainda não tem uma estratégia clara. É hora de estruturar melhor suas ações para colher bons resultados.")
    elif score <= 20:
        st.warning("🟡 **Nível: Intermediário**\n\nVocê já aplica algumas estratégias, mas ainda pode otimizar muito os resultados.")
    else:
        st.success("🔝 **Nível: Avançado**\n\nParabéns! Seu nível de marketing estratégico está alinhado com o crescimento do seu negócio.")

    if st.button("🔁 Refazer quiz"):
        st.session_state.indice = 0
        st.session_state.pontuacao = 0
        st.experimental_rerun()