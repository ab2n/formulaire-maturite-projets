import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="Checklist Interactive", layout="centered")
st.title("📋 Checklist Interactive - Maturité de votre projet")

# Questions originales pour les sliders
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

# Labels courts pour le radar chart
short_labels = [
    "Objectif",
    "Présentation",
    "1er cercle",
    "Ressources",
    "Calendrier",
    "Plateformes",
    "Contreparties",
    "Suivi",
    "Impact"
]

st.write("## Évaluez chaque point selon votre préparation (0 = pas du tout, 5 = parfaitement)")

responses = []
for q in questions:
    response = st.slider(q, min_value=0, max_value=5, value=0, step=1)
    responses.append(response)

# Calcul du score moyen et typologie
average_score = sum(responses) / len(questions)

if average_score <= 1:
    maturity = "Débutant"
    comment = "Votre projet est encore au stade initial. Il est recommandé de clarifier vos objectifs et de renforcer vos fondamentaux avant de lancer une campagne."
    resources = [
        ("Guide pour débutants", "https://example.com/debutant-guide"),
        ("Checklist de préparation", "https://example.com/debutant-checklist")
    ]
elif average_score <= 2:
    maturity = "Émergent"
    comment = "Votre projet commence à prendre forme mais plusieurs aspects restent à consolider. Travaillez sur votre présentation et votre réseau de contacts."
    resources = [
        ("Atelier planification", "https://example.com/emergent-atelier"),
        ("Modèles de campagne", "https://example.com/emergent-modeles")
    ]
elif average_score <= 3:
    maturity = "En progression"
    comment = "Votre projet est en bonne voie. Il vous reste à finaliser certains éléments pour être totalement prêt à lancer."
    resources = [
        ("Optimisation de campagne", "https://example.com/progression-optimisation"),
        ("Exemples de succès", "https://example.com/progression-exemples")
    ]
elif average_score <= 4:
    maturity = "Bien préparé"
    comment = "Votre projet est bien structuré et prêt pour le lancement. Quelques ajustements mineurs pourraient le rendre encore plus solide."
    resources = [
        ("Stratégies avancées", "https://example.com/bienprepare-strategies"),
        ("Checklist finale", "https://example.com/bienprepare-checklist")
    ]
else:
    maturity = "Prêt à lancer"
    comment = "Félicitations ! Votre projet est prêt à être lancé. Pensez à suivre vos contributeurs et à maintenir la communication après la campagne."
    resources = [
        ("Lancement et suivi", "https://example.com/pret-lancer-lancement"),
        ("Outils de fidélisation", "https://example.com/pret-lancer-outils")
    ]

st.write("---")
st.subheader("🚀 Votre typologie de maturité")
st.info(f"**{maturity}** (score moyen : {average_score:.1f}/5)")
st.write(comment)

# Affichage des ressources
st.write("### 📚 Ressources recommandées pour vous")
for title, url in resources:
    st.markdown(f"- [{title}]({url})")

# Définir la couleur de chaque axe selon le score
colors = []
for val in responses:
    if val <= 1:
        colors.append("red")
    elif val <= 3:
        colors.append("yellow")
    else:
        colors.append("green")

# Boucler pour fermer le radar
responses_loop = responses + [responses[0]]
short_labels_loop = short_labels + [short_labels[0]]
colors_loop = colors + [colors[0]]

# Création du radar chart avec couleur dynamique
fig = go.Figure()
for i in range(len(responses)):
    fig.add_trace(go.Scatterpolar(
        r=[0, responses[i]],
        theta=[short_labels[i], short_labels[i]],
        mode='lines+markers',
        line=dict(color=colors[i], width=3),
        marker=dict(size=8, color=colors[i]),
        showlegend=False
    ))

# Ajouter la zone remplie
fig.add_trace(go.Scatterpolar(
    r=responses_loop,
    theta=short_labels_loop,
    fill='toself',
    fillcolor='rgba(0,128,255,0.2)',
    line_color='blue',
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
