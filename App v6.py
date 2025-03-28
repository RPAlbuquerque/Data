import streamlit as st
from PIL import Image

# Configuração da página
st.set_page_config(page_title="Mark da Marketri - Quiz de Marketing", page_icon="📊", layout="wide")

# Cores
COR_ROXO = "#8c52ff"
COR_AZUL = "#5ce1e6"

# CSS com fundo degradê e botões estilizados
st.markdown(f"""
    <style>
        html, body, .stApp {{
            background: linear-gradient(135deg, {COR_ROXO}, {COR_AZUL}) fixed !important;
            color: black !important;
        }}
        .stButton > button {{
            background-color: {COR_AZUL};
            color: black;
            font-weight: bold;
            border-radius: 6px;
            padding: 0.5em 1em;
        }}
        .stRadio > div {{
            padding: 10px 0;
        }}
    </style>
""", unsafe_allow_html=True)

# Colunas para layout com Mark na esquerda
g_col, q_col = st.columns([1, 2])

with g_col:
    st.image("https://raw.githubusercontent.com/RPAlbuquerque/Data/main/Mark_fundo_transparente.png", width=250)

with q_col:
    st.markdown("""
        <h3 style='color: white;'>👍 Oi! Eu sou o <strong>Mark</strong>, da <strong>Marketri</strong>.</h3>
        <p style='color: white; font-size: 18px;'>Vou te ajudar a descobrir qual é o <strong>nível de Marketing Estratégico</strong> da sua empresa.<br>
        É rapidinho! Responda as próximas perguntas e no final te conto o resultado. Vamos nessa? 🚀</p>
    """, unsafe_allow_html=True)

# Perguntas e alternativas
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

# Estado do quiz
if "indice" not in st.session_state:
    st.session_state.indice = 0
    st.session_state.pontuacao = 0
    st.session_state.concluido = False
    st.session_state.respostas = [None] * len(perguntas)

indice = st.session_state.indice

if not st.session_state.concluido and indice < len(perguntas):
    pergunta_atual = perguntas[indice]
    st.markdown("---")

    with st.form(key=f"form_{indice}"):
        st.subheader(f"{indice+1}. {pergunta_atual['pergunta']}")
        opcoes = [a[0] for a in pergunta_atual["alternativas"]]
        escolha = st.radio("Escolha uma opção:", opcoes, key=f"q_{indice}")
        submitted = st.form_submit_button("Próxima pergunta")

        if submitted and escolha:
            valor = dict(pergunta_atual["alternativas"])[escolha]
            if st.session_state.respostas[indice] is None:
                st.session_state.pontuacao += valor
                st.session_state.respostas[indice] = escolha
            elif st.session_state.respostas[indice] != escolha:
                valor_antigo = dict(pergunta_atual["alternativas"])[st.session_state.respostas[indice]]
                st.session_state.pontuacao -= valor_antigo
                st.session_state.pontuacao += valor
                st.session_state.respostas[indice] = escolha
            st.session_state.indice += 1
            if st.session_state.indice == len(perguntas):
                st.session_state.concluido = True

# Resultado final
if st.session_state.concluido:
    score = st.session_state.pontuacao
    st.markdown("---")
    st.subheader("Resultado Final 🎯")

    if score <= 10:
        st.error("🔻 **Nível: Iniciante**\n\nSeu marketing ainda não tem uma estratégia clara. É hora de estruturar melhor suas ações para colher bons resultados.")
    elif score <= 20:
        st.warning("🟡 **Nível: Intermediário**\n\nVocê já aplica algumas estratégias, mas ainda pode otimizar muito os resultados.")
    else:
        st.success("🔝 **Nível: Avançado**\n\nParabéns! Seu nível de marketing estratégico está alinhado com o crescimento do seu negócio.")

    st.markdown("---")
    st.markdown("""
        <div style='text-align: center;'>
            <h4 style='color: white;'>📲 Quer melhorar o marketing da sua empresa?<br>
            Fale com a equipe da <strong>Marketri</strong> e descubra como podemos te ajudar de forma estratégica!</h4>
            <a href='https://wa.me/message/OIPGWY5OX4AEJ1' target='_blank'>
                <button style='background-color:#5ce1e6; color:black; font-weight:bold; padding:10px 20px; border:none; border-radius:5px; font-size:16px;'>Falar com a Marketri no WhatsApp</button>
            </a>
        </div>
    """, unsafe_allow_html=True)
