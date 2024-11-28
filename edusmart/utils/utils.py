import random
import os
import random
from openai import OpenAI
from dotenv import load_dotenv
import json
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

def get_exo_examples_from_dict():
    """
    load a .txt file containing an exercice, its solution and a some meta data all in the json format.
    """
    pass

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
