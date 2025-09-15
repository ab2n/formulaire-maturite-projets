import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Checklist Interactive", layout="centered")
st.title("📋 Checklist Interactive - Maturité de votre projet")

questions = [
    "Objectif et montant clair",
    "Présentation inspirante",
    "Connaissance du 1er cercle",
    "Ressources disponibles",
    "Calendrier et supports prêts",
    "Plateformes adaptées",
    "Contreparties attractives",
    "Suivi des contributeurs",
    "Potentiel citoyen"
]

st.write("## Évaluez chaque point selon votre préparation (0 = pas du tout, 5 = parfaitement)")

responses = []
for q in questions:
    response = st.slider(q, min_value=0, max_value=5, value=0, step=1)
    responses.append(response)

# Calcul du score moyen pour la typologie
average_score = sum(responses) / len(questions)

if average_score <= 1:
    maturity = "Débutant"
elif average_score <= 2:
    maturity = "Émergent"
elif average_score <= 3:
    maturity = "En progression"
elif average_score <= 4:
    maturity = "Bien préparé"
else:
    maturity = "Prêt à lancer"

st.write("---")
st.subheader("🚀 Votre typologie de maturité")
st.info(f"Votre projet est : **{maturity}** (score moyen : {average_score:.1f}/5)")

# Diagramme radar
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=responses + [responses[0]],  # pour boucler le radar
    theta=questions + [questions[0]],
    fill='toself',
    name='Maturité'
))

fig.update_layout(
    polar=dict(
        radialaxis=dict(
            visible=True,
            range=[0,5]
        )),
    showlegend=False
)

st.plotly_chart(fig, use_container_width=True)
