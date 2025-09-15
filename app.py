import streamlit as st

st.set_page_config(page_title="Checklist Interactive", layout="centered")
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

st.write("## Évaluez chaque point selon votre préparation (0 = pas du tout, 5 = parfaitement)")

responses = []
for q in questions:
    response = st.slider(q, min_value=0, max_value=5, value=0, step=1)
    responses.append(response)

# Calcul du score total et typologie
total_score = sum(responses)
max_score = len(questions) * 5
average_score = total_score / len(questions)  # moyenne par question

# Définition des typologies
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

# Visualisation simple
st.bar_chart(responses)
