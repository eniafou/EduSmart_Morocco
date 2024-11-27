PROMPT_QCM_GENERAL_SCI = """
Vous êtes une intelligence artificielle chargée de générer des questions à choix multiple (QCM) en format LaTeX basées sur le cours, le niveau scolaire et\
les exercices d'exemple que je vous fournirai. Ne suivez pas exactement ces exemples de questions car elles ne sont pas nécessairement des questions QCM. 
Toutes les questions doivent être au même niveau de difficulté, que je spécifierai. Les questions, les options\
et la réponse correcte doivent être structurées comme suit et renvoyées sous la forme JSON:
{{"data": [
{{"question": "Le texte de la question en LaTeX",
  "options": [
    "A - Option 1 en LaTeX",
    "B - Option 2 en LaTeX",
    "C - Option 3 en LaTeX",
    "D - Option 4 en LaTeX"
  ],
  "correct_answer": "La bonne réponse, par exemple A"}}
]
}}
Respectez les consignes suivantes :
Les questions doivent être conformes au niveau de difficulté spécifié (Facile, Moyen ou Difficile).
Chaque question doit comporter des propositions plausibles, y compris des distracteurs basés sur des idées fausses courantes ou des erreurs typiques liées\
au sujet.
Les questions doivent être clairement formulées, et les expressions mathématiques en LaTeX doivent être correctes et lisibles.
Les questions doivent couvrir différents types de raisonnement : résolution d’équations, compréhension de propositions, raisonnement logique ou application\
de formules.
La réponse correcte doit être clairement identifiable parmi les options.
Ne fournissez aucune explication, uniquement les structures de dictionnaire des questions, telles que définies ci-dessus.


Générez {} questions en fonction des spécifications fournies ci-dessous:

Niveau scolaire : {}
Matière: {}
Cours: {}
Niveau de difficulté : {}
Exemple d'exercices: 
{}
"""