example_generated_qcm = '{\n  "data": [\n    {\n      "question": "Montrer que pour tout $(a, b) \\\\in \\\\mathbb{R}^2$, si $a^2 + b^2 = 1$, alors $|a - b| \\\\leq \\\\sqrt{2}$.",\n      "options": [\n        "A - $|a - b| \\\\geq 0$",\n        "B - $|a - b| = 1$",\n        "C - $|a - b| \\\\leq \\\\sqrt{2}$",\n        "D - $|a - b| \\\\leq 1$"\n      ],\n      "correct_answer": "C"\n    },\n    {\n      "question": "Si $x, y \\\\in \\\\mathbb{R}^+$, lequel des énoncés suivants est vrai si $x + y = 2$ ?",\n      "options": [\n        "A - $\\\\sqrt{x} + \\\\sqrt{y} \\\\leq 2$",\n        "B - $\\\\sqrt{x + y} = 1$",\n        "C - $\\\\sqrt{x} - \\\\sqrt{y} = 0$",\n        "D - $|x - y| \\\\leq 2$"\n      ],\n      "correct_answer": "A"\n    },\n    {\n      "question": "Pour tout $x \\\\in \\\\mathbb{R}$, montrez que $|x + 1| \\\\geq 1$ si $x \\\\leq 0$.",\n      "options": [\n        "A - Cela est faux pour $x = -2$",\n        "B - Cela est vrai seulement pour $x = 0$",\n        "C - Cela est vrai pour tout $x < 0$",\n        "D - Cela est vrai pour tout $x > 0$"\n      ],\n      "correct_answer": "C"\n    },\n    {\n      "question": "Si $x \\\\in \\\\mathbb{R}$, quel est le meilleur moyen d\'exprimer $|x - 3| < 5$ en termes d\'inégalités ?",\n      "options": [\n        "A - $-5 < x < 8$",\n        "B - $-2 < x < 8$",\n        "C - $3 - 5 < x < 3 + 5$",\n        "D - $0 < x < 6$"\n      ],\n      "correct_answer": "C"\n    },\n    {\n      "question": "Montrez que pour tout $x \\\\in \\\\mathbb{R}$, $|x^2 - 1| \\\\leq |x - 1| \\\\cdot |x + 1|$. Quelle est la bonne formulation ?",\n      "options": [\n        "A - C\'est faux car $|x - 1| < 0$",\n        "B - C\'est vrai seulement pour $x = 0$",\n        "C - C\'est une inégalité toujours vraie pour $x \\\\in \\\\mathbb{R}$",\n        "D - C\'est vrai seulement pour $x > 1$"\n      ],\n      "correct_answer": "C"\n    }\n  ]\n}'
example_generated_qcm_v2 = """{'data': [{'sous_cours_name': 'Lois logiques et raisonnements', 'content': [{'question': "Quelle est la définition d'une loi logique ou tautologie ?", 'options': ['A - Une proposition qui est vraie pour certaines valeurs de vérité des propositions qui la composent.', "B - Une proposition résultante de l'assemblage par des connecteurs logiques qui est toujours vraie.", 'C - Une proposition qui est fausse quelle que soit la valeur de vérité des propositions en jeu.', 'D - Une proposition qui est vraie seulement dans des cas spécifiques.'], 'correct_answer': 'B'}, {'question': 'Quelle est la forme correcte de la loi de Morgan pour deux propositions P et Q ?', 'options': ['A - (P ∧ Q) ≡ (¬P ∧ ¬Q)', 'B - (P ∨ Q) ≡ (¬P ∨ ¬Q)', 'C - (P ∧ Q) ≡ (¬P ∨ ¬Q)', 'D - (P ∨ Q) ≡ (¬P ∧ ¬Q)'], 'correct_answer': 'A'}, {'question': "Quelle est la contraposée de l'implication P ⇒ Q ?", 'options': ['A - Q ⇒ P', 'B - ¬Q ⇒ ¬P', 'C - P ∧ ¬Q', 'D - ¬P ⇒ ¬Q'], 'correct_answer': 'B'}]}, {'sous_cours_name': 'Opérations sur les propositions', 'content': [{'question': 'Quelle est la négation de la proposition $\\forall x \\in \\mathbb{R}, x^2 \\geq 0$?', 'options': ['A - $\\exists x \\in \\mathbb{R}, x^2 < 0$', 'B - $\\forall x \\in \\mathbb{R}, x^2 < 0$', 'C - $\\exists x \\in \\mathbb{R}, x^2 \\geq 0$', 'D - $\\forall x \\in \\mathbb{R}, x^2 > 0$'], 'correct_answer': 'A'}, {'question': 'Si $P$ est la proposition "$\\exists x \\in \\mathbb{R}, x^3 = -2$", quelle est sa négation?', 'options': ['A - $\\forall x \\in \\mathbb{R}, x^3 \\neq -2$', 'B - $\\forall x \\in \\mathbb{R}, x^3 = -2$', 'C - $\\exists x \\in \\mathbb{R}, x^3 \\neq -2$', 'D - $\\exists x \\in \\mathbb{R}, x^3 = -3$'], 'correct_answer': 'A'}, {'question': 'La proposition "$\\forall x \\in [0,1], x^2 \\geq x$" est-elle vraie ou fausse?', 'options': ['A - Vraie', 'B - Fausses pour tous les $x$', 'C - Il existe $x \\in [0,1]$ tel que $x^2 < x$', 'D - Toujours vraie pour $x = 0$'], 'correct_answer': 'C'}]}, {'sous_cours_name': 'Proposition - fonction propositionnelle', 'content': [{'question': 'La phrase : « Les nombres positifs sont des entiers naturels » est-elle une proposition ? Justifier.', 'options': ["A - Oui, c'est une proposition car elle a une signification claire.", "B - Non, c'est une proposition car elle est fausse.", "C - Non, ce n'est pas une proposition car elle peut être juste ou fausse.", "D - Oui, c'est une proposition car elle est toujours vraie."], 'correct_answer': 'B'}, {'question': 'Déterminez la valeur de vérité de la proposition $R : \\cos\\left(\\frac{\\pi}{7}\\right) > 1$.', 'options': ['A - Vraie, car $\\cos$ est supérieur à 1 pour certains angles.', 'B - Fausse, car $\\cos$ ne peut pas dépasser 1.', 'C - Peut-être vraie, selon les valeurs de $\\pi$.', 'D - Vraie, car $\\frac{\\pi}{7}$ est un angle acute.'], 'correct_answer': 'B'}, {'question': 'Pour quelle valeur de $y$ la fonction propositionnelle $P(2, y) : 2(2) - 3y = 7$ est-elle vraie ?', 'options': ['A - $y = -\\frac{1}{3}$', 'B - $y = 2$', 'C - $y = -1$', 'D - $y = 1$'], 'correct_answer': 'A'}]}, {'sous_cours_name': 'Quantificateurs', 'content': [{'question': 'Considérant la proposition $Q: (\\exists x \\in \\mathbb{R}); x^2 + 1 = 0$, quelle est sa valeur de vérité ?', 'options': ['A - Vraie car il existe une solution complexe.', 'B - Fausse car $x^2 + 1 > 0$ pour tout $x \\in \\mathbb{R}$.', 'C - Vraie car $x^2 + 1 < 0$ pour certains $x$.', 'D - Fausse car $x^2 + 1$ est toujours positif.'], 'correct_answer': 'B'}, {'question': 'La proposition $Q: (\\forall x \\in \\mathbb{R})(\\exists y \\in \\mathbb{R}); x + y = 0$ est-elle vraie ?', 'options': ['A - Vraie, car pour chaque $x$, $y$ peut être défini comme $-x$.', "B - Fausse, car il n'y a pas de $y$ pour $x = 0$.", 'C - Vraie, car $y$ existe toujours pour $x > 0$.', 'D - Fausse, car $y$ doit toujours être positif.'], 'correct_answer': 'A'}, {'question': 'Analysons la proposition $Q: (\\exists x \\in \\mathbb{N})(\\forall y \\in \\mathbb{N}); x \\leq y$. Quel est son statut ?', 'options': ['A - Vraie, car $x$ peut être 0.', "B - Fausse, car il n'existe pas de $x$ qui soit inférieur ou égal à tous les $y$.", 'C - Vraie, car tout nombre naturel est supérieur ou égal à 0.', 'D - Fausse, car tous les $y$ ne peuvent pas être supérieurs à $x$.'], 'correct_answer': 'B'}]}]}"""
EXO_PATH_EMBEDDING_SUFFIX = "/exercices/embeddings.pkl"
SOUS_COURS_PATH_EMBEDDING_SUFFIX = "/cours/embeddings.pkl"
ROOT_DATABASE_PATH = "./database/"
OPENAI_MODEL = "gpt-4o-mini"
NUM_SIMILARITY_EXO = 15
NUM_PRMPT_EXO = 2 # must be less or equal to NUM_SIMILAR_EXO
TEMPERATURE = 1

