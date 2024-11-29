input_data= {'answers': [{'sous_cours_name': 'Lois logiques et raisonnements', 'answers': [0, 1, 1]},
            {'sous_cours_name': 'Opérations sur les propositions', 'answers': [1, 2, 0]}, 
            {'sous_cours_name': 'Proposition - fonction propositionnelle', 'answers': [1, 0, 2]}, 
            {'sous_cours_name': 'Quantificateurs', 'answers': [3, 2, 0]}], 
'qcm': [{'content': [{'correct_answer': 'A', 'options': ['A - Une tautologie', 'B - Une contradiction', 'C - Une proposition contingent', 'D - Une négation'], 'question': 'Quelle loi logique est représentée par la proposition $P \\implies (Q \\implies P)$ ?'}, 
                    {'correct_answer': 'A', 'options': ['A - $\\neg P \\lor \\neg Q$', 'B - $\\neg P \\land \\neg Q$', 'C - $P \\lor Q$', 'D - $\\neg Q \\land P$'], 'question': 'Parmi les propositions suivantes, laquelle est équivalente à $\\neg (P \\land Q)$ selon les lois de Morgan ?'}, 
                    {'correct_answer': 'B', 'options': ['A - $\\neg P \\implies \\neg Q$', 'B - $\\neg Q \\implies \\neg P$', 'C - $Q \\implies P$', 'D - $P \\lor Q$'], 'question': 'Laquelle des propositions suivantes représente la contraposée de $P \\implies Q$ ?'}], 
        'sous_cours_name': 'Lois logiques et raisonnements'}, 
        {'content': [{'correct_answer': 'A', 'options': ['A - $\\exists x \\in \\mathbb{R}, x^2 < 0$', 'B - $\\exists x \\in \\mathbb{R}, x^2 > 0$', 'C - $\\forall x \\in \\mathbb{R}, x^2 = 0$', 'D - $\\exists x \\in \\mathbb{R}, x^2 = 0$'], 'question': 'Quelle est la négation de la proposition suivante : $\\forall x \\in \\mathbb{R}, x^2 \\geq 0$ ?'}, 
                        {'correct_answer': 'A', 'options': ['A - $\\forall y \\in \\mathbb{R}, y^3 \\neq -2$', 'B - $\\exists y \\in \\mathbb{R}, y^3 \\neq -2$', 'C - $\\forall y \\in \\mathbb{R}, y^3 = -2$', 'D - $\\exists y \\in \\mathbb{R}, y^3 = 0$'], 'question': 'Comment exprimer la négation de la proposition $\\exists y \\in \\mathbb{R}, y^3 = -2$ ?'}, 
                        {'correct_answer': 'A', 'options': ['A - Elle est fausse seulement si $P$ et $Q$ sont toutes deux fausses.', 'B - Elle est vraie seulement si $P$ et $Q$ sont toutes deux vraies.', 'C - Elle est vraie si $P$ est vraie et $Q$ est fausse.', 'D - Elle est toujours fausse.'], 'question': 'Laquelle des propositions suivantes est une définition correcte de la disjonction $P \\text{ ou } Q$ ?'}], 
        'sous_cours_name': 'Opérations sur les propositions'}, 
        {'content': [{'correct_answer': 'C', 'options': ['A - $P : \\sqrt[3]{5} = \\frac{5}{\\sqrt[3]{25}}$', 'B - $Q : \\frac{3-5}{2} = -1$', 'C - $R : \\cos\\left(\\frac{\\pi}{7}\\right) > 1$', "D - $S :$ Les solutions de l'équation $2018x^2 + 2017x - 1 = 0$ sont $1$ et $-\\frac{1}{2018}$"], 'question': 'Laquelle des propositions suivantes est fausse ?'}, 
                        {'correct_answer': 'C', 'options': ['A - $y = -\\frac{1}{3}$', 'B - $y = \\frac{1}{3}$', 'C - $y = \\frac{5}{3}$', 'D - $y = -5$'], 'question': "Considérant la fonction propositionnelle $P(x, y) : 2x - 3y = 7$, quel est l'ensemble des valeurs de $y$ pour lesquelles $P(2, y)$ est vrai ?"}, 
                        {'correct_answer': 'A', 'options': ['A - Tout $x \\in \\mathbb{R}$', 'B - $x \\leq -1$', 'C - $x \\geq 6$', 'D - Pas de solutions réelles'], 'question': 'Quel ensemble de solutions $S$ permet de rendre la proposition $D(x) : x^2 + x + 6 \\geq 0$ toujours vraie ?'}], 
        'sous_cours_name': 'Proposition - fonction propositionnelle'}, 
        {'content': [{'correct_answer': 'B', 'options': ['A - Vraie, car il existe des nombres réels qui satisfont cette équation.', 'B - Fausse, car le discriminant est négatif.', "C - Vraie, car l'équation a une solution réelle.", 'D - Fausse, car il existe au moins une solution négative.'], 'question': 'Déterminez la valeur de vérité de la proposition suivante : $Q_1: (\\exists x \\in \\mathbb{R}); x^2 + x + 1 = 0$'}, 
                        {'correct_answer': 'B', 'options': ['A - Vraie, car cela implique une équation quadratique avec des solutions entières.', 'B - Fausse, car $2x - 4$ ne peut pas être négatif.', 'C - Vraie, car il peut y avoir des solutions pour des x réels.', 'D - Fausse, ceci est vrai pour tout $x \\in \\mathbb{Z}$.'], 'question': 'Laquelle des propositions suivantes est vraie ? $Q_3: (\\exists x \\in \\mathbb{N}); \\sqrt{x^2 + 3} = 2x - 4$'}, 
                        {'correct_answer': 'A', 'options': ['A - Vraie, car $x=1$ satisfait cette condition.', 'B - Fausse, car tous les $x$ ne peuvent pas donner 1.', 'C - Vraie, car $x$ peut être 0.', 'D - Fausse, car le résultat varie selon $y$.'], 'question': 'Évaluez la proposition : $Q_5: (\\exists x \\in \\mathbb{R}^)(\\forall y \\in \\mathbb{Z}^); x^y = 1$.'}], 
        'sous_cours_name': 'Quantificateurs'}]}


import json

def compare_answers(input_data):
    results = {}

    for course in input_data['answers']:
        sous_cours_name = course['sous_cours_name']
        user_answers = course['answers']
        
        # Find the corresponding qcm content
        qcm_content = next((item for item in input_data['qcm'] if item['sous_cours_name'] == sous_cours_name), None)
        
        if qcm_content:
            for i, question in enumerate(qcm_content['content']):
                correct_answer = question['correct_answer']
                user_answer_index = user_answers[i]
                
                # Convert user answer index to corresponding option letter (A, B, C, D)
                user_answer_letter = chr(65 + user_answer_index)  # 65 is ASCII for 'A'
                
                if user_answer_letter != correct_answer:
                    if sous_cours_name not in results:
                        results[sous_cours_name] = []
                    results[sous_cours_name].append(question['question'])
    
    # Convert results to the desired output format
    formatted_results = [
        {"sous_cours_name": key, "question": value}
        for key, value in results.items()
    ]
    
    return formatted_results

wrong_answers = compare_answers(input_data)

with open('wrong_answers.json', 'w', encoding='utf-8') as f:
    json.dump(wrong_answers, f, ensure_ascii=False, indent=4)

print("Results saved to 'wrong_answers.json'")
