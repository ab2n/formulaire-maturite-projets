import streamlit as st

st.set_page_config(page_title="Checklist de préparation", layout="centered")
st.title("📋 Checklist Interactive - Maturité de votre projet")

questions = [
    "Je sais précisément pourquoi je veux lancer cette campagne et quel montant je souhaite atteindre",
    "J’ai une présentation claire, inspirante et convaincante de mon projet, avec une histoire qui donne envie de contribuer",
    "Je connais mon “1er cercle” (amis, famille, partenaires proches) et je sais comment le solliciter dès le lancement",
    "J’ai les ressources humaines et techniques pour mener à bien ma campagne",
    "J’ai déjà prévu un calendrier et des supports de communication (posts réseaux sociaux, mails, visuels, vidéo)",
    "Je sais quelles plateformes correspondent le mieux à mon projet et à mon public cible",
    "J’ai identifié des contreparties attractives, cohérentes avec mon projet et adaptées à mon public",
    "Je sais comment remercier, fidéliser et tenir informés mes contributeurs une fois la campagne terminée",
    "Mon projet a le potentiel pour embarquer les citoyens"
]

st.write("## Évaluez chaque point selon votre préparation")

responses = []
for q in questions:
    response = st.slider(q, min_value=0, max_value=1, value=0, step=1, format="%d")
    responses.append(response)

# Calcul du score et typologie
score = sum(responses)
typologie_mapping = {
    (0, 1): "Débutant",
    (2, 3): "Émergent",
    (4, 5): "En progression",
    (6, 7): "Bien préparé",
    (8, 9): "Prêt à lancer"
}

for key_range, label in typologie_mapping.items():
    if score in range(key_range[0], key_range[1]+1):
        maturity = label

st.write("---")
st.subheader("🚀 Votre typologie de maturité")
st.info(f"Votre projet est : **{maturity}**")

# Optionnel : visualisation graphique
st.bar_chart(responses)
