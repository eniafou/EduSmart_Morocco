export interface SousPartieCours {
    id: number;
    title: string;
    content: string;
}





export const customizedCourse: SousPartieCours[] = [
    {
        id: 1,
        title: "Partie 1",
        content: "## Notion de Logique - **II. Quantificateurs**\n\n### Introduction\n\nDans cette leçon, nous allons clarifier l’utilisation des quantificateurs universel ($\\forall$) et existentiel ($\\exists$) en nous concentrant sur les propositions mal comprises dans vos réponses. Nous expliquerons leur usage et appliquerons ces notions à des exemples pour corriger vos erreurs.\n\n---\n\n### Rappel des définitions\n\n#### Le quantificateur existentiel ($\\exists$)\n- **Définition** : La proposition « $(\\exists x \\in E); P(x)$ » signifie : _« il existe au moins un $x \\in E$ tel que $P(x)$ est vraie »_.\n- **Véracité** : Cette proposition est vraie s’il existe au moins **un élément** $x \\in E$ qui satisfait la propriété $P(x)$.\n\n#### Le quantificateur universel ($\\forall$)\n- **Définition** : La proposition « $(\\forall x \\in E); P(x)$ » signifie : _« pour tout $x \\in E$, $P(x)$ est vraie »_.\n- **Véracité** : Cette proposition est vraie si **tous les éléments** de $E$ vérifient la propriété $P(x)$.\n\n---\n\n### Correction des erreurs\n\n#### Proposition $Q_1: (\\exists x \\in \\mathbb{R}); x^2 + x + 1 = 0$\n\n1. **Analyse**\n   - Cette proposition demande s’il existe un réel $x$ tel que $x^2 + x + 1 = 0$.\n   - Pour résoudre cette équation, calculons son discriminant :\n     $$\\Delta = b^2 - 4ac = 1^2 - 4(1)(1) = 1 - 4 = -3$$\n     - Le discriminant est négatif ($\\Delta < 0$), donc cette équation n’a **aucune solution réelle**.\n\n2. **Conclusion**\n   - La proposition est **fausse** car aucun $x \\in \\mathbb{R}$ ne vérifie $x^2 + x + 1 = 0$.\n\n#### Proposition $Q_3: (\\exists x \\in \\mathbb{N}); \\sqrt{x^2 + 3} = 2x - 4$\n\n1. **Analyse**\n   - Cette proposition demande s’il existe un entier naturel $x \\in \\mathbb{N}$ tel que $\\sqrt{x^2 + 3} = 2x - 4$.\n   - Élevons les deux membres au carré pour éliminer la racine :\n     $$x^2 + 3 = (2x - 4)^2$$\n     $$x^2 + 3 = 4x^2 - 16x + 16$$\n     $$0 = 3x^2 - 16x + 13$$\n   - Résolvons cette équation quadratique :\n     $$\\Delta = (-16)^2 - 4(3)(13) = 256 - 156 = 100$$\n     $$x = \\frac{-b \\pm \\sqrt{\\Delta}}{2a} = \\frac{16 \\pm 10}{6}$$\n     $$x = \\frac{26}{6} = \\frac{13}{3} \\quad \\text{ou} \\quad x = \\frac{6}{6} = 1$$\n     - $x = 1$ est le seul entier naturel.\n   - Vérification pour $x = 1$ :\n     $$\\sqrt{1^2 + 3} = \\sqrt{4} = 2, \\quad 2(1) - 4 = -2$$\n     - Les deux membres ne sont **pas égaux**, donc $x = 1$ ne satisfait pas l’équation.\n\n2. **Conclusion**\n   - La proposition est **fausse** car aucun $x \\in \\mathbb{N}$ ne vérifie $\\sqrt{x^2 + 3} = 2x - 4$.\n\n---\n\n### Remarques et conseils\n\n1. **Vérifiez les discriminants pour les équations quadratiques** : Si $\\Delta < 0$, aucune solution réelle n’existe.\n2. **Soyez attentif aux ensembles considérés ($\\mathbb{N}, \\mathbb{R}$, etc.)** : Une solution peut exister dans un ensemble mais pas dans un autre.\n3. **Vérifiez toujours les solutions candidates** après manipulation des équations (par exemple, après élévation au carré).\n\n---\n\n### Exercice d’entraînement\n\nPour renforcer votre compréhension, déterminez la valeur de vérité des propositions suivantes :\n\n1. $(\\forall x \\in \\mathbb{R}); x^2 \\geq 0$\n2. $(\\exists x \\in \\mathbb{R}); x^3 + 1 = 0$\n3. $(\\forall x \\in \\mathbb{N}); x^2 + x \\geq 2$\n\nExpliquez vos réponses en détaillant les étapes comme nous l’avons fait dans la leçon.\n",
    },
    {
        id: 2,
        title: "Partie 2",
        content: "Contenu de la partie 2",
    },
    {
        id: 3,
        title: "Partie 3",
        content: "Contenu de la partie 3",
    },
];