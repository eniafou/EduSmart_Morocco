import random
import os
import random
from openai import OpenAI
from dotenv import load_dotenv
import json
import pickle
import numpy as np
#from pylatex import Document, Section, Subsection, Command, Itemize, NoEscape
#from pylatex.utils import escape_latex
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[0]))
import constants.values as cv
import constants.prompts as pmt
import constants.names as cn

load_dotenv()
client = OpenAI()

def load_embeddings(file_path):
    """
    Load embeddings from a pickle file.
    """
    try:
        with open(file_path, 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return {}
def cosine_similarity(vec1, vec2):
    """
    Calculate the cosine similarity between two vectors.
    """
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    if norm_vec1 == 0 or norm_vec2 == 0:
        return 0.0
    return dot_product / (norm_vec1 * norm_vec2)

def get_similar_exo_cours(level = "lycee", year = "1_bac" , branch = "sci_math" , subject =  "math", lesson = "notion_de_logique", num_example_exo = 10):
    """
    load simple .txt file containing an exercice and its solution
    """
    full_path_exo_txt = "./database/" + level + "/" + year + "/" + branch + "/" + subject + "/" + lesson + "/exercices/embeddings.pkl"
    full_path_cour_txt = "./database/" + level + "/" + year + "/" + branch + "/" + subject + "/" + lesson + "/cours/embeddings.pkl"
    cour_embeddings = load_embeddings(full_path_cour_txt)
    exo_embeddings = load_embeddings(full_path_exo_txt)

    simcours = {}
    for cours_name, cours_embedding in cour_embeddings.items():
        similarities = [
            (exo_name, cosine_similarity(cours_embedding, exo_embedding))
            for exo_name, exo_embedding in exo_embeddings.items()
        ]
        # Sort by similarity in descending order and take top N
        top_similar = sorted(similarities, key=lambda x: x[1], reverse=True)[:num_example_exo]
        simcours[cours_name] = [name for name, _ in top_similar]
    return simcours  


    
def get_exo_examples_from_txt(level, year, branch, subject, lesson, num_example_exo = 3):
    """
    load simple .txt file containing an exercice and its solution
    """
    full_path_exo_txt = "./database/" + level + "/" + year + "/" + branch + "/" + subject + "/" + lesson + "/exercices/"
    all_exos = os.listdir(full_path_exo_txt)
    selected_exos = random.sample(all_exos, num_example_exo)
    output = []
    for exo in selected_exos:
        try:
            with open(full_path_exo_txt + exo, 'r') as file:
                output.append(file.read())
        except FileNotFoundError:
            print(f"The file at {full_path_exo_txt} was not found.")
    return output


def generate_quiz_pdf(data, include_correct_answers=False, output_file="quiz.pdf"):
    # Initialize the document
    doc = Document()

    # Add a title
    doc.preamble.append(Command("title", "Quiz"))
    doc.preamble.append(Command("author", "Generated Quiz"))
    doc.preamble.append(Command("date", NoEscape(r"\today")))
    doc.append(NoEscape(r"\maketitle"))

    # Loop through questions and add to the document
    for idx, item in enumerate(data['questions']):
        question = item['question']
        options = item['options']
        correct_answer = item['correct_answer']

        # Add question as a subsection
        with doc.create(Section(f"Question {idx + 1}")):
            doc.append(NoEscape(question))  # Use NoEscape to handle LaTeX
            doc.append("\n\n")

            # Add options as an itemized list
            with doc.create(Itemize()) as itemize:
                for option in options:
                    itemize.add_item(NoEscape(option))

            if include_correct_answers:
                doc.append(NoEscape(f"\n\n\\textbf{{Correct Answer: {escape_latex(correct_answer)}}}"))
    
    # Generate the PDF
    doc.generate_pdf(output_file, clean_tex=False)


def generate_general_qcm(level, year, branch, subject, lesson, difficulty, num_questions):
    example_exos = get_exo_examples_from_txt(level, year, branch, subject, lesson, cv.num_example_exo)
    example_exos = "\n\n".join(example_exos)
    prompt = pmt.PROMPT_QCM_GENERAL_SCI.format(5,f"{cn.level_mapping[level]} {cn.year_mapping[year]} {cn.branch_mapping[branch]} Maroc", cn.subject_mapping[subject], cn.lesson_mapping[lesson], difficulty, example_exos)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        response_format = { "type": "json_object" }
    )
    return json.loads(completion.choices[0].message.content)



def save_qcm_to_html(qcm_data, output_file="qcm_output.html"):
    """
    Convert QCM data to a formatted HTML file with properly separated text and LaTeX
    """
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>QCM Questions</title>
        <meta charset="UTF-8">
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 900px;
                margin: 0 auto;
                padding: 20px;
                line-height: 1.6;
            }
            .question {
                margin-bottom: 30px;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            .question-text {
                font-weight: bold;
                margin-bottom: 15px;
                font-size: 1.2em;
            }
            .question-content {
                margin-bottom: 15px;
                font-style: italic;
            }
            .options {
                margin-left: 20px;
            }
            .option {
                margin: 15px 0;
                padding: 10px;
                background-color: white;
                border-radius: 4px;
                border: 1px solid #eee;
            }
            .correct-answer {
                color: #2e7d32;
                font-weight: bold;
                margin-top: 15px;
                padding: 10px;
                background-color: #e8f5e9;
                border-radius: 5px;
            }
        </style>
        <script>
            MathJax = {
                tex: {
                    inlineMath: [['$', '$']],
                    displayMath: [['$$', '$$']],
                    processEscapes: true,
                    packages: ['base', 'ams', 'noerrors', 'noundefined']
                }
            };
        </script>
        <script id="MathJax-script" async 
            src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
        </script>
    </head>
    <body>
        <h1>QCM Questions</h1>
    """
    
    def fix_latex(text):
        """Clean up LaTeX formatting"""
        # Remove extra backslashes and fix spacing
        text = text.replace('\\\\', '\\')
        # Ensure math expressions are properly delimited
        if '\\mathbb' in text or '\\forall' in text or '\\exists' in text or '\\geq' in text:
            if not text.startswith('$'):
                text = '$' + text
            if not text.endswith('$'):
                text = text + '$'
        return text

    def process_option(option):
        """Process each option to separate letter label and content"""
        parts = option.split(' - ', 1)
        if len(parts) == 2:
            label, content = parts
            return f"{label} - {fix_latex(content)}"
        return fix_latex(option)

    # Add each question
    for i, item in enumerate(qcm_data['data'], 1):
        question = fix_latex(item['question'])
        
        html_content += f"""
        <div class="question">
            <div class="question-text">Question {i}:</div>
            <div class="question-content">{question}</div>
            <div class="options">
        """
        
        # Add options
        for option in item['options']:
            processed_option = process_option(option)
            html_content += f'<div class="option">{processed_option}</div>'
        
        # Add correct answer
        html_content += f"""
            </div>
            <div class="correct-answer">Correct Answer: {item['correct_answer']}</div>
        </div>
        """
    
    html_content += """
    </body>
    </html>
    """
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"QCM has been saved to {output_file}")

