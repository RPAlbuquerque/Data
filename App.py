# -*- coding: utf-8 -*-
"""Untitled37.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1LerOr8V7-AAMadlAD5-CzuZzSseg7IZs
"""

import streamlit as st

# Configuração da página
st.set_page_config(page_title="Mark da Marketri - Quiz de Marketing", page_icon="📊", layout="centered")

# Cores da marca
COR_PRIMARIA = "#6A0DAD"  # Roxo
COR_SECUNDARIA = "#00BFFF"  # Azul celeste

# Estilo CSS corrigido
st.markdown(f"""
    <style>
        .stApp {{
            background-color: #f9f9f9;
            color: #000000;
        }}
        .title h1 {{
            color: {COR_PRIMARIA};
        }}
        .stButton > button {{
            background-color: {COR_SECUNDARIA};
            color: white;
            font-weight: bold;
        }}
        label, .css-1cpxqw2, .css-1d391kg, .css-17eq0hr, .css-81oif8, .css-1v0mbdj, .css-1xarl3l, .stRadio label, .css-qrbaxs, .css-qri22k {{
            color: #000000 !important;
        }}
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("<h1 style='text-align: center;'>🐵 Mark da Marketri</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>Descubra o nível de Marketing Estratégico da sua empresa</h3>", unsafe_allow_html=True)
st.markdown("---")

pontuacao = 0

# Perguntas
perguntas = [
    {
        "pergunta": "1️⃣ Você tem um plano de Marketing claro para os próximos meses?",
        "alternativas": [
            ("a) Não tenho planejamento, faço postagens e campanhas aleatórias", 1),
            ("b) Tenho algumas ideias, mas sem plano estruturado", 2),
            ("c) Sim, tenho um planejamento bem definido com metas claras", 3)
        ]
    },
    {
        "pergunta": "2️⃣ Você acompanha e analisa os resultados e dados de sua campanha?",
        "alternativas": [
            ("a) Não, só vejo curtidas e seguidores", 1),
            ("b) Analiso algumas métricas, mas sem muita frequência", 2),
            ("c) Uso dados para tomar decisões estratégicas e otimizar minhas campanhas", 3)
        ]
    },
    {
        "pergunta": "3️⃣ Seu marketing está alinhado com suas metas de vendas?",
        "alternativas": [
            ("a) Não, marketing e vendas são coisas separadas pra mim", 1),
            ("b) Tenho algumas ações voltadas pra vendas, mas sem funil bem definido", 2),
            ("c) Sim, marketing e vendas andam juntos na minha empresa", 3)
        ]
    },
    {
        "pergunta": "4️⃣ Sua marca tem uma identidade visual forte e reconhecível?",
        "alternativas": [
            ("a) Não tenho um padrão visual bem definido", 1),
            ("b) Uso uma identidade visual, mas sem consistência em todos os canais", 2),
            ("c) Sim, minha identidade visual é bem estruturada e reforça meu posicionamento", 3)
        ]
    },
    {
        "pergunta": "5️⃣ Você trabalha com Marketing Virtual e Offline de forma integrada?",
        "alternativas": [
            ("a) Uso só marketing digital ou offline, não tem integração", 1),
            ("b) Tenho algumas ações integradas, mas ainda sem um plano estruturado", 2),
            ("c) Sim, minhas estratégias online e offline são alinhadas para potencializar os resultados", 3)
        ]
    },
]

for i, q in enumerate(perguntas):
    alternativas = [alt[0] for alt in q["alternativas"]]
    escolha = st.radio(q["pergunta"], alternativas, index=None, key=i)
    if escolha:
        pontos = dict(q["alternativas"])[escolha]
        pontuacao += pontos

# Resultado
if st.button("📊 Ver meu nível de marketing"):
    st.markdown("---")
    if pontuacao <= 10:
        st.error("🔻 **Nível: Iniciante**\n\nSeu marketing ainda não tem uma estratégia clara. É hora de estruturar melhor suas ações para colher bons resultados.")
    elif pontuacao <= 20:
        st.warning("🟡 **Nível: Intermediário**\n\nVocê já aplica algumas estratégias, mas ainda pode otimizar muito os resultados.")
    else:
        st.success("🔝 **Nível: Avançado**\n\nParabéns! Seu nível de marketing estratégico está alinhado com o crescimento do seu negócio.")