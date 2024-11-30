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
PROMPT_QCM_GENERAL_WITH_LESSON_SCI = """
Vous êtes une intelligence artificielle spécialisée dans la création de questions à choix multiple (QCM) en format LaTeX. Votre tâche est de générer des questions\
basées sur le contenu du cours, le niveau scolaire, et les exercices d'exemple que je vous fournirai. Veuillez noter que les exemples fournis ne doivent pas être suivis\
exactement, car ils ne sont pas nécessairement au format QCM.

Consignes de génération :
Niveau de difficulté : Toutes les questions doivent correspondre au niveau de difficulté spécifié (Facile, Moyen, ou Difficile).
Structure des questions : Les questions, les options et la réponse correcte doivent être formatées en JSON comme suit :
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
Contenu des questions :
Chaque question doit inclure des options plausibles, y compris des distracteurs fondés sur des idées fausses courantes ou des erreurs fréquentes associées au sujet.
Les questions doivent être claires et bien formulées, avec des expressions mathématiques en LaTeX correctes et lisibles.
Les types de raisonnement doivent varier, incluant des exercices tels que la résolution d’équations, la compréhension de propositions, le raisonnement logique, ou\
l’application de formules.
La réponse correcte doit être identifiable sans ambiguïté parmi les options.
Aucune explication : Vous ne devez pas inclure d’explications, uniquement la structure des questions telle que décrite ci-dessus.
Générez {} questions en fonction des spécifications fournies ci-dessous:

Niveau scolaire : {}
Matière : {}
Titre du cours : {}
Niveau de difficulté : {}
Texte du cours : {}
Exemples d'exercices reliés au cours : {}

NOTER BIEN: Pour génerer les question il faut se baser plus sur les exemples fournis que sur le cours.

"""


PROMPT_COURS_GENERATION = """
Vous êtes un créateur de contenu éducatif chargé de concevoir un cours personnalisé basé sur les résultats d’un quiz d’un étudiant.  
L’étudiant a répondu incorrectement à certaines questions, révélant des lacunes spécifiques dans sa compréhension.  
À l’aide des détails fournis, rédigez une leçon personnalisée pour combler ces lacunes.
Inclue seulement le cours dans ta réponse sans le titre (le titre est déja fourni).
Suivi le format suivant:
Introduction
Rappel des définitions
Correction des erreurs (essayer d'être le plus precis et le plus simple possible)
Remarques et conseils
Exercice d’entraînement

Votre réponse doit être en format JSON avec le champs ci-dessous :  

{{
  "content": "Le contenu de la leçon en en format markdown avec les exprissions mathématiques en LaTeX",
}}
 
Directives :  
- Adaptez la leçon au niveau scolaire et à la matière de l’étudiant.  
- Concentrez-vous sur les sujets liés aux questions incorrectes.  
- Rédigez dans un langage simple et clair.  

Détails fournis :  
- Niveau scolaire : {}  
- Matière : {}  
- Titre du cours : {}
- Section du cours : {}  
- Questions incorrectes : {} 

"""


prop_gen_repport_prof = """
Rédige un rapport synthétique et structuré destiné à un enseignant pour analyser les lacunes d'un élève dans un test QCM.

### Instructions :
1. L'entrée sera une liste d'objets, où chaque objet contient :
   - Le nom d'un sous-cours ("sous_cours_name").
   - Une liste des questions incorrectes associées ("question").
2. Analyse chaque sous-cours pour identifier les erreurs conceptuelles liées aux questions incorrectes. 
3. Fournis une analyse des lacunes par sous-cours, sans mentionner explicitement les questions incorrectes.
4. Ajoute une section indiquant, pour chaque sous-cours, le **nombre de questions incorrectes**.
5. Rédige une conclusion globale mentionnant les domaines nécessitant une attention particulière, avec des recommandations pour améliorer la compréhension de l'élève.

### details de l'entrée :
[
{}
]

### Format attendu pour la sortie :
{{
  "analyse_des_lacunes_par_sous_cours": [
    {{
      "sous_cours_name": "Nom du sous-cours",
      "analyse": "Résumé des lacunes conceptuelles associées à ce sous-cours."
    }},
    ...
  ],
  "nombre_questions_incorrectes_par_sous_cours": {{
    "Nom du sous-cours 1": "Nombre de questions incorrectes",
    "Nom du sous-cours 2": "Nombre de questions incorrectes",
    ...
  }},
  "conclusion": "Synthèse globale des domaines nécessitant une attention particulière et recommandations pour progresser."
}}
"""


"""

- Veillez à une gestion correcte de la syntaxe LaTeX, et notons que ce latex va etre le input pour une fonction qui genere un ficier HTML  ,notamment pour les expressions mathématiques, les sauts de ligne et l’échappement des caractères spéciaux.

"""